import numpy as np
import pandas as pd
import random as rd

def WelcomeScreen():
    print(f'[][][][][][][][][][][][][][][][][][][][][][][][][][][][][]')
    print(f'[][][][][][][] MODE-LOCKED GRAPH ANALYSIS [][][][][][][][]')
    print(f'[][][][][][][][][][][][][][][][][][][][][][][][][][][][][]')


def genFreq(N):
    f =  np.zeros(N)
    for i in range(0, N):
        f[i] = rd.random()

    return sorted(f)

def fmc(f, g):
    c = 0

    for l in range(0, len(f)):
        for k in range(0, l):
            for j in range(0, k):
                for i in range(0, j):
                    if abs(f[i] + f[l] - f[k] - f[j]) <= g:
                        c += 1
                    #elif abs(f[i] + f[k] - f[l] - f[j]) <= g:
                    #    c += 1
                    #elif abs(f[i] + f[j] - f[l] - f[k]) <= g:
                    #    c += 1

    return c

def sizeGraph(nmin, nmax, r):

    N = np.arange(nmin, nmax ,1)

    t = np.zeros(len(N))
    s = np.zeros(len(N))

    filename = "tetrads_R" + f'{r}.dat'
    file = open(filename, "w")

    for i in range(0, len(N)):
        g = 1. / (2 * (N[i] - 1))
        tetrads = N[i] * (N[i] - 1) * (N[i] - 2) * (N[i] - 3) / 24
        c = np.zeros(r)
        for k in range(0, r):
            f = genFreq(N[i])
            c[k] = fmc(f, g) / tetrads

        t[i] = np.mean(c)
        s[i] = np.std(c)
        print(f'{N[i]}\t{t[i]}\t{s[i]}')
        file.write(f'{1./N[i]}\t{t[i]}\t{s[i]}\n')

    file.close()

def connect(nmin, nmax, dn, r):

    N = np.arange(nmin, nmax, dn)
    g = np.arange(0, 1., 0.05)
    t = np.ndarray(shape=(len(N), len(g)))
    s = np.ndarray(shape=(len(N), len(g)))
    filename = "connectivity_R" + f'{r}.dat'
    file = open(filename, "w")
    for i in range(0, len(N)):
        tetrads = N[i] * (N[i] - 1) * (N[i] - 2) * (N[i] - 3) / 24
        for j in range(0, len(g)):
            c = np.zeros(int(r))
            for k in range(0, r):
                f = genFreq(N[i])
                c[k] = (fmc(f, g[j]) / tetrads)
                # print(f'c[{i}][{j}][{k}] = {c[i][j][k]}')

            t[i][j] = np.mean(c)
            s[i][j] = np.std(c)
            print(f'{N[i]}\t{g[j]}\t{t[i][j]}\t{s[i][j]}')
            file.write(f'{g[j]}\t{t[i][j]}\t{s[i][j]}\t{N[i]}\n')
        file.write(f'\n')
    file.close()