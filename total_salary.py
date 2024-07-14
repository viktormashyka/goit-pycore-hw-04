def total_salary(path):
    total = 0
    count_lines = 0

    try:
        with open(path, 'r', encoding="utf-8") as fh:
            for line in fh:
                if not line.strip():
                    continue
                comaIndex = line.find(",")
                if comaIndex == -1:
                    continue
                salary_srt = line[comaIndex + 1:].strip()
                try:
                    salary = int(salary_srt)
                    total  += salary
                    count_lines += 1
                except ValueError:
                    continue
        
        average = int(total / count_lines) if count_lines != 0 else 0

    except FileNotFoundError:
        print(f"File {path} not found.")
        return 0, 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0
    
    return total, average
    fh.close()

if __name__ == '__main__':
    total, average = total_salary("data/salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


# Очікуваний результат:
# Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000
