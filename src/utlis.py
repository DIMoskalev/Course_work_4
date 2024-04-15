import os.path

from config import ROOT_DIR
from src.headhunter_api import HeadhunterAPI
from src.json_file_handler import JSONFileHandler
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


def work_with_vacancies_from_api():
    """Функция позволяет пользователю получать данные по вакансиям
    с сайта hh.ru с помощью api."""
    print('Добро пожаловать в программу поиска вакансий с сайта hh.ru!\n'
          'Данная часть программы позволяет работать с api hh.ru\n'
          'Функции программы представлены ниже.\n')
    user_input = 0

    while user_input not in ['back', 'назад']:
        user_input = input('Выберите, какую команду хотите выполнить:\n'
                           '1 - Запрос по ключевому слову - обязательная стартовая операция!\n'
                           '2 - Выполнить фильтрацию по ключевым словам\n'
                           '3 - Отфильтровать вакансии по диапазону зарплат\n'
                           '4 - Отсортировать вакансии в порядке убывания минимальной зарплаты\n'
                           '5 - Оставить топ N вакансий от начала списка\n'
                           '6 - Вывести информацию о вакансиях\n'
                           '7 - Сохранить текущие вакансии в json-файл\n')
        if user_input in ['1', '2', '3', '4', '5', '6', '7']:
            if user_input == '1':
                search_query = input('Введите ключевое слово для поиска вакансий:\n')
                vacancies_list = get_vacancies(search_query)
                print(f'Запрос по ключевому слову выполнен, список с вакансиями создан\n'
                      f'Вакансий в списке: {len(vacancies_list)} шт.')
            try:
                bool(vacancies_list)
            except UnboundLocalError:
                print('Для работы с вакансиями необходимо выполнить запрос по ключевому слову!')
                continue
            if user_input == '2':
                filter_words = input("Введите ключевые слова для фильтрации вакансий через пробел: ").split()
                vacancies_list = filter_vacancies(vacancies_list, filter_words)
                print(f'Выполнена фильтрация вакансий по ключевым словам\n'
                      f'Вакансий в списке: {len(vacancies_list)} шт.\n')
            if user_input == '3':
                while True:
                    salary_range = input("Введите диапазон зарплат в формате '50000 - 60000':\n").split()
                    if len(salary_range) == 3:
                        break
                vacancies_list = get_vacancies_by_salary(vacancies_list, salary_range)
                print(f'Зарплаты отфильтрованы по указанному диапазону зарплат\n'
                      f'Вакансий в списке: {len(vacancies_list)} шт.\n')
            if user_input == '4':
                vacancies_list = sort_vacancies(vacancies_list)
                print(f'Вакансии отсортированы в порядке убывания минимальной зарплаты\n'
                      f'Вакансий в списке: {len(vacancies_list)} шт.\n')
            if user_input == '5':
                top_n = int(input('Введите количество вакансий для вывода в топ N: '))
                vacancies_list = get_top_vacancies(vacancies_list, top_n)
                print(f'Вакансий в списке: {len(vacancies_list)}\n')
            if user_input == '6':
                print_vacancies(vacancies_list)
                print(f'Выведено вакансий: {len(vacancies_list)}')
            if user_input == '7':
                file_name = input('Введите имя файла: \n')
                file_path = os.path.join(ROOT_DIR, 'data', file_name + '.json')
                json_file_handler = JSONFileHandler(file_path)
                if not os.path.exists(file_path):
                    json_file_handler.write_vacancies_to_file(vacancies_list)
                    print('Вакансии сохранены в json-файл\n')
                    break
                else:
                    print(f'Файл с таким именем уже существует.')
                    user_confirm = input(f'Хотите выполнить операции с этим файлом?\n'
                                         f'Введите "Да" или "Нет"\n').lower().strip()
                    if user_confirm == 'нет':
                        continue
                    elif user_confirm == 'да':
                        user_confirm = input('Выберите, что вы хотите сделать с текущим файлом:\n'
                                             '1 - Добавить вакансии в конец текущего файла\n'
                                             '2 - Стереть прошлые данные и записать только текущие вакансии\n')
                        if user_confirm == '1':
                            json_file_handler.add_vacancies(vacancies_list)
                            print(f'Текущие вакансии добавлены в конец файла {file_name}')
                            quit()
                        elif user_confirm == '2':
                            json_file_handler.write_vacancies_to_file(vacancies_list)
                            print(f'Прошлые вакансии удалены из файла, текущие вакансии сохранены в файл {file_name}')
                            quit()
                        else:
                            print('Повторите попытку операции сохранения в файл')
            if user_input in ['stop', 'стоп']:
                quit()
        if user_input in ['stop', 'стоп']:
            quit()
        else:
            print('Введите порядковый номер операции, которую хотите выполнить')


