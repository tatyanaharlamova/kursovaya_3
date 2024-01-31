import datetime
import json


def read_json(file_name):
    """
    Считывает данные из файла .json, возвращает список словарей
    """
    with open(file_name, "r") as file:
        operations = json.load(file)
    return operations


def sort_operations(file_name):
    """
    Сортирует список словарей по дате
    """
    operations_list = read_json(file_name)
    execute_operations_list = []
    for operation in operations_list:
        if operation.get("state") == "EXECUTED":
            execute_operations_list.append(operation)
    sorted_operations = sorted(execute_operations_list, key=lambda x: x.get("date"), reverse=True)
    return sorted_operations[:5]


def format_date(operation_list):
    """
    Меняет формат даты на DD.MM.YYYY
    """
    for operation in operation_list:
        operation["date"] = datetime.datetime.strptime(operation["date"], '%Y-%m-%dT%H:%M:%S.%f')
        operation["date"] = operation["date"].strftime("%d.%m.%Y")
    return operation_list


def hide_from(operation):
    """
    Возвращает частично скрытый номер отправителя
    """
    list_from = operation.split(" ")
    name_from = list_from[0]
    if list_from[1] != list_from[-1]:
        name_from = name_from + " " + list_from[1]
    number_from = list(list_from[-1])
    for index in range(len(number_from)):
        if index in range(6, len(number_from) -4):
            number_from[index] = "*"
    number_from.insert(4, " ")
    number_from.insert(9, " ")
    number_from.insert(14,  " ")
    number_from.insert(19, " ")

    return f"{name_from} {"".join(number_from)}"


def hide_to(operation):
    """
    Возвращае частично скрытый номер получателя
    """
    list_to = operation.split(" ")
    name_to = list_to[0]
    if list_to[1] != list_to[-1]:
        name_to = name_to + " " + list_to[1]
    number_to = list(list_to[-1])
    for index in range(len(number_to)):
        if index in range(0, len(number_to) -4):
            number_to[index] = "*"
    number_to.insert(4,  " ")
    number_to.insert(9, " ")
    number_to.insert(14,  " ")
    number_to.insert(19, " ")

    return f"{name_to} {"".join(number_to)}"


def amount(operation):
    """
    Возвращет сумму перевода и валюту
    """
    amount_ = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    return f"{amount_} {currency}"

