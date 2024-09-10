config = {
    'model_name': 'llama3.1:8b',
    'temperature': 0.1,
    'embed_name': 'nomic-embed-text:v1.5',
    'file_path': 'real_data_train.csv',
    'search_type': 'mmr',
    'num_answers': 5,
    'lambda_mult': 0.25,
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
    'is_embed_fake': True
}
