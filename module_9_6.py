def all_variants(text):                 # Создаем функцию-генератор
    for i in range(len(text)):          # Внешний цикл, который итерируется по длине строки text
        for j in range(len(text) - i):  # Внутрений цикл, который итерируется от 0 до len(text) - i
         yield text[j: i + j + 1]       # Возвращаем подстроки начиная с индекса j до индекса i + j + 1

a = all_variants("abc")
for i in a:
    print(i)
