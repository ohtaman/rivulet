import json

from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse, JSONResponse

router = APIRouter()

@router.get("/event")
async def event_endpoint():
    events = [
        {"id": 1, "name": "Event 1"},
        {"id": 2, "name": "Event 2"},
        {"id": 3, "name": "Event 3"},
    ]
    return StreamingResponse((f"data: {json.dumps(event, ensure_ascii=False)}\n\n" for event in events), media_type="text/event-stream")
