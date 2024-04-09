from src.headhunter_api import HeadhunterAPI
from src.vacancy import Vacancy


def main():
    search_query = input('Нажмите Enter для запуска программы\n')
    hh_api = HeadhunterAPI()
    hh_vacancies = hh_api.load_vacancies(search_query)
    vacancies_list = Vacancy.data_conversion(hh_vacancies)
    for vacancies in vacancies_list:
        print(vacancies)


if __name__ == '__main__':
    main()
