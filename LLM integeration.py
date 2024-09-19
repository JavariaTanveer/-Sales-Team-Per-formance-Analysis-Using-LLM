import requests

HUGGING_FACE_API_KEY = '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'

def get_llm_insights(prompt: str):
    url = "https://api-inference.huggingface.co/models/gpt2"  # You can use another model if you prefer
    headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}
    response = requests.post(url, headers=headers, json={"inputs": prompt})

    if response.status_code == 200:
        result = response.json()
        return result[0]["generated_text"]
    else:
        return f"Error: {response.status_code} {response.text}"
