import asyncio
from collections import defaultdict
import json

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter()

component_state = defaultdict(dict) # global state

def generate_virtual_dom():
    return [
        {"tag": "div", "id": component_id, "states": states}
        for component_id, states in component_state.items()
    ]


@router.get("/components")
async def get_components():
    return JSONResponse(content=generate_virtual_dom())


@router.post("/components/{component_id}/states/{state_name}")
async def update_component_state(component_id: str, state_name: str, request: Request):
    state = await request.json()
    component_state[component_id][state_name] = state
    return JSONResponse(content=generate_virtual_dom())