from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

from langchain_classic.chains import (
    create_history_aware_retriever,
    create_retrieval_chain,
)
from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain,
)

from backend.core.config import llm
from backend.services.session_service import session_service


def get_conversational_rag_chain(session_id: str):

    vector_store = session_service.get_vector_store(session_id)

    if vector_store is None:
        raise ValueError("Invalid session ID.")

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 4,
        },
    )

    contextualize_system_prompt = (
        "Given the chat history and latest user question, "
        "rewrite the question so it is standalone. "
        "Do not answer the question."
    )

    contextualize_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                contextualize_system_prompt,
            ),
            MessagesPlaceholder(
                "chat_history",
            ),
            (
                "human",
                "{input}",
            ),
        ]
    )

    history_aware_retriever = create_history_aware_retriever(
        llm,
        retriever,
        contextualize_prompt,
    )

    system_prompt = """
You are MediBridge, an AI medical assistant.

Rules:
- Answer only from the uploaded medical report whenever possible.
- If the answer is not present in the report, clearly say you don't know.
- Do not invent medical information.
- If the user greets you, greet them politely.
- If the user asks for a summary, summarize the report.

Context:
{context}
"""

    qa_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                system_prompt,
            ),
            MessagesPlaceholder(
                "chat_history",
            ),
            (
                "human",
                "{input}",
            ),
        ]
    )

    qa_chain = create_stuff_documents_chain(
        llm,
        qa_prompt,
    )

    rag_chain = create_retrieval_chain(
        history_aware_retriever,
        qa_chain,
    )

    conversational_chain = RunnableWithMessageHistory(
        rag_chain,
        session_service.get_chat_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer",
    )

    return conversational_chain


def chat(
    session_id: str,
    question: str,
):

    chain = get_conversational_rag_chain(
        session_id,
    )

    response = chain.invoke(
        {
            "input": question,
        },
        config={
            "configurable": {
                "session_id": session_id,
            }
        },
    )

    return response["answer"]