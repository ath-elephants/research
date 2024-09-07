# Лог экспериментов

4:06 5/9: в rubert-tiny2.ipynb завел rubert-tiny2, пока valid accuracy = 0.04

модель: <https://huggingface.co/cointegrated/rubert-tiny2>

11:25 5/9: в rubert-tiny2.ipynb:

1. добавил аугментации текста от xenopupei

2. убрал уникальные ответы, стратифицированно разделил

получил valid accuracy = 0.6051, precision = 0.6154, recall = 0.6051, f1 = 0.5972

3:04 7/9:

1. добавил ноутбук для генерации синтетики на gemini-1.5-flash

2. потестил langchain на наших данных, пока без метрик
