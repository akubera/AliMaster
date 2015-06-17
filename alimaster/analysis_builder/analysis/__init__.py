#
# alimaster/analysis_builder/analysis/__init__.py
#

import pickle


class Analysis:
    """
    Base class for the abstract analysis class which can
    """

    def __init__(self, name, author):
        self.name = name
        self.author = author

    def serialize(self):
        """
        Turn the Project object into a string of bytes for writing to disk.
        """
        return pickle.dumps(self)

    @classmethod
    def deserialize(cls, bytes_data):
        """
        Loads an Project class from a bytes object, presumably read from disk.
        """
        return pickle.loads(bytes_data)
