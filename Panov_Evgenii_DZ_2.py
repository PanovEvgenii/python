# задание 1. Выяснить тип результата выражений:


# one, two, three, four = 15 * 3, 15 / 3, 15 // 2, 15 ** 2
# print('15 * 3', '=', one,type(one))
# print('15 / 3', '=', two,type(two))
# print('15 // 2', '=', three,type(three))
# print('15 ** 2', '=', four, type(four))
#
# Выполнялось на средней сложности, заняло часа 2


# Задание 2, 3. Дан список:

# my_list =['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# my_list.insert(1, '"')
# my_list.insert(3, '"')
# my_list.insert(5, '"')
# my_list.insert(7, '"')
# my_list.insert(12, '"')
# my_list.insert(14, '"')
# for index, i in enumerate(my_list):
#     if i[0:14] == '5':
#         my_list[index] = f'{int(i):02}'
#     elif i[0:14] == '+5':
#         my_list[index] = i[:1] + i[5:].replace('', '05')
#
# print(' '.join(my_list))
#
# Выполнял 2 дня, очень сложн




# 4. Дан список, содержащий искажённые данные с должностями и именами сотрудников

# name=['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
#
# for i in name:
#     print('Привет,', i.split(' ')[-1].title())
#
# Сложно, выполнял часов 5. Помогли одногрупники. Жалко что такой простой код отнял столько времени




# 5.Создать вручную список, содержащий цены на товары (10–20 товаров)

# one_list = [235.1, 25, 525, 12.02, 54, 25.07, 15, 34, 12.43, 151.43, 235.12, 32, 235, 235, 212, 6457, 58, 345, 23, 4.34]
# print(id(one_list))
# one_list.sort()
# print(id(one_list))
# for i in one_list:
#     rub = int(i)
#     kop = int(i * 100) % 100
#     print(f'{rub} руб. {kop:02.0f} коп.', end=', ')
# print('_____________________________________________________________________________________________________________')
# twoo_list = sorted(one_list)[::-1][:5]
# twoo_list.sort()
# for i in twoo_list:
#     rub = int(i)
#     kop = int(i * 100) % 100
#     print(f'{rub} руб. {kop:02.0f} коп.', end=', ')
#
# Сложно. Нудно больше информации про "f" строки, про цикличность. приходится искать много информации вне курса.
# Плохо что так поверхостно по темам проходим.
# Минимум кода не получилось