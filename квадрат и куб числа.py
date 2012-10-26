import os 
name = input('Введите имя файла для чтения: ')
name += '.txt'
while not os.path.exists(name):
    name = input('Файл не существует! Пожалуйста, введите имя файла еще раз: ')
    name += '.txt'
with open(name, "r") as file:
     list=file.readlines()
with open('out.txt', "w") as wfile:
    
    #function for show on dysplay and write in file in one time
    def printf(str):
        if (str): wfile.write(str + '\n')
        print(str)
        
    printf('|     число|   квадрат|       куб|')
    # string a for table
    a=('+' + '-' * 10 + '+' + '-' * 10 + '+' + '-' * 10 + '+')
    printf(a)
    size= len(list)
    for i in range (size):
        try:
            list[i] = float(list[i])
            s = "|{0:10.3f}|{1:10.3f}|{2:10.3f}|".format(list[i], pow(list[i], 2), pow(list[i], 3)) #format values for table
            printf(s)
        except ValueError:
            s = "|{0:>10}|".format(list[i].replace('\n', '')) + "-   неверное значение|"
            printf(s)
        printf(a)
m = input("результаты сохранены в файле "out.txt"")		
