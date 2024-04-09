import json

from src.saver import Saver


class JSONSaver(Saver):

    def __init__(self, file_path):
        self.file_path = file_path

    def add_vacancy(self, vacancies):
        pass

    def del_vacancy(self, vacancies):
        pass
