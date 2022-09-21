import lib
import os
r = 1

os.system("clear")

lib.WelcomeScreen()
print(f'Choose mode:')
print(f'(1)Connectivity in function of gamma')
print(f'(2)Connectivity in function of N with gamma = 1/2(N-1)')
dec = input()
c = int(dec)
if c == 1:
    print(f'Input N_min: ')
    nmin = input()
    print(f'Input N_max: ')
    nmax = input()
    print(f'Input step size: ')
    dn = input()
    lib.connect(int(nmin), int(nmax), int(dn), r)
#elif dec == '2':
elif c == 2:
    print(f'Input N_min: ')
    nmin = input()
    print(f'Input N_max: ')
    nmax = input()
    lib.sizeGraph(int(nmin), int(nmax), r)
else:
    print(f'Invalid choice!')
#else:
        #print(f'Invalid choose!')



