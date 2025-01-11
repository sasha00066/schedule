import csv

short = {
    'Беларуская  лiтаратура':                'бел. лит.   ',
    'Беларуская мова':                       'бел. яз.    ',
    'Беларуская лiтаратура':                 'бел. лит.   ',
    'Русский язык':                          'русск. яз.  ',
    'Русская литература':                    'русск. лит. ',
    'Английский язык':                       'англ. яз.   ',
    'Немецкий язык':                         'нем. яз.    ',
    'Китайский язык':                        'китайский   ',
    'Информатика':                           'информ.     ',
    'Физика':                                'физика      ',
    'Астрономия':                            'астрономия  ',
    'Человек и мир':                         'чел. и мир  ',
    'Химия':                                 'химия       ',
    'Допризывная и медицинская подготовка':  'допр. и мед.',
    'Биология':                              'биология    ',
    'Математика':                            'математика  ',
    'Обществоведение':                       'обществ.    ',
    'Всемирная история':                     'всем. ист.  ',
    'История Беларуси':                      'ист. Бел.   ',
    'География':                             'георафия    ',
    'Физическая культура и здоровь':         'физ-ра      ',
    'Физическая культура и здоровье':        'физ-ра      ',
    'Час здоровья и спорта':                 'ЧЗС         ',
    'Трудовое обучение':                     'труд. обуч. ',
    'Черчение':                              'черчение    ',
    'Искусство':                             'искусство   ',
    'Основы безопасности жизнедеятельности': 'ОБЖ         ',
    '???':                                   '???         ',
    '':                                      '???         '
}

print('Расписание занятий')

table = []

# Extracting data from table
with open('data.csv', newline='', encoding='utf-16') as f:
    reader = csv.reader(f, csv.excel_tab, delimiter=',')
    for row in reader:
        table.append(row)

form = input('Класс: ').upper()

# Searching for form
schedule = []
for j in range(3, len(table[0])):
    for i in range(len(table)):
        if form in table[i][j]:
            schedule.append((i, j))
            break
    else:
        schedule.append(None)

# Output results
old_schedule = schedule.copy()
schedule = []
for a in old_schedule:
    if a is None:
        schedule.append(short['???'] + ' ' * 7)
    else:
        i, j = a
        schedule.append('{:6}'.format(table[i][j][-6:]) + ' ' + short[table[i][2]])
schedule = schedule[1:]
tschedule = [[[]] * 10 for _ in range(7)]
for i in range(len(schedule)):
    tschedule[i // 10][i % 10] = schedule[i]
if old_schedule[0] is not None:
    print('Класная: ' + table[old_schedule[0][0]][1])
print(f'    Понедельник        Вторник            Среда              Четверг            Пятница')
print(f' 1. {tschedule[0][0]}{tschedule[1][0]}{tschedule[2][0]}{tschedule[3][0]}{tschedule[4][0]}')
print(f' 2. {tschedule[0][1]}{tschedule[1][1]}{tschedule[2][1]}{tschedule[3][1]}{tschedule[4][1]}')
print(f' 3. {tschedule[0][2]}{tschedule[1][2]}{tschedule[2][2]}{tschedule[3][2]}{tschedule[4][2]}')
print(f' 4. {tschedule[0][3]}{tschedule[1][3]}{tschedule[2][3]}{tschedule[3][3]}{tschedule[4][3]}')
print(f' 5. {tschedule[0][4]}{tschedule[1][4]}{tschedule[2][4]}{tschedule[3][4]}{tschedule[4][4]}')
print(f' 6. {tschedule[0][5]}{tschedule[1][5]}{tschedule[2][5]}{tschedule[3][5]}{tschedule[4][5]}')
print(f' 7. {tschedule[0][6]}{tschedule[1][6]}{tschedule[2][6]}{tschedule[3][6]}{tschedule[4][6]}')
print(f' 8. {tschedule[0][7]}{tschedule[1][7]}{tschedule[2][7]}{tschedule[3][7]}{tschedule[4][7]}')
print(f' 9. {tschedule[0][8]}{tschedule[1][8]}{tschedule[2][8]}{tschedule[3][8]}{tschedule[4][8]}')
print(f'10. {tschedule[0][9]}{tschedule[1][9]}{tschedule[2][9]}{tschedule[3][9]}{tschedule[4][9]}')
while True:
    pass
