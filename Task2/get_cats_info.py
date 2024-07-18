def get_cats_info(path):
    cats_info = []  # Ініціалізуємо порожній список для зберігання інформації про котів

    try:
        # Відкриваємо файл з вказаним шляхом і кодуванням UTF-8
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:  # Перебираємо кожен рядок у файлі
                chunks = line.split(',')  # Парсимо рядок за допомогою коми
                if len(chunks) > 0:  # Перевіряємо, чи рядок не є порожнім
                    # Створюємо словник з інформацією про кота і додавання його до списку
                    cat = {'id': chunks[0], 'name': chunks[1], 'age': int(chunks[2])}
                    cats_info.append(cat)
                else:
                    # Виводимо повідомлення, якщо рядок порожній
                    print(f"Рядок порожній")
    except FileNotFoundError:
        # Виводимо повідомлення, якщо файл не знайдено
        print(f"Файл {path} не знайдено")
    except Exception as e:
        # Виводимо повідомлення про будь-яку іншу помилку
        print(f"Сталася помилка: {e}")
    return cats_info  # Повертаємо список з інформацією про котів