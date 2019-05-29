#  from requests_toolbelt import MultipartEncoder
import requests

TOKEN = 'a6fd3a58aeb4aa726dbf7f25f63442db1c97f279'


def get_json_api():
    data = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=' + TOKEN)
    return data.encoding


def post_json_api():
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=a6fd3a58aeb4aa726dbf7f25f63442db1c97f279'
    payload = {'file': 'answer', 'filename': 'answer.json'}
    headers = {'Content-Type': 'multipart/form-data', 'Accept': 'application/json'}
    p = requests.request('POST', url=url, data=payload, headers=headers)
    return p.history


if __name__ == '__main__':
    print(post_json_api())
