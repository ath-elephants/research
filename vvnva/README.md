### Прирост метрик на основе исходных данных без ситетики и аугментации - rubert:

| Metric        | Без обработки       | -concat category  <br> -.str.lower()         |
|---------------|---------------------|---------------------|
| Accuracy      | 0.6108              | 0.7938              |
| Precision     | macro: 0.4940, micro: 0.6108 | macro: 0.6029, micro: 0.7938 |
| Recall        | macro: 0.4877, micro: 0.6108 | macro: 0.6112, micro: 0.7938 |
| F1 Score      | macro: 0.4757, micro: 0.6108 | macro: 0.5934, micro: 0.7938 |




## Саммари по аугментациям 
### с синтетикой
| Augmentation                                             | sber-gpt                                                                                                                                                                  | navec                                                                                                                                                                     | rubert                                                                                                                                                                    |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| shuffle_words, introduce_typo, add_or_remove_punctuation | **Accuracy**: 0.8436 <br> **Precision**: (macro: 0.8129, micro: 0.8436) <br> **Recall**: (macro: 0.8611, micro: 0.8436) <br> **F1 Score**: (macro: 0.8147, micro: 0.8436) | **Accuracy**: 0.7930 <br> **Precision**: (macro: 0.7049, micro: 0.7930) <br> **Recall**: (macro: 0.7784, micro: 0.7930) <br> **F1 Score**: (macro: 0.7118, micro: 0.7930) | **Accuracy**: 0.7672 <br> **Precision**: (macro: 0.6452, micro: 0.7672) <br> **Recall**: (macro: 0.7461, micro: 0.7672) <br> **F1 Score**: (macro: 0.6540, micro: 0.7672) |
| "cointegrated/rut5-base-paraphraser"                     | **Accuracy**: 0.8346 <br> **Precision**: (macro: 0.7833, micro: 0.8346) <br> **Recall**: (macro: 0.8212, micro: 0.8346) <br> **F1 Score**: (macro: 0.7804, micro: 0.8346) | **Accuracy**: 0.7683 <br> **Precision**: (macro: 0.6713, micro: 0.7683) <br> **Recall**: (macro: 0.7498, micro: 0.7683) <br> **F1 Score**: (macro: 0.6813, micro: 0.7683) | **Accuracy**: 0.7672 <br> **Precision**: (macro: 0.6452, micro: 0.7672) <br> **Recall**: (macro: 0.7461, micro: 0.7672) <br> **F1 Score**: (macro: 0.6540, micro: 0.7672) |
| "Helsinki-NLP/opus-mt-ru-en"                             | **Accuracy**: 0.8268 <br> **Precision**: (macro: 0.7827, micro: 0.8268) <br> **Recall**: (macro: 0.8244, micro: 0.8268) <br> **F1 Score**: (macro: 0.7790, micro: 0.8268) | **Accuracy**: 0.7672 <br> **Precision**: (macro: 0.6452, micro: 0.7672) <br> **Recall**: (macro: 0.7461, micro: 0.7672) <br> **F1 Score**: (macro: 0.6540, micro: 0.7672) | **Accuracy**: 0.7514 <br> **Precision**: (macro: 0.6879, micro: 0.7514) <br> **Recall**: (macro: 0.7462, micro: 0.7514) <br> **F1 Score**: (macro: 0.6809, micro: 0.7514) |
| Без аугментации                                          | **Accuracy**: 0.8245 <br> **Precision**: (macro:0.7796, micro:0.8245) <br> **Recall**: (macro:0.8320, micro:0.8245) <br> **F1 Score**: (macro:0.7770, micro:0.8245)       | **Accuracy**: 0.7289 <br> **Precision**: (macro:0.6038, micro:0.7289) <br> **Recall**: (macro:0.7047, micro:0.7289) <br> **F1 Score**: (macro:0.6012, micro:0.7289)       | **Accuracy**: 0.7537 <br> **Precision**: (macro:0.7074, micro:0.7537) <br> **Recall**: (macro:0.7431, micro:0.7537) <br> **F1 Score**: (macro:0.6826, micro:0.7537)       |
### На оригинальных c откидыванием частот = 3
| Augmentation                                             | sber-gpt                                                                                                                                                                  | navec                                                                                                                                                                     | rubert                                                                                                                                                              |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| shuffle_words, introduce_typo, add_or_remove_punctuation | **Accuracy**: 0.8753 <br> **Precision**: (macro:0.7698, micro:0.8753) <br> **Recall**: (macro:0.7885, micro:0.8753) <br> **F1 Score**: (macro:0.7675, micro:0.8753)       | **Accuracy**: 0.8338  <br> **Precision**: (macro:0.6841, micro:0.8338) <br> **Recall**: (macro:0.6892, micro:0.8338) <br> **F1 Score**: (macro:0.6675, micro:0.8338)      | **Accuracy**: 0.8260 <br> **Precision**: (macro:0.6691, micro:0.8260) <br> **Recall**: (macro:0.7024, micro:0.8260) <br> **F1 Score**: (macro:0.6695, micro:0.8260) |
| "cointegrated/rut5-base-paraphraser"                     | **Accuracy**: 0.8416 <br> **Precision**: (macro:0.6916, micro:0.8416) <br> **Recall**: (macro:0.6993, micro:0.8416) <br> **F1 Score**: (macro:0.6849, micro:0.8416)       | **Accuracy**: 0.8468 <br> **Precision**: (macro:0.6958, micro:0.8468) <br> **Recall**: (macro:0.7077, micro:0.8468) <br> **F1 Score**: (macro:0.6876, micro:0.8468)       | **Accuracy**: 0.8026 <br> **Precision**: (macro:0.6943, micro:0.8026) <br> **Recall**: (macro:0.7237, micro:0.8026) <br> **F1 Score**: (macro:0.6966, micro:0.8026) |
| "Helsinki-NLP/opus-mt-ru-en"                             | **Accuracy**: 0.8442 <br> **Precision**: (macro:0.6800, micro:0.8442) <br> **Recall**: (macro:0.7052, micro:0.8442) <br> **F1 Score**: (macro:0.6794, micro:0.8442)       | **Accuracy**: 0.8130 <br> **Precision**: (macro:0.5711, micro:0.8130) <br> **Recall**: (macro:0.6129, micro:0.8130) <br> **F1 Score**: (macro:0.5754, micro:0.8130)       | **Accuracy**: 0.7844 <br> **Precision**: (macro:0.5949, micro:0.7844) <br> **Recall**: (macro:0.6374, micro:0.7844) <br> **F1 Score**: (macro:0.6001, micro:0.7844) |
| Без аугментации                                          | **Accuracy**: 0.8494 <br> **Precision**: (macro:0.6784, micro:0.8494) <br> **Recall**: (macro:0.7001, micro:0.8494) <br> **F1 Score**: (macro:0.6762, micro:0.8494)       | **Accuracy**: 0.7896 <br> **Precision**: (macro:0.5465, micro:0.7896) <br> **Recall**: (macro:0.5355, micro:0.7896) <br> **F1 Score**: (macro:0.5277, micro:0.7896)       | **Accuracy**: 0.7766 <br> **Precision**: (macro:0.5897, micro:0.7766) <br> **Recall**: (macro:0.5965, micro:0.7766) <br> **F1 Score**: (macro:0.5759, micro:0.7766) |


                                         __
                                        / _)
                               _.----._/ /
                              /         /
                          __/ (  | (  |
                          /__.-'|_|--|_|

[почему микро метрики равны между собой](https://stackoverflow.com/questions/74440410/sklearn-evaluate-accuracy-precision-recall-f1-show-same-result?noredirect=1&lq=1)

## Яндекс Клауд
Нам дали промокод на 5к, тарифы Yandex Cloud зависят от мощности ресурсов и времени использования.

### Конфигурации и цены:
Есть готовые [тарифы](https://yandex.cloud/en/docs/datasphere/pricing)

| Конфигурация                  | Потребление (юнитов/сек) | Цена за 1 час (с НДС) |
|-------------------------------|--------------------------|-----------------------|
| **c1.4 (4 vCPU, 0 GPU)**       | 4                        | 17,28 ₽               |
| **c1.8 (8 vCPU, 0 GPU)**       | 8                        | 34,56 ₽               |
| **c1.32 (32 vCPU, 0 GPU)**     | 32                       | 138,24 ₽              |
| **c1.80 (80 vCPU, 0 GPU)**     | 80                       | 345,60 ₽              |
| **g1.1 (8 vCPU, 1 GPU V100)**  | 72                       | 311,04 ₽              |
| **g1.2 (16 vCPU, 2 GPU V100)** | 144                      | 622,08 ₽              |
| **g1.4 (32 vCPU, 4 GPU V100)** | 288                      | 1 244,16 ₽            |
| **g2.1 (28 vCPU, 1 GPU A100)** | 116                      | 501,12 ₽              |
| **g2.2 (56 vCPU, 2 GPU A100)** | 232                      | 1 002,24 ₽            |
| **g2.4 (112 vCPU, 4 GPU A100)**| 464                      | 2 004,48 ₽            |
| **g2.8 (224 vCPU, 8 GPU A100)**| 928                      | 4 008,96 ₽            |
| **gt4.1 (4 vCPU, 1 GPU T4)**   | 36                       | 155,52 ₽              |

С полным списком тарифов и более гибким калькулятором можно ознакомиться на [калькуляторе цен Yandex Cloud](https://yandex.cloud/ru/prices).

### Возможности в пределах промокода:
- **DataSphere Jobs**: Удаленный запуск Python-скриптов через командную строку. Инструкция по работе с Jobs [здесь](https://yandex.cloud/ru/docs/datasphere/operations/projects/work-with-jobs).
- Есть озможность подключения по SSH для работы с репозиториями или удалёнными серверами [Подробнее](https://yandex.cloud/ru/docs/datasphere).

### Расчёты:
- Промокод может покрыть работу на разных конфигурациях. за 5к можно использовать:
    - **c1.4** около 289 часов - как будто и не надо
    - **g1.1 (1 GPU V100)** около 16 часов
    - **g2.1 (1 GPU A100)** около 10 часов
---
## Базовые модели с аугментацией и перефразированием

Взяла код Вани и прогнала с аугментацией и перефразированием.

---

### 1. Ванина аугментация + перефразирование

| **Train**                                                                 | **Test**                                                                |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Accuracy: **0.9681**                                                      | Accuracy: **0.8576**                                                    |
| Precision: (macro: **0.9754**, micro: **0.9681**)                         | Precision: (macro: **0.7591**, micro: **0.8576**)                       |
| Recall: (macro: **0.9697**, micro: **0.9681**)                            | Recall: (macro: **0.7625**, micro: **0.8576**)                          |
| F1 Score: (macro: **0.9716**, micro: **0.9681**)                          | F1 Score: (macro: **0.7440**, micro: **0.8576**)                        |

---

### 2. Только перефразирование

| **Train**                                                                 | **Test**                                                                |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Accuracy: **0.9711**                                                      | Accuracy: **0.8245**                                                    |
| Precision: (macro: **0.9805**, micro: **0.9711**)                         | Precision: (macro: **0.6848**, micro: **0.8245**)                       |
| Recall: (macro: **0.9749**, micro: **0.9711**)                            | Recall: (macro: **0.6811**, micro: **0.8245**)                          |
| F1 Score: (macro: **0.9763**, micro: **0.9711**)                          | F1 Score: (macro: **0.6682**, micro: **0.8245**)                        |

---

### 3. Только Ванина аугментация

| **Train**                                                                 | **Test**                                                                |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Accuracy: **0.9714**                                                      | Accuracy: **0.8709**                                                    |
| Precision: (macro: **0.9797**, micro: **0.9714**)                         | Precision: (macro: **0.7605**, micro: **0.8709**)                       |
| Recall: (macro: **0.9736**, micro: **0.9714**)                            | Recall: (macro: **0.7711**, micro: **0.8709**)                          |
| F1 Score: (macro: **0.9758**, micro: **0.9714**)                          | F1 Score: (macro: **0.7488**, micro: **0.8709**)                        |

---
Методы от Вани делают win win

### Back translate
Более жесткий для генерации, пока проверяю
