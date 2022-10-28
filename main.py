from piatek import login

haslo = input("Podaj hasło: ")

if not login.wazne_haslo(haslo):
    print("Hasło jest nieprawidłowe")
else:
    print("OK, hasło jest poprawne!")


# if __name__ == '__main__':
    # haslo = input("Podaj hasło: ")
    #
    # if not login.wazne_haslo(haslo):
    #     print("Hasło jest nieprawidłowe")
    # else:
    #     print("OK, hasło jest poprawne!")