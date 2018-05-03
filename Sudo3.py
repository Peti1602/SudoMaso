import random

sor = [['4', '3', '9', '8', '6', '7', '2', '5', '1'],
       ['1', '7', '8', '5', '4', '2', '6', '3', '9'],
       ['6', '5', '2', '9', '3', '1', '8', '4', '7'],
       ['7', '4', '3', '1', '9', '8', '5', '6', '2'],
       ['5', '2', '6', '4', '7', '3', '1', '9', '8'],
       ['8', '9', '1', '6', '2', '5', '4', '7', '3'],
       ['3', '1', '7', '2', '5', '4', '9', '8', '6'],
       ['9', '8', '4', '3', '1', '6', '7', '2', '5'],
       ['2', '6', '5', '7', '8', '9', '3', '1', '4']]

jateksor = [['4', '3', '9', '8', '6', '7', '2', '5', '1'],
            ['1', '7', '8', '5', '4', '2', '6', '3', '9'],
            ['6', '5', '2', '9', '3', '1', '8', '4', '7'],
            ['7', '4', '3', '1', '9', '8', '5', '6', '2'],
            ['5', '2', '6', '4', '7', '3', '1', '9', '8'],
            ['8', '9', '1', '6', '2', '5', '4', '7', '3'],
            ['3', '1', '7', '2', '5', '4', '9', '8', '6'],
            ['9', '8', '4', '3', '1', '6', '7', '2', '5'],
            ['2', '6', '5', '7', '8', '9', '3', '1', '4']]

# Random kiveszünk számokat a táblázatból


for i in range(0, 9):
    y = random.randint(0, 8)
    jateksor[i][y] = " "

# Kirajzoljuk a foghíjas táblát


def screen():
    print('=========================')
    for i in range(0, len(jateksor)):
        if i % 3 == 2:
            print('| %s %s %s | %s %s %s | %s %s %s |' % (
                jateksor[i][0], jateksor[i][1], jateksor[i][2], jateksor[i][3], jateksor[i][4],
                jateksor[i][5], jateksor[i][6], jateksor[i][7], jateksor[i][8]))
            print('=========================')
        else:
            print('| %s %s %s | %s %s %s | %s %s %s |' % (
                jateksor[i][0], jateksor[i][1], jateksor[i][2], jateksor[i][3], jateksor[i][4],
                jateksor[i][5], jateksor[i][6], jateksor[i][7], jateksor[i][8]))

# Ellenőrizzük a bejövő paramétereket


def error_handing(question):
    index = 0
    while index < 1:
        number = (input(question))
        if number in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            index += 1
        elif number == 'q':
            exit()
        else:
            number = 0
            print('Hibás szám!')
    return number


screen()
a = 0
joValasz = 0
while a <= 8:
    x = int(error_handing("Válassz sort!: "))
    y = int(error_handing("Válassz oszlopot!: "))
    z = str("\x1b[1;31m{}\x1b[0;37m" . format(error_handing("Mondj egy számot(1-9-ig):")))

    if jateksor[x-1][y-1] == " ":
        a += 1
        jateksor[x-1][y-1] = z
        screen()
        if z == sor[x-1][y-1]:
            joValasz += 1

    else:
        print("Foglalt.")

if joValasz == 9:
    print("Jó megoldás!")
else:
    print(str(joValasz) + " jó megoldás van!")
