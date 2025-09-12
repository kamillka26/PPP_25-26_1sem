import sys
try:
    kol=int(input('введите количество студентов:'))
except ValueError:
    print('Ошибка: введено не целое число. Повторите попытку.')
except KeyboardInterrupt:
    print('Ошибка: вы завершили выполнение кода.')
else:
    mas_student=[]
    for i in range(kol):
        mas_student.append(input('введите имя студента:'))

    try:
        classes=int(input('введите количество предметов:'))
    except ValueError:
        print('Ошибка: введено не целое число.')
    except KeyboardInterrupt:
        print('Ошибка: вы завершили выполнение кода.')
    else:
        works=[]
        try:
            for i in range(classes):
                works.append(input('введите название предмета:'))
        except KeyboardInterrupt:
            print('Ошибка: вы завершили выполнение кода.')
        else:

            all_marks=[]
            for i in range(kol):
                all_marks.append([])

            try:
                for i in range(kol):
                    for j in range(classes):
                        all_marks[i].append(int(input(f'введите оценку студента {mas_student[i]} по предмету {works[j]}:')))
                        if all_marks[i][j]>5 or all_marks[i][j]<1:
                            sys.exit('Ошибка: введено число, не соответствующее пятибальной шкале оценивания.')
            except ValueError:
                print('Ошибка: введено не целое число.')
            except KeyboardInterrupt:
                print('Ошибка: вы завершили выполнение кода.')
            else:
                sredb_all=[]
                for i in range(kol):
                    sumb=0
                    for j in range(classes):
                        sumb+=all_marks[i][j]
                    srzn=sumb/classes
                    sredb_all.append(srzn)    #это средние баллы всех
                    print(f'средний балл студента {mas_student[i]}',srzn)


                marks_for_class=[]
                for i in range(classes):
                    marks_for_class.append([])
                for i in range(classes):
                    for j in range(kol):
                        marks_for_class[i].append(all_marks[j][i])

                for i in range(classes):
                    print(f'минимальная оценка по предмету {works[i]}: {min(marks_for_class[i])}')
                    print(f'максимальная оценка по предмету {works[i]}: {max(marks_for_class[i])}')

                the_best=max(sredb_all)
                the_worst=min(sredb_all)
                best=[]
                worst=[]
                for i in range(kol):
                    if sredb_all[i]==the_best:
                        best.append(mas_student[i])
                    if sredb_all[i]==the_worst:
                        worst.append(mas_student[i])

                print('лучший средний балл:'),print(*best,sep=', ')
                print('худший средний балл:'),print(*worst,sep=', ')
