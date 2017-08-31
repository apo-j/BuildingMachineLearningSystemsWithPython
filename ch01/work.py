import scipy as sp
import os
from matplotlib import pyplot as plt

data = sp.genfromtxt(os.path.join(os.getcwd(), 'data\\web_traffic.tsv') , delimiter='\t')

# preprocessing
x = data[:, 0]
y = data[:, 1]
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

# plot the data
plt.scatter(x, y, c='r' ,s=10)
plt.xlabel('Time/Hours')
plt.ylabel('Requests')
plt.title('Number of requests per hour')
plt.xticks([w*7*24 for w in range(10)], ['week %i' % w for w in range(10)])
plt.grid(True)
plt.autoscale(tight=True)

# choosing model

# define the error function
def error(f, x, y):
    return sp.sum((f(x) - y)**2)

# simple straighe line

def plot_models():
    plt.scatter(x, y, c='r', s=10)
    plt.xlabel('Time/Hours')
    plt.ylabel('Requests')
    plt.title('Number of requests per hour')
    plt.xticks([w * 7 * 24 for w in range(10)], ['week %i' % w for w in range(10)])
    plt.grid(True)
    plt.autoscale(tight=True)
    fx = sp.linspace(0, x[-1], 1000)
    legends = []
    errors = []
    for i in [1, 2, 3, 10, 100]:
        f = sp.poly1d(sp.polyfit(x, y, i))
        plt.plot(fx, f(fx), linewidth=2)
        errors.append(error(f, x, y))
        legends.append(f.order)

    plt.legend(["d=%i" % o for o in legends], loc='upper left')
    return errors

plt.show()

inflection = 3.5*7*24

xa = x[:inflection]
ya = y[:inflection]

xb = x[inflection:]
yb = y[inflection:]

f1 = sp.poly1d(sp.polyfit(xa, ya, 1))
f2 = sp.poly1d(sp.polyfit(xb, yb, 1))

plt.scatter(x, y, c='r', s=10)
plt.xlabel('Time/Hours')
plt.ylabel('Requests')
plt.title('Number of requests per hour')
plt.xticks([w * 7 * 24 for w in range(10)], ['week %i' % w for w in range(10)])
plt.grid(True)
plt.autoscale(tight=True)

fx = sp.linspace(0, x[-1], 1000)
plt.plot(fx, f1(fx), linewidth=2)
plt.plot(fx, f2(fx), linewidth=2)



