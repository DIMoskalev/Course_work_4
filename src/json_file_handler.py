import json
from src.handler import Handler


class JSONFileHandler(Handler):

    def __init__(self, file_path):
        self.file_path = file_path

    def get_vacancies(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            list_of_vacancies = json.load(file)
            return list_of_vacancies

    def write_vacancies_to_file(self, vacancies):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            data_for_write = []
            for data in vacancies:
                data_for_write.append(data.__dict__)
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancies):
        with open(self.file_path, 'a+', encoding='utf-8') as file:
            data = json.load(file)
            for vacancy in vacancies:
                data.append(vacancy.__dict__)
        json.dump(data, file, ensure_ascii=False, indent=4)

    def del_vacancy(self, vacancy):
        with open(self.file_path, 'a+', encoding='utf-8') as file:
            data = json.load(file)
            if vacancy in data:
                data.remove(vacancy)
        json.dump(data, file, ensure_ascii=False, indent=4)
