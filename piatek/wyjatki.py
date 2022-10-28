# def mnozenie(a, b):
#     try:
#         return int(a) * int(b)
#     except (TypeError, ValueError):
#         print("błąd typu, zwracam bezpieczne 0")
#         return 0

def mnozenie(a, b):
    try:
        return int(a) * int(b)
    except TypeError:
        print("błąd typu, zwracam bezpieczne 0")
        return 0
    except ValueError:
        print("błąd wartości, zwracam bezpieczne 0")
        return 0


print(mnozenie(3, 4))
print(mnozenie("3", "4"))
print(mnozenie("a", "b"))
