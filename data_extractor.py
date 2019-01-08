from websites.resources.data import WEBSITES


class DataExtractor:
    """
    Use to extract, cleanse and amend incorrect website data collection.
    """
    def __init__(self):
        self.data = WEBSITES

    def find_items(self, value):
        """
        Find and return a new list of items where key "value" is greater than or equal to parameter value.
        :return: list(dict), list of dictionaries matching the above filtering rule.
        """
        return [item for item in self.data if item.get('value') and item.get('value') >= value]


# data_extractor = DataExtractor()
# print(data_extractor.find_items(4))
# print(len(data_extractor.find_items(4)))
