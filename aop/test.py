from django.test import TestCase

from django.http import HttpResponse

from .constants import JSON_CONTENT_TYPE


class BaseTestCase(TestCase):

    def json_post(self, path, data=None, **extra) -> HttpResponse:
        return self.client.post(path, data, content_type=JSON_CONTENT_TYPE, **extra)