def work_with_vacancies_from_json():
    """Функция позволяет пользователю работать с вакансиями
    из json-файла"""
    print("Добро пожаловать в программу работы с вакансиями из "
          "созданного в программе по работе с api hh.ru json-файла!\n")
    user_input = 0
    while user_input not in ['back', 'назад']:
        user_input = input('Выберите, какую команду хотите выполнить:\n'
                           '1 - Получить вакансии из файла - обязательная стартовая операция!\n'
                           '2 - Выполнить фильтрацию по ключевым словам\n'
                           '3 - Отфильтровать вакансии по диапазону зарплат\n'
                           '4 - Отсортировать вакансии в порядке убывания минимальной зарплаты\n'
                           '5 - Оставить топ N вакансий от начала списка\n'
                           '6 - Вывести информацию о вакансиях\n'
                           '7 - Сохранить текущие вакансии в текущий/новый json-файл\n'
                           '8 - Удалить текущие вакансии из исходного json-файла, если они повторяются '
                           '(альфа-версия функции, может работать некорректно).\n')
        if user_input in ['1', '2', '3', '4', '5', '6', '7', '8']:
            if user_input == '1':
                file_name = input('Введите имя файла: \n')
                file_path = os.path.join(ROOT_DIR, 'data', file_name + '.json')
                if not os.path.exists(file_path):
                    print('json-файла с таким именем не существует.\n')
                else:
                    json_file_handler = JSONFileHandler(file_path)
                    vacancies_from_file = json_file_handler.get_vacancies()
                    vacancies_list = Vacancy.get_objects_for_data_conversion(vacancies_from_file)
                    print(f'Вакансии получены из json-файла в виде списка.\n'
                          f'Вакансий в списке: {len(vacancies_list)} шт.\n')
                    continue
            try:
                bool(vacancies_list)
            except UnboundLocalError:
                print('Для работы с вакансиями необходимо выгрузить их из json-файла!\n')
                continue
            if user_input == '2':
                filter_words = input("Введите ключевые слова для фильтрации вакансий через пробел: ").split()
                vacancies_list = filter_vacancies(vacancies_list, filter_words)
                print(f'Выполнена фильтрация вакансий по ключевым словам\n'
                      f'Вакансий в списке: {len(vacancies_list)} шт.\n')
            if user_input == '3':
                while True:
                    salary_range = input("Введите диапазон зарплат в формате '50000 - 60000':\n").split()
                    if len(salary_range) == 3:
                        break
                vacancies_list = get_vacancies_by_salary(vacancies_list, salary_range)
                print(f'Зарплаты отфильтрованы по указанному диапазону зарплат\n'
                      f'Вакансий в списке: {len(vacancies_list)} шт.\n')
            if user_input == '4':
                vacancies_list = sort_vacancies(vacancies_list)
                print(f'Вакансии отсортированы в порядке убывания минимальной зарплаты\n'
                      f'Вакансий в списке: {len(vacancies_list)} шт.\n')
            if user_input == '5':
                top_n = int(input('Введите количество вакансий для вывода в топ N: '))
                vacancies_list = get_top_vacancies(vacancies_list, top_n)
                print(f'Вакансий в списке: {len(vacancies_list)}\n')
            if user_input == '6':
                print_vacancies(vacancies_list)
                print(f'Выведено вакансий: {len(vacancies_list)}')
            if user_input == '7':
                file_name = input('Введите имя файла: \n')
                file_path = os.path.join(ROOT_DIR, 'data', file_name + '.json')
                json_file_handler = JSONFileHandler(file_path)
                if not os.path.exists(file_path):
                    json_file_handler.write_vacancies_to_file(vacancies_list)
                    print(f'Вакансии сохранены в json-файл {file_name}.\n')
                    break
                else:
                    print(f'Файл с таким именем уже существует.')
                    user_confirm = input(f'Хотите выполнить операции с этим файлом?\n'
                                         f'Введите "Да" или "Нет"\n').lower().strip()
                    if user_confirm == 'нет':
                        continue
                    elif user_confirm == 'да':
                        user_confirm = input('Выберите, что вы хотите сделать с текущим файлом:\n'
                                             '1 - Добавить вакансии в конец текущего файла\n'
                                             '2 - Стереть прошлые данные и записать только текущие вакансии\n')
                        if user_confirm == '1':
                            json_file_handler.add_vacancies(vacancies_list)
                            print(f'Текущие вакансии добавлены в конец файла {file_name}')
                            quit()
                        elif user_confirm == '2':
                            json_file_handler.write_vacancies_to_file(vacancies_list)
                            print(f'Прошлые вакансии удалены из файла, текущие вакансии сохранены в файл {file_name}')
                            quit()
                        else:
                            print('Повторите попытку операции сохранения в файл')
            if user_input == '8':
                print('Данна функция еще находится в разработке и может работать некорректно.\n'
                      'Наша команда все починит в следующем обновлении\n')
                current_num_vacancies = len(vacancies_list)
                vacancies_list = json_file_handler.del_duplicate_vacancies(vacancies_list)
                new_num_vacancies = len(vacancies_list)
                delta_num_vacancies = current_num_vacancies - new_num_vacancies
                if current_num_vacancies != new_num_vacancies:
                    print('Совпадающие вакансии удалены\n'
                          f'Вакансий до удаления дубликатов: {current_num_vacancies}\n'
                          f'Вакансий после удаления дубликатов: {new_num_vacancies}\n'
                          f'Дубликатов было удалено: {delta_num_vacancies}')
                else:
                    print('Совпадений вакансий в текущем списке и в json-файле не найдено\n')
            if user_input in ['stop', 'стоп']:
                quit()
        if user_input in ['stop', 'стоп']:
            quit()
        else:
            print('Введите порядковый номер операции, которую хотите выполнить')
