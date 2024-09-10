import Levenshtein
from difflib import SequenceMatcher
import pandas as pd
from scripts import get_rag_chain
from tqdm import tqdm
from config import config
import numpy as np


def similarity_score(answer1, answer2):
    return SequenceMatcher(None, answer1, answer2).ratio()


def levenshtein_similarity(pred, true_answer):
    distance = Levenshtein.distance(pred, true_answer)
    max_len = max(len(pred), len(true_answer))
    return 1 - (distance / max_len)


def get_metrics(df, test_percentage=1):

    sample_size = int(len(df) * test_percentage)
    df_sample = df.sample(sample_size, random_state=42).reset_index(drop=True)

    rag_model = get_rag_chain(**config)
    similarity_scores = []
    levenshtein_scores = []

    for index, row in tqdm(df_sample.iterrows(), total=len(df_sample)):
        question = row['question']
        true_answer = row['content']
        pred_answer = rag_model.invoke(
            {'input': question},
            config={'configurable': {'session_id': str(index)}}
        )['answer']

        similarity = similarity_score(pred_answer, true_answer)
        levenshtein_sim = levenshtein_similarity(pred_answer, true_answer)

        similarity_scores.append(similarity)
        levenshtein_scores.append(levenshtein_sim)

    avg_similarity = np.mean(similarity_scores)
    avg_levenshtein = np.mean(levenshtein_scores)

    return {
        'average_similarity_score': avg_similarity,
        'average_levenshtein_similarity': avg_levenshtein
    }


if __name__ == '__main__':

    df = pd.read_csv('real_data_test.csv')
    metrics = get_metrics(df, test_percentage=1) # test_percentage - используемая доля тестового датафрейма
    print(metrics)

