from fastapi import APIRouter, HTTPException

from backend.models.schemas import (
    ChatRequest,
    ChatResponse,
)

from backend.services.rag_service import (
    chat as rag_chat,
)

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse,
)
async def chat(
    request: ChatRequest,
):

    try:

        answer = rag_chat(
            session_id=request.session_id,
            question=request.question,
        )

        return ChatResponse(
            answer=answer,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )