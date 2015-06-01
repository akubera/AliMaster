#
# alimaster/analysis_builder/project.py
#

import pickle


class Project:
    """
    Core project class which handles the different 'Models' for use.
    """

    def __init__(self, name, author):
        """
        Construct a new project.
        """
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
