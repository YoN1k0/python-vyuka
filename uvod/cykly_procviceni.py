rozmer = int(input("rozmer"))

for radek in range(0, rozmer):
    for sloupec in range(radek, rozmer):
        print(' ', end='')
    for sloupec in range(0, radek):
        print('* ', end='')
    print('')