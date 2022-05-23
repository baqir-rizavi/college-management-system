import datetime


def input_validated_int(prompt: str, additional_error_info='') -> int:
    while True:
        try:
            val = int(input(prompt))
            break
        except ValueError as e:
            print(additional_error_info + " / an invalid input enter again")
    return val


def input_validated_int_range(prompt: str, start, end, additional_error_info='') -> int:
    while True:
        try:
            val = int(input(prompt))
            if start <= val <= end:
                break
            else:
                print(additional_error_info + "/ an invalid input enter again")
        except ValueError as e:
            print("an invalid input enter again")
    return val


def input_validated_in(prompt: str, equal_to, additional_error_info=''):
    while True:
        val = input(prompt)
        if val in equal_to:
            return val
        print(additional_error_info + " / an invalid input enter again")


def input_validated_int_in(prompt: str, equals_to, additional_error_info=''):
    while True:
        try:
            val = int(input(prompt))
            if val in equals_to:
                return val
            else:
                print(additional_error_info + "/ an invalid input enter again")
        except ValueError as e:
            print("an invalid input enter again")


def input_validated_date():
    year = input_validated_int_range('enter year: ', 1, 9999)
    month = input_validated_int_range('enter month: ', 1, 12)
    day = input_validated_int_range('enter day: ', 1, 31)
    hours = input_validated_int_range('enter hour(24hc): ', 0, 23)
    minutes = input_validated_int_range('enter minutes: ', 0, 59)
    now = datetime.datetime(year=year, month=month, day=day, hour=hours, minute=minutes)
    return now.strftime('%Y-%m-%d %H:%M:%S')


def input_validated_float(prompt, additional_error_info=''):
    while True:
        try:
            val = float(input(prompt))
            break
        except ValueError as e:
            print(additional_error_info + " / an invalid input enter again")
    return val
