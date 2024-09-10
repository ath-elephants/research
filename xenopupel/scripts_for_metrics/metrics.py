import Levenshtein
from difflib import SequenceMatcher
import pandas as pd
from scripts import get_rag_chain
from tqdm import tqdm
from config import config
import numpy as np
from nltk.translate.bleu_score import sentence_bleu

def similarity_score(answer1, answer2):
    return SequenceMatcher(None, answer1, answer2).ratio()


def levenshtein_similarity(pred, true_answer):
    distance = Levenshtein.distance(pred, true_answer)
    max_len = max(len(pred), len(true_answer))
    return 1 - (distance / max_len)


def jaccard_similarity(pred, true_answer):
    pred_set = set(pred.split())
    true_set = set(true_answer.split())
    intersection = pred_set.intersection(true_set)
    union = pred_set.union(true_set)
    return len(intersection) / len(union)


def bleu_score(pred, true_answer):
    pred_tokens = pred.split()
    true_tokens = [true_answer.split()]
    return sentence_bleu(true_tokens, pred_tokens)


def get_metrics(df, test_percentage=1):

    sample_size = int(len(df) * test_percentage)
    df_sample = df.sample(sample_size, random_state=42).reset_index(drop=True)

    rag_model = get_rag_chain(**config)
    similarity_scores = []
    levenshtein_scores = []
    jaccard_scores = []
    bleu_scores = []

    for index, row in tqdm(df_sample.iterrows(), total=len(df_sample)):
        question = row['question']
        true_answer = row['content']
        pred_answer = rag_model.invoke(
            {'input': question},
            config={'configurable': {'session_id': str(index)}}
        )['answer']

        similarity = similarity_score(pred_answer, true_answer)
        levenshtein_sim = levenshtein_similarity(pred_answer, true_answer)
        jaccard_sim = jaccard_similarity(pred_answer, true_answer)
        bleu = bleu_score(pred_answer, true_answer)

        similarity_scores.append(similarity)
        levenshtein_scores.append(levenshtein_sim)
        jaccard_scores.append(jaccard_sim)
        bleu_scores.append(bleu)

    avg_similarity = np.mean(similarity_scores)
    avg_levenshtein = np.mean(levenshtein_scores)
    avg_jaccard = np.mean(jaccard_scores)
    avg_bleu = np.mean(bleu_scores)

    return {
        'average_similarity_score': avg_similarity,
        'average_levenshtein_similarity': avg_levenshtein,
        'average_jaccard_similarity': avg_jaccard,
        'average_bleu_score': avg_bleu
    }


if __name__ == '__main__':

    df = pd.read_csv('real_data_test.csv')
    metrics = get_metrics(df, test_percentage=1) # test_percentage - используемая доля тестового датафрейма [0;1]
    print(metrics)

