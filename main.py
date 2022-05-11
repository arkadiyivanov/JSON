
import json

surname = ['Sidorov', 'Gusev']

cash = ['1000000', '5000000']

surname_json = {'surname': surname}
cash_json = {'cash': cash}

with open('surname.json', 'w') as f:
    f.write(json.dumps(surname_json))

with open('cash.json', 'w') as f:
    f.write(json.dumps(cash_json))


with open('surname_cash.txt', "w") as surname_cash:
    with open('surname.json') as f:
        f = f.read()
        t = json.loads(f)
        for section, commands in t.items():
            surname_cash.write(' '.join(commands))
    with open('cash.json') as f:
        f = f.read()
        t = json.loads(f)
        for section, commands in t.items():
            surname_cash.write(' '.join(commands))





    # with open('listfile3.txt', "w") as listfile3:
    #     with open(LIST_FILE, 'r') as listfile:
    #         for f in listfile:
    #             listfile3.write(f)
    #     with open(LIST_F, 'r') as listfile:
    #         for f in listfile:
    #             listfile3.write(f)
    # listfile3.close()


if __name__ == '__main__':
    pass

