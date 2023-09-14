from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from bit_posts.models import Post

from bit_users.tests.example_users import ensure_user
from bit_users.tests.example_users import USER_1


class TestPostsCase(APITestCase):

    def setUp(self):
        self.user = ensure_user(USER_1)
        self.client.force_authenticate(self.user)
        self.post_1 = Post.objects.create(
            user=self.user,
            title='some title',
            content='some content',
        )

    def test_list(self):
        # setup
        url = reverse('post-list-create')

        # run
        response = self.client.get(url, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create(self):
        # setup
        url = reverse('post-list-create')
        data = {
            'title': 'new title',
            'content': 'new content',
        }

        # run
        response = self.client.post(url, data, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(response.data['id'], self.post_1.pk)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['content'], data['content'])
        self.assertEqual(response.data['user']['id'], self.user.pk)
