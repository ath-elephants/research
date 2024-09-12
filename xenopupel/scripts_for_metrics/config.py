config = {
    # Путь до трейна
    'file_path': 'train_synthetic_no_aug.csv',

    # Модель
    'model_name': 'llama3.1:8b',
    'temperature': 0.05,

    # Эмбеддинги
    # 'embed_name': 'nomic-embed-text:v1.5',
    # 'embed_name': 'sergeyzh/rubert-tiny-turbo',
    # 'embed_name': 'Alibaba-NLP/gte-base-en-v1.5',
    # 'embed_name': 'deepvk/USER-base',
    'embed_name': 'ai-forever/ru-en-RoSBERTa',
    'is_embed_fake': False,

    # Параметры ретривера
    'search_type': 'mmr',
    'k': 5,
    'lambda_mult': 0.25,
    'score_threshold': 0.6,  # для search_type == similarity_score_threshold

    # Сохранять вектора эмбеддингов?
    'is_persist_dir' : True,
    'persist_dir_path' : './vectorestore/',

    # Промпты
    'contextualize_q_system_prompt': """
        Given a chat history and the latest user question
        which might reference context in the chat history,
        formulate a standalone question which can be understood
        without the chat history. Do NOT answer the question,
        just reformulate it if needed and otherwise return it as is.
    """,
    'system_prompt': """
        You are an internal technical support assistant for employees of a large company.

        1. Use the entire conversation history with the user to understand the context of the inquiry.
        2. Incorporate the pieces of information retrieved from the knowledge base,
                which consists of pairs of questions (user inquiries) and fixed answers (responses).
        3. Based on the current conversation, choose the most relevant question
                from the retrieved pairs, and respond with the corresponding fixed answer from the knowledge base.
        4. You must provide responses exactly as they appear in the knowledge base,
                without any modifications. All responses must be in Russian.
    \n\n{context}
    """,
}
