class DataExtractor:
    """
    Use to extract, cleanse, sum and amend incorrect website data collection.
    """
    def __init__(self, data):
        self.data = data

    def find_items(self, value=4):
        """
        Find and return a new list of items where key "value" is greater than or equal to parameter value.
        :param value: int, value to find items for.
        :return: list(dict), list of dictionaries matching the above filtering rule.
        """
        return [item for item in self.data if item.get('value') and item.get('value') >= value]

    def amend_domain_values(self, prefix='www.'):
        """
        Fixes missing parts of the domain names. By default we add missing 'www.'.
        :param prefix: str, prefix to add to the domain name.
        :return: amended: list(dict), amended list of web records.
        """
        amended = []
        for item in self.data:
            if item.get('domain') and not item.get('domain').startswith(prefix):
                item['domain'] = f"{prefix}{item['domain']}"
            amended.append(item)
        return amended

    def cleanse_data(self):
        """
        Fix errors in "secure" key values. All urls starting with https should be set to "secure": True, those starting
        with http "secure": False.
        :return: amended: list(dict), amended list of web records.
        """
        amended = []
        for item in self.data:
            url = item.get('url')
            secure = item.get('secure')
            if url:
                # https marked as secure = False
                if url.startswith('https:') and not secure:
                    item['secure'] = True
                # http marked as secure = True
                elif url.startswith('http:') and secure:
                    item['secure'] = False
            amended.append(item)
        return amended

    def get_value_sum(self):
        """
        Returns sum of all value keys in the data set.
        :return: int, sum of all value keys in the data set.
        """
        return sum([item.get('value', 0) for item in self.data])
