import json

from django.shortcuts import reverse

from aop.test import BaseTestCase


class GreetViewTestCase(BaseTestCase):

    def test_success(self):
        resp = self.json_post(reverse('example_greet'), dict(id=1))
        self.assertEqual(resp.status_code, 200)
        content = json.loads(resp.content)
        self.assertEqual(content['ret_code'], 0)
        self.assertEqual(content['message'], 'success')
        self.assertEqual(content['data']['hello'], 'world')

    def test_invalid_input(self):
        resp = self.json_post(reverse('example_greet'))
        self.assertEqual(resp.status_code, 200)
        content = json.loads(resp.content)
        self.assertEqual(content['ret_code'], 1)
