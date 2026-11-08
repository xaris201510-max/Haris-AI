
import json
import urllib.request
import urllib.error
import os

from getpass import getpass
API_KEY = getpass("Enter your OpenAI API key: ")

def get_response(message):
    if not API_KEY:
        return "API key is not configured yet."

    url = "https://api.openai.com/v1/responses"

    data = {
        "model": "gpt-4.1-mini",
        "input": message
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    request = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers=headers,
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            result = json.loads(response.read().decode("utf-8"))

        for item in result.get("output", []):
            for content in item.get("content", []):
                if content.get("type") == "output_text":
                    return content.get("text", "")

        return "I could not find a response."

    except urllib.error.HTTPError as error:
        return f"API Error: HTTP {error.code}"
    except Exception as error:
        return f"Connection Error: {error}"
