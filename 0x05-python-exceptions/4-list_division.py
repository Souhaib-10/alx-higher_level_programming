#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        list_div = 0
        try:
            list_div = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except (IndexError, ValueError):
            print("out of range")
        finally:
            result.append(list_div)
    return result
