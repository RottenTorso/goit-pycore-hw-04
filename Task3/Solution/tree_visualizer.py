# Імпортуємо необхідні модулі: sys для роботи з аргументами командного рядка,
# pathlib для роботи з файловою системою, colorama для кольорового виводу в термінал
import sys
import pathlib
from colorama import Fore, Style

# Оголошуємо функцію tree_visualizer для візуалізації структури директорій та файлів
# Яка приймає шлях до директорії або файлу та рівень вкладеності (за замовчуванням 0)
def tree_visualizer(path, level=0):
    # Перетворюємо отриманий шлях на об'єкт Path для зручності роботи
    path = pathlib.Path(path)
    # Перевіряємо, чи є поточний шлях директорією
    if path.is_dir():
        # Виводимо ім'я директорії зеленим кольором
        print(Fore.GREEN + '\t' * level + path.name + Style.RESET_ALL)
        # Рекурсивно викликаємо tree_visualizer для кожного елемента в директорії
        for item in path.iterdir():
            tree_visualizer(item, level + 1)
    else:
        # Виводимо ім'я файлу фіолетовим кольором
        print(Fore.MAGENTA + '\t' * level + path.name + Style.RESET_ALL)

# Перевіряємо, чи був скрипт запущений як головний файл, а не імпортований
if __name__ == "__main__":
    # Перевіряємо, чи був наданий шлях як аргумент командного рядка
    if len(sys.argv) > 1:
        # Викликаємо функцію tree_visualizer з наданим шляхом
        tree_visualizer(sys.argv[1])