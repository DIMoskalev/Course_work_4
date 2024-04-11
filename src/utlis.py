from src.headhunter_api import HeadhunterAPI
from src.vacancy import Vacancy


def get_vacancies(search_query):
    hh_api = HeadhunterAPI()
    hh_vacancies = hh_api.load_vacancies(search_query)
    vacancies_list = Vacancy.data_conversion(hh_vacancies)
    return vacancies_list


def filter_vacancies(vacancies_list, filter_words):
    filtered_vacancies = []
    for vacancy in vacancies_list:
        for word in filter_words:
            if word in vacancy.requirement or word in vacancy.responsibility:
                filtered_vacancies.append(vacancy)
    return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    ranged_vacancies = []
    salary_range_from = int(salary_range[0])
    salary_range_to = int(salary_range[2])
    for vacancy in filtered_vacancies:
        if salary_range_from <= vacancy.salary_from and vacancy.salary_to <= salary_range_to:
            ranged_vacancies.append(vacancy)
    return ranged_vacancies


def sort_vacancies(ranged_vacancies):
    return sorted(ranged_vacancies, reverse=True)


def get_top_vacancies(sorted_vacancies, top_n):
    return sorted_vacancies[:top_n]


def print_vacancies(top_vacancies):
    for vacancy in top_vacancies:
        print(vacancy)
