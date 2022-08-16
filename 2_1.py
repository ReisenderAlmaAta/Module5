'''пустой список вjson файле был создан в файле 2_0.py '''
import json

class Model:
    title = input()
    text = input()
    author = input()

    def save(self):

        tmp = Model.__dict__
        res = {}
        for k, v in tmp.items():
            if not k.startswith('_'):
                res[k] = v
        del res['save']

        with open('files_info.json', 'r') as r:
            info = json.load(r)
        info.append(res)

        with open('files_info.json', 'w') as w:
            json.dump(info, w)


b = Model()
b.save()

'''Проверка вывода'''
with open('files_info.json', 'r') as r:
    info = json.load(r)
print('1: ', info)




