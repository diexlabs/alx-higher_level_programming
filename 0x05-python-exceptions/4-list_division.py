#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    i = 0

    while i < list_length:
        try:
            q = my_list_1[i] / my_list_2[i]
            result.append(q)
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            i -= 1
            break
        except Exception:
            result.append(0)
        finally:
            i += 1
    while len(result) < list_length:
        result.append(0)

    return result
