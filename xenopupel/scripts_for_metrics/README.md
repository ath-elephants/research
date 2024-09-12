# Метрики разных эмбедингов и генераторов

## train_synthetic_no_aug, дефолтные параметры

| LLM x Embeddings                              | Avg Similarity Score | Avg Levenshtein Similarity | Avg Jaccard Similarity | Avg BLEU Score |
|------------------------------------------------------------|----------------------|----------------------------|------------------------|----------------|
| **Случайные ответы**                                       | 0.1346               | 0.1865                     | 0.0419                 | 0.0074         |
| **llama 3.1 8b** x **nomic-ai/nomic-embed-text-v1.5 137m** | 0.5378               | 0.5642                     | 0.4548                 | 0.4343         |
| **llama 3.1 8b** x **sergeyzh/rubert-tiny-turbo 29.2m**    | 0.6374               | 0.6561                     | 0.5534                 | 0.5375         |
| **llama 3.1 8b** x **Alibaba-NLP/gte-base-en-v1.5 137m**   | 0.6532               | 0.6708                     | 0.5743                 | 0.5614         |
| **llama 3.1 8b** x **deepvk/USER-base 124m**               | 0.6768               | 0.6868                     | 0.5957                 | 0.5802         |
| **llama 3.1 8b** x **ai-forever/ru-en-RoSBERTa 404m**      | 0.7237               | 0.7310                     | 0.6416                 | 0.6293         |

## Чистые данные, откинув <=3 классы

|  **Параметры**: | **Метрики** |
| --------------- |-------------|
|   'model_name': 'llama3.1:8b', </br> 'embed_name': 'nomic-embed-text:v1.5',</br> </br>'search_type': 'similarity_score_threshold',</br> 'k': 5,</br> 'score_threshold': 0.6 | similarity: 0.56, </br> levenshtein: 0.54, </br> jaccard: 0.48, </br> bleu: 0.46 |
| --------------- |-------------|
| --------------- |-------------|

## Случайные ответы

test_synthetic_no_aug.csv: \
'average_similarity_score': 0.13457999885072489, \
'average_levenshtein_similarity': 0.18647395423123936, \
'average_jaccard_similarity': 0.041879182347742946, \
'average_bleu_score': 0.0073593233482635995

test_synthetic_aug.csv: \
'average_similarity_score': 0.13246022000712718, \
'average_levenshtein_similarity': 0.19154487555131322, \
'average_jaccard_similarity': 0.044492837472662784, \
'average_bleu_score': 0.00940852604646604
