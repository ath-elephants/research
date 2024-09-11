## synth_no_aug, дефолтные параметры:
'average_similarity_score': 0.5378277933070031,
'average_levenshtein_similarity': 0.5641647351233865,
'average_jaccard_similarity': 0.45478534600813675,
'average_bleu_score': 0.4343468795510984

## Чистые данные, откинув <=3 классы

|  **Параметры**: | **Метрики** |
| --------------- |-------------|
|   'model_name': 'llama3.1:8b', </br> 'embed_name': 'nomic-embed-text:v1.5',</br> </br>'search_type': 'similarity_score_threshold',</br> 'k': 5,</br> 'score_threshold': 0.6 | similarity: 0.56, </br> levenshtein: 0.54, </br> jaccard: 0.48, </br> bleu: 0.46 |
| --------------- |-------------|
| --------------- |-------------|


## Случайные ответы:

test_synthetic_no_aug.csv:
'average_similarity_score': 0.13457999885072489,
'average_levenshtein_similarity': 0.18647395423123936,
'average_jaccard_similarity': 0.041879182347742946,
'average_bleu_score': 0.0073593233482635995

test_synthetic_aug.csv:
'average_similarity_score': 0.13246022000712718,
'average_levenshtein_similarity': 0.19154487555131322,
'average_jaccard_similarity': 0.044492837472662784,
'average_bleu_score': 0.00940852604646604
