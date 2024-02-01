from src.functions import sort_operations, format_date, hide_from, hide_to, amount


def test_main():
    last_operations = sort_operations("C:/Users/ejik2/PycharmProjects/kursovaya_3/src/operations.json")
    format_last_operations = format_date(last_operations)
    assert format_last_operations[1]["date"] == "07.12.2019"
    for operation in format_last_operations:
        to_ = hide_to(operation.get("to"))
        from_ = ""
        if "from" in operation.keys():
            from_ = hide_from(operation.get("from"))
        else:
            pass
    assert to_ == 'Счет **** **** **** **** 8381'
    assert from_ == ''