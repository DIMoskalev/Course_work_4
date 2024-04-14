from src.headhunter_api import HeadhunterAPI
from src.vacancy import Vacancy


def get_vacancies(search_query):
    """Функция выполняет фильтрацию списка вакансий по ключевому слову search_query
     и возвращает отфильтрованный список с вакансиями"""
    hh_api = HeadhunterAPI()
    hh_vacancies = hh_api.load_vacancies(search_query)
    vacancies_list = Vacancy.data_conversion(hh_vacancies)
    return vacancies_list


def filter_vacancies(vacancies_list, filter_words):
    """Функция выполняет фильтрацию вакансий по """
    filtered_vacancies = []
    for vacancy in vacancies_list:
        for word in filter_words:
            if word in vacancy.requirement or word in vacancy.responsibility:
                filtered_vacancies.append(vacancy)
    return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """Функция принимает список вакансий список с диапазоном зарплат,
     осуществляет отсеивание по зарплате и возвращает обработанный список вакансий"""
    ranged_vacancies = []
    salary_range_from = int(salary_range[0])
    salary_range_to = int(salary_range[2])
    for vacancy in filtered_vacancies:
        if salary_range_from <= vacancy.salary_from and vacancy.salary_to <= salary_range_to:
            ranged_vacancies.append(vacancy)
    return ranged_vacancies


def sort_vacancies(ranged_vacancies):
    """Функция принимает список с вакансиями
    и выполняет сортировку вакансий по зарплате в порядке убывания"""
    return sorted(ranged_vacancies, reverse=True)


def get_top_vacancies(sorted_vacancies, top_n):
    """Функция принимает список вакансий, а возвращает определенное количество (срез) вакансий,
    запрашиваемых пользователем (top_n)"""
    return sorted_vacancies[:top_n]


def print_vacancies(top_vacancies):
    """Функция выводит все вакансий из полученного списка"""
    for vacancy in top_vacancies:
        print(vacancy)
