from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_community.embeddings import FakeEmbeddings

global_store = {}


def _get_embeddings(embed_name='',
                   is_embed_fake=False):
    if is_embed_fake:
        return FakeEmbeddings(size=300)
    return OllamaEmbeddings(model=embed_name)


def _get_llm(llm_name: str, temperature=0.1):
    return ChatOllama(model=llm_name, temperature=temperature)


def _get_loader(file_path: str):
    return CSVLoader(
        file_path=file_path,
        metadata_columns=['id', 'category'],
        content_columns=['question', 'content'],
        encoding='utf-8',
    )


def _get_chat_prompt(prompt: str):
    return ChatPromptTemplate.from_messages(
        [
            ('system', prompt),
            MessagesPlaceholder('chat_history'),
            ('human', '{input}'),
        ]
    )


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in global_store:
        global_store[session_id] = ChatMessageHistory()
    return global_store[session_id]


def get_rag_chain(
        model_name: str,
        temperature: float,
        embed_name: str,
        file_path: str,
        search_type: str,
        num_answers: int,
        lambda_mult: float,
        contextualize_q_system_prompt: str,
        system_prompt: str,
        is_embed_fake=False,
) -> RunnableWithMessageHistory:
    loader_train = _get_loader(file_path)
    embeddings = _get_embeddings(embed_name, is_embed_fake=is_embed_fake)
    print('до llm')
    llm = _get_llm(model_name, temperature=temperature)
    print('после llm')
    vectorstore = Chroma.from_documents(
        collection_name='question_answer_collection',
        documents=loader_train.load(),
        embedding=embeddings,
    )
    retriever = vectorstore.as_retriever(
        search_type=search_type,
        search_kwargs={'num_answers': num_answers, 'lambda_mult': lambda_mult},
    )

    contextualize_q_prompt = _get_chat_prompt(contextualize_q_system_prompt)
    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_q_prompt
    )

    qa_prompt = _get_chat_prompt(system_prompt)
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
    return RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key='input',
        history_messages_key='chat_history',
        output_messages_key='answer',
    )


