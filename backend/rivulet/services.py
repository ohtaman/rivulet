import json

def generate_initial_dom():
    initial_dom = {
        "tag": "div",
        "children": [
            {"tag": "h1", "content": "Welcome to Rivulet"},
            {"tag": "p", "content": "This is a sample virtual DOM."}
        ]
    }
    return json.dumps(initial_dom)

def update_state(data):
    # 状態更新ロジック
    # 仮想DOMの一部または全体を返す
    updated_dom = {
        "tag": "div",
        "children": [
            {"tag": "h1", "content": "Updated Rivulet"},
            {"tag": "p", "content": f"Updated content: {data.get('content', '')}"}
        ]
    }
    return json.dumps(updated_dom)
