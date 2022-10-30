main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
def get_count_char(str_):
    dict_ = {}
    str_ = str_.lower()
    for char in str_:
        if char.isalpha():
            if char in dict_:
                dict_[char] += 1
            else:
                dict_[char] = 1
    return dict_# TODO посчитать количество каждой буквы в строке в аргументе str_

def percent_dict_(str_dict_):
    sum_ = sum(str_dict_.values())
    for n in str_dict_:
        str_dict_[n] = round((str_dict_[n]/sum_) * 100, 1)
    return str_dict_
print(get_count_char(main_str))
var = get_count_char(main_str)
print(percent_dict_(var))