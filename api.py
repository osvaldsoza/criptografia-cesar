#  from requests_toolbelt import MultipartEncoder
import requests

TOKEN = 'a6fd3a58aeb4aa726dbf7f25f63442db1c97f279'


def get_json_api():
    data = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=' + TOKEN)
    return data.encoding


def post_json_api():
<<<<<<< HEAD
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution'
    querystring = {'token': 'a6fd3a58aeb4aa726dbf7f25f63442db1c97f279'}
    payload = {'Content-Disposition': 'form-data', 'file': 'answer', 'filename': 'answer.json', 'Content-Type': 'application/json'}
    headers = {'Content-Type': 'multipart/form-data;'}
    p = requests.request('POST', url=url, data=payload, headers=headers, params=querystring)
    return p.status_code

=======
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=' + TOKEN
    payload = 'name=\"answer\"; filename=\"answer.json\"\r\nContent-Type: application/json'
    headers = {
    'content-type': 'multipart/form-data;'
    }
    response = requests.request('POST', url, data=payload, headers=headers)
    return response.text
>>>>>>> e39b78c76beb837e43f9515dac6958d3bf6fa87e

if __name__ == '__main__':
    print(post_json_api())
