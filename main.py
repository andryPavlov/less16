import patoolib
import os

# rar_file_path = r'C:\Users\37525\Desktop\Homework.rar'
# patoolib.extract_archive(rar_file_path, outdir=extract_path)


name_dir = r'Homework'
extract_path = r'C:\Users\37525\PycharmProjects\pythonProject'
absolut_path = extract_path + '\\' + name_dir
file_list = os.listdir(absolut_path)
name_puple = 'Сазонов Арнольд Авксентьевич'


print('*'*80, 'Вывод оценок всей группы',sep='\n')
for file_name in file_list:

    print(f'{file_name.capitalize()[:len(file_name)-4]}:')
    file_path = os.path.join(absolut_path, file_name)

    with open(file_path, 'r', encoding='UTF8') as file:
        print(file.read())


print('*'*80, 'Вывод оценок определенного учащегося',sep='\n')
for file_name in file_list:
    print(f'{file_name.capitalize()[:len(file_name)-4]}:')
    file_path = os.path.join(absolut_path, file_name)

    with open(file_path, 'r', encoding='UTF8') as file:
        for i in file.readlines():
            puple = i.split()
            if ' '.join(puple[:3]) == name_puple:
                print(i)

print('*'*80, 'Вывод учащихся чьи оценки 3 и меньше',sep='\n')

for file_name in file_list:
    print(f'{file_name.capitalize()[:len(file_name)-4]}:')
    file_path = os.path.join(absolut_path, file_name)

    with open(file_path, 'r', encoding='UTF8') as file:
        for i in file.readlines():
            puple = i.split()
            if int(puple[3]) < 3:
                print(i)
