from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    session_id: str = Field(default="default_session", min_length=1)
    pertanyaan: str = Field(min_length=1)


class ChatResponse(BaseModel):
    jawaban: str
