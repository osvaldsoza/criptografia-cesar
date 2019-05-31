import requests

TOKEN = 'a6fd3a58aeb4aa726dbf7f25f63442db1c97f279'


def get_json_api():
    data = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=' + TOKEN)
    return data.encoding


def post_json_api():
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=' + TOKEN
    payload = {'Content-Disposition': 'form-data', 'file': 'answer', 'filename': 'answer.json',
               'Content-Type': 'application/json'}
    headers = {'content-Type': 'multipart/form-data'}
    p = requests.post(url, data=payload, headers=headers)
    return p.text


if __name__ == '__main__':
    print(post_json_api())
