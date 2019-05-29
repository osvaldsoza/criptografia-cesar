#  from requests_toolbelt import MultipartEncoder
import requests

MY_TOKEN = 'a6fd3a58aeb4aa726dbf7f25f63442db1c97f279'


def get_json_api():
    data = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=' + MY_TOKEN)
    return data.encoding


def post_json_api():
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution'
    querystring = {'token': 'a6fd3a58aeb4aa726dbf7f25f63442db1c97f279'}
    payload = {'Content-Disposition': 'form-data', 'file': 'answer', 'filename': 'answer.json', 'Content-Type': 'application/json'}
    headers = {'Content-Type': 'multipart/form-data;'}
    p = requests.request('POST', url=url, data=payload, headers=headers, params=querystring)
    return p.status_code


if __name__ == '__main__':
    print(post_json_api())
