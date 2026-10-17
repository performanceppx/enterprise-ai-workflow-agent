import json
from pathlib import Path

def recommend(request):
    text = request.get("message", "").lower()
    category = "billing" if "invoice" in text else "general"
    return {"request_id": request["id"], "category": category,
            "recommended_action": "human_review", "write_executed": False}

if __name__ == "__main__":
    examples = json.loads((Path(__file__).parent / "data" / "requests.json").read_text())
    print(json.dumps([recommend(item) for item in examples], indent=2))
