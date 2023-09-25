#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list_div = []

    for x in range(list_length):
        div = 0

        try:
            div = my_list_1[x] / my_list_2[x]

        except (ValueError, ZeroDivisionError):
            print("division by 0")

        except (TypeError):
            print("wrong type")

        except (IndexError):
            print("out of range")

        finally:
            list_div.append(div)

        return list_div
