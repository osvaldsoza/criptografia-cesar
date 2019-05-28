import requests

MY_TOKEN = 'a6fd3a58aeb4aa726dbf7f25f63442db1c97f279'


def get_json_api():
    data = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=' + MY_TOKEN)
    return data.json()


if __name__ == '__main__':
    print(get_json_api())
