from ollama import Client


def test_ollama_connection():
    client = Client(
        host="http://localhost:11434",
        timeout=180,
    )
    print("Sending request to Ollama...", flush=True)

    response = client.chat(
        model="gpt-oss:latest",
        messages=[
            {"role": "user", "content": "Reply with one short sentence: What is an ETL pipeline?",}
        ],
    )

    print("Response from Ollama:")
    print(response.message.content)

if __name__ == "__main__":
    test_ollama_connection()