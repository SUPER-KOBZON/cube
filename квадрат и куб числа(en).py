import os
name = input('Enter file name for reading: ')
while not os.path.exists(name):
    name = input('File is not exist, enter another name, pls: ')
    name += '.txt'
with open(name, "r") as file:
     list=file.readlines()
with open('out.txt', "w") as wfile:
    def printf(str):
        if (str): wfile.write(str + '\n')
        print(str)
    printf('|    number|    square|      cube|')
    a=('+' + '-' * 10 + '+' + '-' * 10 + '+' + '-' * 10 + '+')
    printf(a)
    size= len(list)
    for i in range (size):
        try:
            list[i] = float(list[i])
            s = "|{0:10.3f}|{1:10.3f}|{2:10.3f}|".format(list[i], pow(list[i], 2), pow(list[i], 3))
            printf(s)
        except ValueError:
            s = "|{0:>10}|".format(list[i].replace('\n', '')) + "-   invalid value    |"
            printf(s)
        printf(a)
m = input()		
