from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс для работы c API сервиса с вакансиями"""

    @abstractmethod
    def __init__(self):
        pass
