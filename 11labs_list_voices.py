import requests

API_KEY = "YOUR_API_KEY"

# получить все голоса

# resp = requests.get(
#   "https://api.elevenlabs.io/v1/voices",
#   headers={"xi-api-key": API_KEY, "Accept":"application/json"}
# )
# voices = resp.json()["voices"]
# for v in voices:
#     print(v["voice_id"], "→", v["name"])

# получить имя конкретного голоса

voice_id = "your_voice_id"
url = f"https://api.elevenlabs.io/v1/voices/{voice_id}"

headers = {
    "xi-api-key": API_KEY,
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(f"Voice name: {data['name']}")
else:
    print(f"Ошибка: {response.status_code} — {response.text}")
