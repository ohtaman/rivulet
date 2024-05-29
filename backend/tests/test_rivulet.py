from fastapi.testclient import TestClient
from rivulet import app  # Adjust the import to your actual app module

client = TestClient(app)

def test_get_components():
    response = client.get("/components")
    assert response.status_code == 200
    assert response.json() == []

def test_update_component_state():
    component_id = "component1"
    state_name = "state1"
    new_state = {"content": "updated content"}

    # Update the state
    response = client.post(f"/components/{component_id}/states/{state_name}", json=new_state)
    assert response.status_code == 200

    # Check if the state was updated correctly
    updated_virtual_dom = response.json()
    assert any(
        comp["id"] == component_id and comp["states"].get(state_name) == new_state
        for comp in updated_virtual_dom
    )

    # Verify the updated state via the GET endpoint
    response = client.get("/components")
    assert response.status_code == 200
    components = response.json()
    assert any(
        comp["id"] == component_id and comp["states"].get(state_name) == new_state
        for comp in components
    )
