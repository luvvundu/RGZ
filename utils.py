import requests


async def get_currency_rate(currency: str) -> float | None:
    response = requests.get(f"http://195.58.54.159:8000/rate?currency={currency}")
    if response.status_code == 200:
        data = response.json()
        return data["rate"]
    else:
        return None
