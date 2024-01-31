from src.functions import read_json, sort_operations, format_date, hide_from, hide_to, amount
import pytest


@pytest.fixture
def test_list():
    test_list = sort_operations("../src/operations.json")
    return test_list


def test_read_json():
    assert read_json("../src/operations.json")[0]["id"] == 441945886


def test_read_json_not_file():
    with pytest.raises(FileNotFoundError):
        read_json("1.json")


def test_sort_operations():
    assert sort_operations("../src/operations.json")[0]["date"] == "2019-12-08T22:46:21.935582"
    assert sort_operations("../src/operations.json")[1]["date"] == "2019-12-07T06:17:14.634890"
    assert sort_operations("../src/operations.json")[1][("from")] == "Visa Classic 2842878893689012"

def test_sort_operatios_not_file():
    with pytest.raises(FileNotFoundError):
        sort_operations("1.json")


def test_formate_date(test_list):
    assert format_date(test_list)[1]["date"] == "07.12.2019"


test_dict = {
    "id": 536723678,
    "state": "EXECUTED",
    "date": "2018-06-12T07:17:01.311610",
    "description": "Перевод организации",
     "operationAmount": {
     "amount": "26334.08",
      "currency": {
        "name": "USD",
        "code": "USD"}},
    "from": "Visa Classic 4195191172583802",
    "to": "Счет 17066032701791012883"}


def test_hide_from():
    assert hide_from(test_dict["from"]) == "Visa Classic 4195 19** **** 3802 "
    assert hide_from("Visa 4195191172583802") == "Visa 4195 19** **** 3802 "


def test_hide_from_er():
    with pytest.raises(AttributeError):
        hide_from(0)


def test_hide_from_er_ind():
    with pytest.raises(IndexError):
        hide_from("4195")


def test_hide_to():
    assert hide_to(test_dict["to"]) == "Счет **** **** **** **** 2883"
    assert hide_to("Visa Classic 4195191172583802") == "Visa Classic **** **** **** 3802 "


def test_hide_to_er():
    with pytest.raises(AttributeError):
        hide_to(0)


def test_amount():
    assert amount(test_dict) == '26334.08 USD'



