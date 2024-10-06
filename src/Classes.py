import os
class Txt_merge:
    def __init__(self):
        pass
    def merge_files(self, file_names: list, output_file: str):
        file_info = []
    # Считываем информацию о файлах
        for file_name in file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                line_count = len(lines)
                file_info.append((file_name, line_count, lines))
    # Сортируем файлы по количеству строк
        file_info.sort(key=lambda x: x[1])
    # Записываем в выходной файл
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for file_name, line_count, lines in file_info:
                outfile.write(f"{file_name}\n{line_count}\n")  # Записываем имя файла и количество строк
                outfile.writelines(lines)  # Записываем содержимое файла