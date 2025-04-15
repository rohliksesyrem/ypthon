import requests

# ZDE vlož svůj webhook URL
webhook_url = 'https://discord.com/api/webhooks/TVUJ_WEBHOOK_URL'

# Zpráva, kterou chceš poslat
message = {
    "content": "Ahoj z Pythonu! 🐍"
}

# Odeslání POST požadavku
response = requests.post(webhook_url, json=message)

# Kontrola odpovědi
if response.status_code == 204:
    print("Zpráva úspěšně odeslána!")
else:
    print(f"Chyba při odesílání: {response.status_code} - {response.text}")
    