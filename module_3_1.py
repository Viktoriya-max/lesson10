from pickletools import string1

calls = 0
def count_calls():
    global calls # используем переменную в функции
    calls += 1 # подсчет колф-во функций

def string_info(enter):
    count_calls()
    string = len(enter) # подсчет символов в строке
    string1 = enter.upper() # перевод в верхний регистор
    string2 = enter.lower() # перевод в нижний регистор
    return string, string1, string2

def is_contains(st,list_):
    count_calls()
    st = st.upper() # перевод стороки в верхний регистор
    list_ = [st.upper() for st in list_] # перевод списка в верхний регистор
    return st in list_

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban',['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)




