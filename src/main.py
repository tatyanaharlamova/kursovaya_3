from functions import sort_operations, format_date, hide_from, hide_to, amount


def main():
    last_operations = sort_operations("operations.json")
    format_last_operations = format_date(last_operations)
    for operation in format_last_operations:
        to_ = hide_to(operation.get("to"))
        from_ = ""
        if "from" in operation.keys():
            from_ = hide_from(operation.get("from"))
        else:
            pass
        amount_ = amount(operation)
        print(f"{operation["date"]} {operation["description"]}\n{from_} -> {to_}\n{amount_}\n")


if __name__ == '__main__':
    main()


