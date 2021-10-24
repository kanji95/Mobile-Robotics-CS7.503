from sys import argv, exit
import math
import numpy as np
import matplotlib.pyplot as plt


def readTxt(filename):
    f = open(filename, 'r')
    A = f.readlines()
    f.close()

    X = []
    Y = []
    THETA = []

    for i, line in enumerate(A):
        if(i % 1 == 0):
            (x, y, theta) = line.split()
            X.append(float(x))
            Y.append(float(y))
            THETA.append(math.radians(float(theta.rstrip('\n'))))

    return X, Y, THETA


def readG2o(fileName):
    f = open(fileName, 'r')
    A = f.readlines()
    f.close()

    X = []
    Y = []
    THETA = []

    for line in A:
        if "VERTEX_SE2" in line:
            (ver, ind, x, y, theta) = line.split()
            X.append(float(x))
            Y.append(float(y))
            THETA.append(float(theta.rstrip('\n')))

    X_temp = X
    Y_temp = Y
    X = [y for y in Y_temp]
    Y = [-x for x in X_temp]

    return (X, Y, THETA)


def convert(X, Y, THETA):
    A = np.zeros((len(X), 12))

    for i in range(len(X)):
        T = np.identity(4)
        T[0, 3] = X[i]
        T[1, 3] = Y[i]
        R = np.array([[math.cos(THETA[i]), -math.sin(THETA[i]), 0], [math.sin(THETA[i]), math.cos(THETA[i]), 0], [0, 0, 1]])
        T[0:3, 0:3] = R
        
        A[i] = T[0:3, :].reshape(1, 12)
        
    return A


def draw(X, Y, THETA):
    ax = plt.subplot(111)
    ax.plot(X, Y, 'ro')
    ax.plot(X, Y, 'k-')

    plt.show()


if __name__ == '__main__':
    (X, Y, THETA) = readG2o(argv[1])
    # (X, Y, THETA) = readTxt(argv[1])
    file_name = argv[2]
    
    draw(X, Y, THETA)

    A = convert(X, Y, THETA)

    np.savetxt(file_name, A, delimiter=' ')
    print(f"saved '{file_name}' from '{argv[1]}'")
