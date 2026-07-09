from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory


class SessionService:

    def __init__(self):
        self.vector_stores = {}
        self.chat_histories = {}

    def add_vector_store(
        self,
        session_id,
        vector_store,
    ):
        self.vector_stores[session_id] = vector_store

    def get_vector_store(
        self,
        session_id,
    ):
        return self.vector_stores.get(session_id)

    def get_chat_history(
        self,
        session_id,
    ) -> BaseChatMessageHistory:

        if session_id not in self.chat_histories:
            self.chat_histories[
                session_id
            ] = ChatMessageHistory()

        return self.chat_histories[
            session_id
        ]

    def delete_session(
        self,
        session_id,
    ):
        self.vector_stores.pop(
            session_id,
            None,
        )

        self.chat_histories.pop(
            session_id,
            None,
        )


session_service = SessionService()