def word_up():
    '''Ввод слова для функции'''
    print("Ведите слово:")
    user_word = input()
    return user_word.upper()


def first_letter_up():
    '''Запрос фразы'''
    print("Введите фразу:")
    '''Ввод фразы'''
    user_input = input()
    '''Переводим строку в список'''
    user_input_split = user_input.split()
    for n in user_input_split:
        '''выводим элементы списка, каждый с загл. буквы'''
        print(n.title(), end=' ')
