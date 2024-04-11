class Vacancy:

    def __init__(self, name, professional_roles, experience, employment, schedule,
                 employer, salary_from, salary_to, currency, requirement, responsibility, url, salary=None):
        self.name = name
        self.professional_roles = professional_roles
        self.experience = experience
        self.employment = employment
        self.schedule = schedule
        self.salary = salary
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.employer = employer
        self.requirement = requirement
        self.responsibility = responsibility
        self.url = url

    @classmethod
    def data_conversion(cls, vacancies_data):
        emp_list = []
        for vacancy in vacancies_data:
            name = vacancy['name']
            professional_roles = vacancy['professional_roles'][0]['name']
            experience = vacancy.get('experience').get('name')
            employment = vacancy['employment']['name']
            schedule = vacancy['schedule']['name']
            if vacancy['salary'] is None:
                salary = None
                salary_from = 0
                salary_to = 0
                currency = None
            else:
                salary = vacancy['salary']
                salary_from = vacancy['salary']['from']
                salary_to = vacancy['salary']['to']
                currency = vacancy['salary']['currency']
            employer = vacancy['employer']['name']
            requirement = vacancy['snippet']['requirement']
            responsibility = vacancy['snippet']['responsibility']
            url = vacancy['alternate_url']
            object_vac = cls(name, professional_roles, experience, employment, schedule,
                             employer, salary_from, salary_to, currency, requirement,
                             responsibility, url, salary)
            emp_list.append(object_vac)
        return emp_list

    def get_salary(self):
        if self.salary:
            if self.salary_to is None:
                return f'Зарплата: от {self.salary_from}'
            elif self.salary_from is None:
                return f'Зарплата: до {self.salary_to}'
            elif self.salary_from == self.salary_to:
                return f'Зарплата: {self.salary_to}'
            elif self.salary_from and self.salary_to:
                return f'Зарплата: от {self.salary_from} до {self.salary_to}'
        else:
            return f'Зарплата: Не указана'

    def get_currency(self):
        if self.salary:
            if self.currency == "RUR":
                return "руб."
            elif self.currency == "KZT":
                return "тенге"
            elif self.currency == "BYR":
                return "белорус. руб"
            elif self.currency == "UZS":
                return "узбек. сум"
            elif self.currency == "USD":
                return "долл."
            elif self.currency == "EUR":
                return "евро"
            elif self.currency is None:
                return "попугаев"
            else:
                return f'Неизвестная валюта {self.currency}'
        else:
            return ""

    def get_requirement(self):
        if self.requirement:
            return self.requirement.replace('<highlighttext>', '').replace('</highlighttext>', '')
        else:
            return f'Данные не указаны'

    def get_responsibility(self):
        if self.responsibility:
            return self.responsibility.replace('<highlighttext>', '').replace('</highlighttext>', '')
        else:
            return f'Данные не указаны'

    def __gt__(self, other):
        if isinstance(other, (Vacancy, int)):
            raise TypeError("Значение справа должно иметь тип int или принадлежать классу Vacancy")
        if type(other) is type(self):
            return self.salary_from > other.salary_from
        return self.salary_from > other

    def __str__(self):
        return (f'-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-'
                f'\nВакансия: {self.name}\n'
                f'Должность: {self.professional_roles}\n'
                f'Требуемый опыт: {self.experience}\n'
                f'Тип занятости: {self.employment}\n'
                f'График: {self.schedule}\n'
                f'{self.get_salary()} {self.get_currency()}\n'
                f'Работодатель: {self.employer}\n'
                f'Требования: {self.get_requirement()}\n'
                f'Обязанности: {self.get_responsibility()}\n'
                f'Ссылка на вакансию: {self.url}\n'
                f'-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
