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

file = open("temp.txt", "r")
res = file.read()
print(res)

file.close()