#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    x = []
    for i in range(list_length):
        try:
            y = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            y = None
        except (ValueError, TypeError):
            print("wrong type")
            y = None
        except IndexError:
            print("out of range")
            y = None
        finally:
            if y is None:
                x.append(0)
            else:
                x.append(y)
    return x
