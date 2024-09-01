def all_variants(text):
    for k in text:           # Цикл по каждому элементу строки text
        yield k              # Возвращаем каждый элемент text
    yield text[0] + text[1]  # Возвращаем первый и второй элемент text
    yield text[1] + text[2]  # Возвращаем второй и третий элемент text
    yield text               # Возвращаем исходную строку text

a = all_variants("abc")
for i in a:
    print(i)