import sys
import pathlib
from colorama import Fore, Style

def tree_visualizer(path, level=0):
    path = pathlib.Path(path)
    if path.is_dir():
        print(Fore.GREEN + '\t' * level + path.name + Style.RESET_ALL)
        for item in path.iterdir():
            tree_visualizer(item, level + 1)
    else:
        print(Fore.YELLOW + '\t' * level + path.name + Style.RESET_ALL)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        tree_visualizer(sys.argv[1])
    else:
        print("Будь ласка, вкажіть шлях до директорії як аргумент.")