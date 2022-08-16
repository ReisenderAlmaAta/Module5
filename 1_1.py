class StringVar():

    txt = input('Введите текст: ')

    def get(self):
        return self.txt

    def set(self):
        self.txt = input('Введите новый текст: ')


t1 = StringVar()
print(('Выберите действие'))
print('Для вывода текста нажмите "o"')
print('Для изменения нажмите c')
action = input()
if action == 'o' or action == 'O':
    print(f'Введённый текст: {t1.get()}')
elif action == 'c' or action == 'o':
    t1.set()
    print(f'Теперь текст: {t1.get()}')

