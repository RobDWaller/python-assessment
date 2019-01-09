from data_extractor import DataExtractor
from websites.resources.data import WEBSITES

data_extractor = DataExtractor(WEBSITES)


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
        assert data_extractor.find_items() == expected

    def test_find_items_none_found(self):
        assert data_extractor.find_items(100) == []

    def test_find_items_all_matching(self):
        assert data_extractor.find_items(1) == WEBSITES

    def test_amend_domain_values(self):
        expected = [
            {
                'name': 'Google',
                'url': 'https://www.google.co.uk',
                'domain': 'www.google.co.uk',
                'secure': True,
                'value': 5},
            {
                'name': 'Facebook',
                'url': 'https://developers.facebook.com/blog/post/2018/10/02/facebook-login-update/',
                'domain': 'www.facebook.com',
                'secure': True, 'value': 4},
            {
                'name': 'Bing',
                'url': 'https://www.bing.com/search?q=athlete&qs=n&form=QBLH&sp=-1&pq=athlete&sc=8-7&sk=&cvid=53830DD7FB2E47B7A5D9CF27F106BC9A',
                'domain': 'www.bing.com',
                'secure': False,
                'value': 3
            },
            {
                'name': 'Ask',
                'url': 'https://uk.ask.com/web?o=0&l=dir&qo=serpSearchTopBox&q=jupiter',
                'domain': 'www.ask.com',
                'secure': False,
                'value': 1},
            {
                'name': 'Duck Duck Go',
                'url': 'http://duckduckgo.com/?q=plane&t=h_&ia=web',
                'domain': 'www.duckduckgo.com',
                'secure': True,
                'value': 2
            },
            {
                'name': 'Vimeo',
                'url': 'https://vimeo.com/53812885',
                'domain': 'www.vimeo.com',
                'secure': False,
                'value': 2
            },
            {
                'name': 'YouTube',
                'url': 'https://www.youtube.com/watch?v=09Cd7NKKvDc',
                'domain': 'www.youtube.com',
                'secure': True,
                'value': 5
             },
            {
                'name': 'Daily Motion',
                'url': 'http://www.dailymotion.com/search/football',
                'domain': 'www.dailymotion.com',
                'secure': True,
                'value': 1
            }
        ]
        assert data_extractor.amend_domain_values() == expected

    def test_amend_domain_values_retains_original_if_prefix_matching(self):
        test_data = [
            {
                'name': 'Google',
                'url': 'https://www.google.co.uk',
                'domain': 'www.google.co.uk',
                'secure': True,
                'value': 5
            }
        ]
        _data_extractor = DataExtractor(test_data)
        assert _data_extractor.amend_domain_values() == test_data

    def test_cleanse_data(self):
        test_data = [
            {
                'name': 'Google',
                'url': 'https://www.google.co.uk',
                'domain': 'google.co.uk',
                'secure': False,
                'value': 5
            },
            {
                'name': 'Facebook',
                'url': 'http://developers.facebook.com/blog/post/2018/10/02/facebook-login-update/',
                'domain': 'facebook.com',
                'secure': True,
                'value': 4
            },
            {
                'name': 'Bing',
                'url': 'http://www.bing.com/search?q=athlete&qs=n&form=QBLH&sp=-1&pq=athlete&sc=8-7&sk=&cvid=53830DD7FB2E47B7A5D9CF27F106BC9A',
                'domain': 'bing.com',
                'secure': False,
                'value': 3
            },
            {
                'name': 'Duck Duck Go',
                'url': 'https://duckduckgo.com/?q=plane&t=h_&ia=web',
                'domain': 'duckduckgo.com',
                'secure': True,
                'value': 2
            },
        ]

        expected = [
            {
                'name': 'Google',
                'url': 'https://www.google.co.uk',
                'domain': 'google.co.uk',
                'secure': True,
                'value': 5
            },
            {
                'name': 'Facebook',
                'url': 'http://developers.facebook.com/blog/post/2018/10/02/facebook-login-update/',
                'domain': 'facebook.com',
                'secure': False,
                'value': 4
            },
            {
                'name': 'Bing',
                'url': 'http://www.bing.com/search?q=athlete&qs=n&form=QBLH&sp=-1&pq=athlete&sc=8-7&sk=&cvid=53830DD7FB2E47B7A5D9CF27F106BC9A',
                'domain': 'bing.com',
                'secure': False,
                'value': 3
            },
            {
                'name': 'Duck Duck Go',
                'url': 'https://duckduckgo.com/?q=plane&t=h_&ia=web',
                'domain': 'duckduckgo.com',
                'secure': True,
                'value': 2
            },
        ]
        _data_extractor = DataExtractor(test_data)
        assert _data_extractor.cleanse_data() == expected

    def test_get_value_sum(self):
        assert data_extractor.get_value_sum() == 23

    def test_get_value_sum_empty_data_set(self):
        _data_extractor = DataExtractor([])
        assert _data_extractor.get_value_sum() == 0
