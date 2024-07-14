def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding="utf-8") as fh:

            lines = [line.strip() for line in fh.readlines() if line.strip()]
            for line in lines:
                cat_data = line.split(',')
                if len(cat_data) == 3:
                    cat_info = {"id": cat_data[0], "name": cat_data[1], "age": cat_data[2]}
                    cats_info.append(cat_info)
                else: print(f"Line format error: {line}")
    except FileNotFoundError:
        print(f"File {path} not found.")
        return 0, 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0
    
    return cats_info
    fh.close()

if __name__ == '__main__':
    cats_info = get_cats_info("data/cats_file.txt")
    print(cats_info)



# Очікуваний результат:
# [
#     {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
#     {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
#     {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
#     {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
#     {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
# ]
