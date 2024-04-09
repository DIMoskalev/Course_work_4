class Vacancy:

    def __init__(self, name, professional_role, experience, employment, schedule, salary_min, salary_max,
                 currency, employer, requirement, responsibility, url):
        self.name = name
        self.professional_role = professional_role
        self.experience = experience
        self.employment = employment
        self.schedule = schedule
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.currency = currency
        self.employer = employer
        self.requirement = requirement
        self.responsibility = responsibility
        self.url = url

    def __str__(self):
        return (f'-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-'
                f'\nВакансия: {self.name}\n'
                f'Должность: {self.professional_role}\n'
                f'Требуемый опыт: {self.experience}\n'
                f'Тип занятости: {self.employment}\n'
                f'График: {self.schedule}\n'
                f'Зарплата: от {self.salary_min} до {self.salary_max} {self.currency}\n'
                f'Работодатель: {self.employer}\n'
                f'Требования: {self.requirement}\n'
                f'Обязанности: {self.responsibility}\n'
                f'Ссылка на вакансию: {self.url}\n'
                f'-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
