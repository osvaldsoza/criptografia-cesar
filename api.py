#  from requests_toolbelt import MultipartEncoder
import requests

MY_TOKEN = 'a6fd3a58aeb4aa726dbf7f25f63442db1c97f279'


def get_json_api():
    data = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=' + MY_TOKEN)
    return data.encoding


def post_json_api():
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=' + MY_TOKEN
    data = {'file': ('answer', open('answer.json', 'rb'))}
    p = requests.post(url=url, data=data)
    return p.text


if __name__ == '__main__':
    print(post_json_api())
