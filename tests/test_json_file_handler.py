import os
from config import ROOT_DIR

TEST_FILE_PATH1 = os.path.join(ROOT_DIR, 'data', 'test.json')


def test_write_vacancy(get_json_file_handler_object, list_object_vacancies,
                       list_dict_vacancies_1):
    get_json_file_handler_object.write_vacancies_to_file(list_object_vacancies)
    assert get_json_file_handler_object.get_vacancies() == [
        {
            "name": "Тестировщик комфорта квартир",
            "professional_roles": "Руководитель проектов",
            "experience": "Нет опыта",
            "employment": "Полная занятость",
            "schedule": "Гибкий график",
            "salary_from": 350000,
            "salary_to": 450000,
            "currency": "RUR",
            "employer": "Специализированный застройщик BM GROUP",
            "requirement": "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...",
            "responsibility": "Оценивать вид из окна: встречать рассветы на кухне, и провожать алые закаты в спальне. Оценивать инфраструктуру района: ежедневно ходить на...",
            "url": "https://hh.ru/vacancy/93353083"
        }
    ]


def test_del_vacancy(get_json_file_handler_object, list_dict_vacancies_3):
    get_json_file_handler_object.del_vacancy(list_dict_vacancies_3)
    assert get_json_file_handler_object.get_vacancies() == []


def test_add_vacancy(get_json_file_handler_object, list_object_vacancies,
                     list_dict_vacancies_3):
    get_json_file_handler_object.add_vacancies(list_object_vacancies)
    assert get_json_file_handler_object.get_vacancies() == [list_dict_vacancies_3]
    get_json_file_handler_object.del_vacancy(list_dict_vacancies_3)  # строка возвращающая файл в исходное состояние
