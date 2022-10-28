# def mnozenie(a, b):
#     try:
#         return int(a) * int(b)
#     except (TypeError, ValueError):
#         print("błąd typu, zwracam bezpieczne 0")
#         return 0

# def mnozenie(a, b):
#     try:
#         return int(a) * int(b)
#     except TypeError:
#         print("błąd typu, zwracam bezpieczne 0")
#         return 0
#     except ValueError:
#         print("błąd wartości, zwracam bezpieczne 0")
#         return 0

# def mnozenie(a, b):
#     try:
#         return int(a) * int(b)
#     except Exception as e:
#         print("Wystąpił:", e)
#         return 0

def mnozenie(a, b):
    try:
        print(int(a) * int(b))
    except Exception as e:
        print("Wystąpił:", e)
        print(0)
    else:
        wynik = []
        wynik.append(a)
        wynik.append(b)
        print(wynik)
    finally:
        print("Wykonywałem instrukcje z funkcji mnozenie()")


mnozenie(3, 4)
mnozenie("3", "4")
mnozenie("a", "b")
