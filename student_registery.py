student=0

name=int(input('how many students are registering ?'))
file=open('reg_form.txt' , 'w')
for x in range(name):
    
    id_no=(input('your id numbe'))
    file.write(id_no +'\n')
    #student+=1




student=0
num = 0

names=int(input('how many students registering ?'))
for x in range(names):
    num+=1
    id_no = input(f'enter id number {num} ') 