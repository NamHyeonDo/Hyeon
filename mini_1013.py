""" a = "*"
for b in range(5, 0, -1):
    print(a * b)
    
for b in range(1, 6):
    print(a * b)
    
for b in range(1, 6):
    spaces = " " * (6 - b)
    stars = "*" * (2 * b - 1)
    print(spaces + stars)
    
for b in range(1, 6):
    spaces = " " * (6 - b)
    stars = "*" * (2 * b - 1)
    print(spaces + stars)
for b in range(6, 0, -1):
    spaces = " " * (6 - b)
    stars = "*" * (2 * b - 1)
    print(spaces + stars) """
    
""" num = 0
line = []
for i in range(5):
    for j in range(5):
        num += 1
        line.append(num)
    print(line)
    line = []    
    
    
num = 0
line = []
for i in range(1, 6):
    for j in range(1, 6):
        num = ((j-1) * 5) + i
        line.append(num)
    print(line)
    line = []    
    
num = 26
line = []
for i in range(5):
    for j in range(5):
        num -= 1
        line.append(num)
    print(line)
    line = []  """      
    
""" import random
def get_computer_choice():
    choices = ['1', '2', '3']
    return random.choice(choices)

def determine_winner(user_choice):
    pcnum = get_computer_choice()
    print(user_choice, pcnum)
    if user_choice == pcnum:
        print("무승부")
        return
    
    elif(
        (user_choice == "1" and pcnum "3") or
        (user_choice == "2" and pcnum "1") or
        (user_choice == "3" and pcnum "2") 
    ): """
        
        
""" file = open("“c:/User/Catholic/temp.txt”", 'w')
file.close()  """

""" file = open("temp.txt", "r")
file.close() """

""" file = open("temp.txt", "a")
file.close() """

""" file = open("temp.txt", "r+")
file.close() """

#파일 쓰기
""" file = open("temp.txt", 'w')
file.write("hello")
file.write("world")

file.close() """

""" f = open ("c:\\User\\Catholic\\temp.txt")
for i  in range(100) :
    f.write(f"{i}\n")

f.close() """

#파일 추가 쓰기
""" f = open ("c:\\User\\Catholic\\temp.txt")
file = open("temp.txt", "a")
file.write("hello\n")
file.write("world")

file.close() """

""" file = open("temp.txt", "r")
res = file.read()
print(res)

file.close() """

""" #활용
import os
fp = "temp.txt"
file = open(fp, "w")
if os.path. exists(fp):
        print("ok")
        
else :
    print("error")
    
file.close """

#삭제
""" import os
fp = "new.txt"

f = open(fp, "w")
f.close()

os.remove(fp)
print("complete") """

#
""" import os

def dir_print(p):
    files = os.listdir(p)
    for f in files:
        print(f)
        
fp = "new.txt"
f = open(fp, "w")
f.close()

dir_print("./")

os.remove(fp)
print("----------------------\n\n")
dir_print("./") """

#파일명 변경
""" import os
fp = "new.txt"
f = open(fp, "w")
f.close()

os.rename(fp, "new.txt")
print("complete") """

#재변경 예외처리
""" import os

fp = "new.txt"
tp = "new1.txt"

f = open(fp, "w")
f.close

if os.path.exists(tp):
    print("exist, same name file")
    os.remove(tp)
else:
    os.remove(fp, "new1.txt")
    print("complate") """
    
#위에서 했던것들
""" import os
def dir_print(p):
    files = os.listdir(p)
    for f in files:
        print(f)
        
fp = "new.txt"
tp = "new1.txt"

f = open(fp, "w")
f.close

dir_print("./")
print("\n----------------------")

if os.path.exists(tp):
    print("exist, same name file")
    os.remove(tp)
else:
    os.remove(fp, "new1.txt")
    print("complate") """
    
#with

""" with open(tamp.txt, "r") as f:
    print(f.read()) """