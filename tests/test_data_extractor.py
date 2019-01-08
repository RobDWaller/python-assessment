import pytest

from data_extractor import DataExtractor

data_extractor = DataExtractor()


class TestDataExtractor:

    def test_find_items(self):
        expected = [
            {
                'name': 'Google',
                'url': 'https://www.google.co.uk',
                'domain': 'google.co.uk',
                'secure': True,
                'value': 5},
            {
                'name': 'Facebook',
                'url': 'https://developers.facebook.com/blog/post/2018/10/02/facebook-login-update/',
                'domain': 'facebook.com',
                'secure': True,
                'value': 4},
            {
                'name': 'YouTube',
                'url': 'https://www.youtube.com/watch?v=09Cd7NKKvDc',
                'domain': 'youtube.com',
                'secure': True,
                'value': 5
            }
        ]
        assert data_extractor.find_items(4) == expected
