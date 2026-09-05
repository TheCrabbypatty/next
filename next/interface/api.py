import requests
from django.conf import settings

def get_next_task_from_ai(tasks):
    prompt = (
        "You are a productivity assistant. The user has the following tasks:\n\n"
    )

    for t in tasks:
        prompt += f"- {t.name} ({t.estimated_time} minutes)\n"

    prompt += (
        "\nChoose the best next task based on:\n"
        "- shortest time first\n"
        "- clarity\n"
        "- ease of starting\n"
        "- avoiding overwhelm\n\n"
        "Respond with ONLY the task name."
    )

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3.1:8b",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }
    )

    print("STATUS:", response.status_code)
    print("RAW RESPONSE:", response.text)

    try:
        data = response.json()
        return data["message"]["content"].strip()
    except Exception:
        return "Could not determine the next task."