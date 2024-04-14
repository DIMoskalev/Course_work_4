from abc import ABC, abstractmethod


class Handler(ABC):
    """Абстрактный класс, который обязывает реализовывать методы для работы с файлами"""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def write_vacancies_to_file(self, vacancies):
        pass

    @abstractmethod
    def add_vacancies(self, vacancies):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def del_vacancy(self, vacancy):
        pass
