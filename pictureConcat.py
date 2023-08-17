import os

folder_path = './'  # Укажите путь к папке, содержащей файлы
output_file = 'output.png'  # Укажите имя файла, в который будет записано содержимое всех файлов

file_list = sorted(os.listdir(folder_path))  # Получаем список файлов, отсортированных по алфавиту

i = 0

with open(output_file, 'wb') as output:
    for filename in file_list:
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and not filename.endswith('.py'):
            with open(file_path, 'rb') as file:
                binary_content = file.read()
                output.write(binary_content)
                i += 1

print("Объединение " + str(i) + " файлов закончено!")