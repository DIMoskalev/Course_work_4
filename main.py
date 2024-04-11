from src.utlis import get_vacancies, print_vacancies, filter_vacancies, get_vacancies_by_salary, sort_vacancies, \
    get_top_vacancies


def main():
    print("Добро пожаловать в программу поиска вакансий с сайта hh.ru.")
    while True:
        start_input = input('Чтобы начать работу программы нажмите Enter и следуйте инструкциям.\n')
        if start_input == '':
            search_query = input('Введите ключевое слово для поиска вакансий:\n')
            top_n = int(input('Введите количество вакансий для вывода в топ N: '))
            filter_words = input("Введите ключевые слова для фильтрации вакансий через пробел: ").split()

            while True:
                salary_range = input("Введите диапазон зарплат в формате '50000 - 60000':\n").split()
                if len(salary_range) == 3:
                    break

            vacancies_list = get_vacancies(search_query)

            filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

            ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

            sorted_vacancies = sort_vacancies(ranged_vacancies)

            top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
            print_vacancies(top_vacancies)

            break


if __name__ == '__main__':
    main()
