def total_salary(path):
    try:
        # Відкриваємо файл за вказаним шляхом з кодуванням UTF-8
        with open(path, 'r', encoding='UTF-8') as file_with_data:
            data = file_with_data.readlines()  # Зчитуємо всі рядки файлу
            amounts = []  # Список для зберігання знайдених чисел
            for line in data:
                try:
                    # Намагаємось перетворити другий елемент після розділення комою на ціле число і додати до списку
                    amounts.append(int(line.split(',')[1]))
                except ValueError:
                    # Якщо перетворення не вдалося - ігнорувати цей рядок
                    continue
        if not amounts:  # Перевіряємо, чи список не пустий
            return print("У файлі немає значень для обчислення")  # Виводимо повідомлення, якщо список пустий
        total = sum(amounts)  # Обчислюємо суму всіх зарплат
        average = total / len(amounts)  # Обчислюємо середню зарплату
        return (total, average)
    except FileNotFoundError:
        # Виводимо повідомлення, якщо файл не знайдено
        print(f"Файл {path} не знайдено.")
    except Exception as e:
        # Виводимо повідомлення про будь-яку іншу помилку
        print(f"Сталася помилка: {e}")