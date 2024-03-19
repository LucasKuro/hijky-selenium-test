import random
import pytest
import requests


class TestGetToken:
    def test_get_apikey(self):
        response = requests.get('https://secrets-api.appbrewery.com/generate-api-key')
        result = response.json()
        new_apikey = result['apiKey']
        return new_apikey

    def test_get_filter(self):
        response = requests.get(
            'https://secrets-api.appbrewery.com/filter?',
            params={
                'score': 5,
                'apiKey': self.test_get_apikey()
            })
        result = response.json()
        print(result)
        assert result[0]['username'] == 'secretsnacker'

    def test_create_user(self):
        x = random.randint(0, 100)
        name = 'kevinttest' + str(x)
        response = requests.post(
            'https://secrets-api.appbrewery.com/register',
            data={
                'username': f'{name}',
                'password': 'liferay123'
            })
        result = response.json()
        print(result)
        assert result['success'] == 'Successfully registered.'
        return name

    def test_get_auth_token(self):
        response = requests.post(
            'https://secrets-api.appbrewery.com/get-auth-token',
            data={
                'username': self.test_create_user(),
                'password': 'liferay123'
            })
        result = response.json()
        new_auth_token = result['token']
        return new_auth_token


if __name__ == '__main__':
    pytest.main(['-vs', 'test02.py'])
