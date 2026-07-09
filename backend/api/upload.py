import os
import uuid

from fastapi import APIRouter, File, HTTPException, UploadFile

from backend.models.schemas import UploadResponse
from backend.services.session_service import session_service

from data_ingestion import (
    load_documents,
    chunker,
)
from embeddings import create_vector_store

router = APIRouter()


@router.post(
    "/upload",
    response_model=UploadResponse,
)
async def upload_pdf(
    file: UploadFile = File(...),
):

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed.",
        )

    session_id = str(uuid.uuid4())

    os.makedirs(
        "temp",
        exist_ok=True,
    )

    temp_path = os.path.join(
        "temp",
        f"{session_id}.pdf",
    )

    try:

        with open(
            temp_path,
            "wb",
        ) as f:
            f.write(await file.read())

        documents = load_documents(
            temp_path,
        )

        chunks = chunker(
            documents,
        )

        vector_store = create_vector_store(
            chunks,
        )

        session_service.add_vector_store(
            session_id,
            vector_store,
        )

        return UploadResponse(
            session_id=session_id,
            message="Medical report processed successfully.",
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)