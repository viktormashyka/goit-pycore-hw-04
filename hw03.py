import sys
from pathlib import Path
from colorama import Fore, Style

def get_dir_info():
    if len(sys.argv) > 1:
        input_path_dir = sys.argv[1]
        dir_path = Path(input_path_dir)
        if dir_path.exists() and dir_path.is_dir():
            for path in sorted(dir_path.iterdir()):
                print(Fore.GREEN + str(path) + Style.RESET_ALL)
        else: print(Fore.RED + f"{dir_path} директорії не існує" + Style.RESET_ALL)
    else: print(Fore.RED + f"Шлях до директорії не введено" + Style.RESET_ALL)

if __name__ == "__main__":
    get_dir_info()

# Приклад викристання:
# in terminal =>> python hw03.py data
# Очікуваний результат:
# data/salary_file.txt
# data/cats_file.txt