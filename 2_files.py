#----------
# Домашнее задание №2
#----------
# Задание: Работа с файлами

# 1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
# 2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
# 3. Подсчитайте количество слов в тексте
# 4. Замените точки в тексте на восклицательные знаки
# 5. Сохраните результат в файл referat2.txt

def main():
    with open("referat.txt", "r", encoding="utf-8") as referat:

        content = referat.read()                                        # 1
        len_referat = len(content)
        print(f"Количество символов в документе: {len_referat}")

        len_words = len(content.split())                                # 2
        print(f"Количество слов в документе: {len_words}")

        change_symbol = content.replace(".", "!")                       # 3
        print()

    with open("referat2.txt", "w", encoding="utf-8") as referat2:       # 4
        referat2.write(change_symbol)

if __name__ == "__main__":
    main()
