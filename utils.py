import json


def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


def all_candidates():
    """
    покажет всех кандидатов
    :return: list
    """
    data = load_candidates()
    candidates = [i['name'] for i in data]
    return candidates


def get_by_pk(pk):
    """
    возвращает кандидата, ссылку на картинку, навыки по pk,
    :return: str
    """
    data = load_candidates()
    for i in data:
        if pk == i['pk']:
            return i['name'], i['picture'], i['skills']
    return 'NOT FOUND'


def get_by_skill(skill_name):
    """
    Возвращает кандидата по навыку
    :return: list
    """
    data = load_candidates()
    candidates = [i['name'] for i in data if (" " + skill_name.lower()) in (" " + i['skills'].lower())]
    return candidates
