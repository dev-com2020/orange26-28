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

