def int_res(parametr):
    try:
        a = int(parametr)
        return True
    except:
        return False
def float_res(parametr):
    try:
        a = float(parametr)
        return True
    except:
        return False
def get_int():
    param = input('введите целое число: ')
    a = int_res(param)
    while a == 0:
        param = input('введено не целое число, попробуйте ещё раз: ')
        a = int_res(param)
    return param
def get_float():
    param = input('введите число: ')
    a = float_res(param)
    while a == 0:
        param = input('введено не число, попробуйте ещё раз: ')
        a = int_res(param)
    return param

print('введите количество курсов, которые собираетесь ввести')
quantitie = int(get_int())
mas_of_course = [[] for i in range(quantitie)]
for i in range(quantitie):
    print(f'введите {i+1} курс')
    first = input('введите первую валюту: ')
    second = input('введите вторую валюту: ')
    #'курс составляет'
    course = get_float()
    mas_of_course[i].append(first)
    mas_of_course[i].append(second)
    mas_of_course[i].append(course)
    print(first, second, 'курс сотавляет', course)


print('введите сумму, с которой начнётся конвертация')
need_sum = int(get_float())

val_start = input('введите начальную валюту ')

strok = input('введите через пробел в нужном порядке остальные валюты для конвертаций ')
valuti = strok.split()


valuti.insert(0, val_start)

chain = [0 for m in range(len(valuti))]
chain[0] = need_sum

for i in range(len(valuti) - 1):
    val = valuti[i] + valuti[i+1]
    course_i = 0

    for j in range(len(mas_of_course)):
        if mas_of_course[j][0] + mas_of_course[j][1] == val:
            course_i = float(mas_of_course[j][2])
    if course_i != 0:
        chain[i+1] = round(float(chain[i]) * course_i, 2)
    else:
        print('Операция не может быть выполнена. Возможно, вы хотите перевести сумму по курсу, не указанному ранее')
        print('или вы ошиблись в названии валюты. Повторите попытку.')
        break

spis_all = [[] for i in range(len(chain))]
for i in range(len(spis_all)):
    spis_all[i].append(str(chain[i]))
    spis_all[i].append(valuti[i])
spisok = []
for i in range(len(spis_all)):
    spisok.append(' '.join(spis_all[i]))
print(*spisok, sep='->')
