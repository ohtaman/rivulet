from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from rivulet.services import generate_initial_dom, update_state

router = APIRouter()

@router.get("/rivulet")
async def get_virtual_dom(request: Request):
    initial_dom = generate_initial_dom()
    return StreamingResponse(content=iter([initial_dom]), media_type="application/json")

@router.post("/rivulet/state")
async def update_virtual_dom_state(request: Request):
    data = await request.json()
    updated_dom = update_state(data)
    return StreamingResponse(content=iter([updated_dom]), media_type="application/json")
