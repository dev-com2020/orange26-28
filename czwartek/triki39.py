# d = {'a': 'A', 'b': 'B'}
# e = {'b': 8, 'c': 'C'}
# s = 'Hello There'
#
# print(d | e)
# print(e | d)
# print({**d, **e})
#
# print(s.removeprefix("Hello"))
# print(s.removesuffix("There"))
# print(s.removeprefix("Python"))


wybor = input("Napisz swoją ulubioną liczbę: ")

match wybor:
    case "1":
        print("Twoja ulubiona cyfra to", wybor)
    case "3":
        print("Twoja ulubiona cyfra to", wybor)
    case "5":
        print("Twoja ulubiona cyfra to", wybor)
    case "4":
        print("Twoja ulubiona cyfra to", wybor)
    case _:
        print("**Twoja ulubiona cyfra to**", wybor)

