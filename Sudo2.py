import random

sor = [['4','3','9','8','6','7','2','5','1'],['1','7','8','5','4','2','6','3','9'],['6','5','2','9','3','1','8','4','7'],['7','4','3','1','9','8','5','6','2'],['5','2','6','4','7','3','1','9','8'],['8','9','1','6','2','5','4','7','3'],['3','1','7','2','5','4','9','8','6'],['9','8','4','3','1','6','7','2','5'],['2','6','5','7','8','9','3','1','4']]
jateksor= [['4','3','9','8','6','7','2','5','1'],['1','7','8','5','4','2','6','3','9'],['6','5','2','9','3','1','8','4','7'],['7','4','3','1','9','8','5','6','2'],['5','2','6','4','7','3','1','9','8'],['8','9','1','6','2','5','4','7','3'],['3','1','7','2','5','4','9','8','6'],['9','8','4','3','1','6','7','2','5'],['2','6','5','7','8','9','3','1','4']]

for i in range (0,9):
    y=random.randint(0,8)
    jateksor[i][y]= " "



def screen():
    print ('=========================')
    for i in range(0,len(jateksor)):
        if i%3==2:
            print ('| %s %s %s | %s %s %s | %s %s %s |' %(jateksor[i][0], jateksor[i][1], jateksor[i][2], jateksor[i][3], jateksor[i][4], jateksor[i][5], jateksor[i][6], jateksor[i][7], jateksor[i][8]))
            print ('=========================')
        else:
            print ('| %s %s %s | %s %s %s | %s %s %s |' %(jateksor[i][0], jateksor[i][1], jateksor[i][2], jateksor[i][3], jateksor[i][4], jateksor[i][5], jateksor[i][6], jateksor[i][7], jateksor[i][8]))
screen()
a=0
joValasz=0
while a<=8:
    x=int(input("Válassz sort!: "))
    y=int(input("Válassz oszlopot!: "))
    z=input("Mondj egy számot(1-9-ig): ")
   
    if jateksor[x-1][y-1]== " ":
        a+=1
        jateksor[x-1][y-1]=z
        screen()
        if z==sor[x-1][y-1]:
            joValasz+=1

    else: 
        print("Foglalt.")
    print(joValasz)

if joValasz==9:
    print("Jó megoldás!")
else: 
    print("Csak " + str(joValasz)+ "jó megoldás van!")

