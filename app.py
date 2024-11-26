import requests


def get_blague(url):

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        jokes_data = response.json()
        return f"{jokes_data['setup']} - {jokes_data['punchline']}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred {e}"

if __name__ == "__main__":
    print(get_blague("https://official-joke-api.appspot.com/random_joke"))