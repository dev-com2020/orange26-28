def liczby(c, *cyfra):
    print(c)
    print(cyfra)


def connect(**opcje):
    conn_param = {
        'host': '127.0.0.7',
        'port': '8080',
        'user': 'admin',
        'pass': '123456'
    }
    conn_param['pwd'] = opcje
    print(conn_param)
    # print(opcje)


connect()
connect(root='/')


# liczby(5, 4, 43, 7)
# liczby(7)
# liczby(43, 7)
# liczby()

# krotka = 4,
# print(krotka)

def wypisz_1(a, b, c):
    print(f"a={a} b={b} c={c}")


def wypisz(a, b, /, c):
    print(f"a={a} b={b} c={c}")


wypisz_1(c=1, a=2, b=3)
wypisz(1, 2, 3)
wypisz(1, 2, c=3)


# wypisz(c=1, a=2, b=3)

def allparams(a, b, /, c=42, *args, d=256, e, **kwargs):
    print('a, b, c:', a, b, c)
    print('d, e:', d, e)
    print('args:', args)
    print('kwargs:', kwargs)


allparams(2, 6, e=10, f=11)
