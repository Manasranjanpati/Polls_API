from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


# class TestPoll(APITestCase):
#     def setUp(self):
#         # ...
#         self.user = self.setup_user()
#         self.token = Token.objects.create(user=self.user)
#         self.token.save()

#     @staticmethod
#     def setup_user():
#         User = get_user_model()
#         return User.objects.create_user(
#             'test',
#             email='testuser@test.com',
#             password='test'
#         )

#     def test_list(self):
#         request = self.factory.get(self.uri,
#                                    HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
#         request.user = self.user
#         response = self.view(request)
#         self.assertEqual(response.status_code, 200,
#                          'Expected Response Code 200, received {0} instead.'
#                          .format(response.status_code))



class TestPoll(APITestCase):
    # ...

    def test_list2(self):
        self.client.login(username="test", password="test")
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))