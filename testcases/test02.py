import unittest
import pytest
import requests


class TestGithub(unittest.TestCase):
    token = "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"
    userName = 'LucasKuro'

    @pytest.fixture(scope="function", autouse=True)
    def driver(self):
        print("开始测试")
        yield
        print("结束测试")

    def test_get_user_name(self):
        response = requests.get('https://api.github.com/user', headers={'Authorization': 'Bearer ' + self.token})
        result = response.json()
        assert response.status_code == 200
        assert result['login'] == 'hijkyTester'

    def test_get_user_repos(self):
        response = requests.get('https://api.github.com/users/Lucaskuro/repos', headers={'Authorization': 'Bearer ' +
                                                                                                          self.token})
        result = response.json()
        assert result[0]['name'] == 'hijky-playwright-test'
        assert result[1]['name'] == 'hijky-selenium-test'
        assert result[2]['name'] == 'LucasKuro'


if __name__ == '__main__':
    pytest.main(['-sv', 'test01.py'])
