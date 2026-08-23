from abc import ABC, abstractmethod


class Working_With_Files(ABC):

    def __init__(self, file, data):
        self.file = file
        self.data = data

    @abstractmethod
    def write_file(self):
        pass

    @abstractmethod
    def write_file_add(self, *args):
        pass

    @abstractmethod
    def get_by_criterion(self, *args):
        pass
