# Первый тест rag

## Чистый данные, откинув <=3 классы

|  **Параметры**: | **Метрики** |
| --------------- |-------------|
|   'model_name': 'llama3.1:8b', </br> 'embed_name': 'nomic-embed-text:v1.5',</br> </br>'search_type': 'similarity_score_threshold',</br> 'k': 5,</br> 'score_threshold': 0.6 | similarity: 0.56, </br> levenshtein: 0.54, </br> jaccard: 0.48, </br> bleu: 0.46
