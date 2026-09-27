import matplotlib.pyplot as plt
import numpy as np
import random


# function
i = input("f(x) = ")


def f(x):
    return eval(i)


# derive
x = int(input("Point pour derive est: "))


# Adjust e
def derivee(x):
    keep_looping = True
    d1 = 0
    e = 0.1
    d2 = delta_en(x, e)

    while keep_looping:
        d1 = d2
        e = e - (e * 0.5)
        d2 = delta_en(x, e)
        keep_looping = abs(d2 - d1) > abs(d1) * 0.5/100

    return d2


# Get derive
def delta_en(x, e):
    xa = x-e
    xb = x+e
    ya = f(xa)
    yb = f(xb)
    d2 = (yb - ya) / (xb - xa)
    return d2


# e is epsilome
# d2 is m derive
# x is point at derivation
print("La pente est: " + str(derivee(x)))


# Function derived
def p_is(x, d2):
    p = f(x) - d2 * x
    return p


def f_derive(x, d2, p):
    y = d2 * x + p
    return y


# integrale
# Get intervale
interval = input("L'intervale est (deux abscisse separee par une virgule): ")

interval.split()
dep = int(interval[0])
arr = int(interval[-1])


# Get air
def integral(mi, ma):
    e = 0.00001
    i = mi
    a = 0
    while i < ma:
        I = i
        i = i + e
        n = ((f(I) + f(i)) * e) / 2
        a = a + n
    return a


print(integral(dep, arr))

# plot

xlist = np.arange(-10, 10.1, .1)

# plot the function
y_f = f(xlist)
plt.plot(xlist, y_f, label="Fonction f(x)")

# plot the derive
y_f_derive = f_derive(xlist, derivee(x), p_is(x, derivee(x)))
plt.plot(xlist, y_f_derive, label="Derive de f(x) en " + str(x))

# plot the integral points
x_1_pt = [dep, dep]
y_1_pt = [f(dep), 0]
plt.plot(x_1_pt, y_1_pt, marker="o", color="g", linestyle="--", label="Integrale de f(x) [" + str(dep) + ", " + str(arr)
         + "]" + "=" + str(integral(dep, arr)))


def plt_pt(x, y):
    plt.plot(x, y, marker="o", color="g", linestyle="--")


x_2_pt = [arr, arr]
y_2_pt = [f(arr), 0]
plt_pt(x_2_pt, y_2_pt)

x_3 = [dep, arr]
y_3 = [f(dep), f(arr)]
plt_pt(x_3, y_3)

x_4 = [dep, arr]
y_4 = [0, 0]
plt_pt(x_4, y_4)

print(plt.style.available)
s = input("What style do u want to use? ")
if s.lower() == "random" or "r":
    r = random.randint(0, 25)
    plt.style.use(plt.style.available[r])
else:
    plt.style.use(s)

plt.title("Graphique representant la fonction f(x) = " + i + ", \nsa derivee en " + str(x) + ", et son integrale dans ["
          + str(dep) + ", " + str(arr) + "]")
plt.legend()
plt.grid()
plt.show()
