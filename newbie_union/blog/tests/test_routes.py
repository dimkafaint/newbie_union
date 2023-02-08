from django.test import TestCase
from django.urls import reverse


class TestRoutes(TestCase):
    def test_routes_uses_correct_url(self):
        SLUG, USERNAME, ID = 'slug', 'User', 1
        cases = [
            ['index', None, '/'],
            ['group_list', [SLUG], f'/group/{SLUG}/'],
            ['profile', [USERNAME], f'/profile/{USERNAME}/'],
            ['post_create', None, '/create/'],
            ['post_detail', [ID], f'/blog/{ID}/'],
            ['post_edit', [ID], f'/blog/{ID}/edit/'],
            ['follow_index', None, '/follow/'],
            ['profile_follow', [USERNAME], f'/profile/{USERNAME}/follow/'],
            ['profile_unfollow', [USERNAME], f'/profile/{USERNAME}/unfollow/']
        ]
        for name, keys, url in cases:
            with self.subTest(url=url):
                self.assertEqual(reverse(f'blog:{name}', args=keys), url)
