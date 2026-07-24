from fastapi import FastAPI, HTTPException

import service
from schemas import ChatRequest, ChatResponse

app = FastAPI(title="Chatbot LLM", version="1.0.0")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/ingest")
async def ingest():
    try:
        return service.ingest_data()
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Ingest gagal: {exc}") from exc


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        jawaban = service.proses_chat(request.session_id, request.pertanyaan)
        return ChatResponse(jawaban=jawaban)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Chat gagal: {exc}") from exc
