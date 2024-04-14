import json
from src.handler import Handler


class JSONFileHandler(Handler):
    """Класс для рабы с JSON файлами"""

    def __init__(self, file_path):
        self.file_path = file_path

    def get_vacancies(self):
        """Метод позволяет получать список вакансий из файла json"""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            list_of_vacancies = json.load(file)
            return list_of_vacancies

    def write_vacancies_to_file(self, vacancies):
        """Метод позволяет записывать полученные вакансии с помощью API HH в json файл"""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            data_for_write = []
            for data in vacancies:
                data_for_write.append(data.__dict__)
            json.dump(data_for_write, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy):
        """Метод позволяет добавлять вакансию и ее данные в json файл"""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            data.append(vacancy)
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancies(self, vacancies):
        """Метод позволяет добавлять список вакансий и их данные в json файл"""
        data = self.get_vacancies()
        for vacancy in vacancies:
            data.append(vacancy.__dict__)
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def del_vacancy(self, vacancy):
        """Метод позволяет удалять вакансию из json файла"""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            data.remove(vacancy)
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
