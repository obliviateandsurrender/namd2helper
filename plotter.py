import matplotlib.pyplot as plt
f = open('da_us.psf',"r")
a = f.read().split('#')[1]
a = a.split('\n')[1:-1]
x = []
y = []
for i in a:
    b = i.split('\t')
    x.append(float(b[0]))
    y.append(float(b[1]))
plt.plot(x,y)
plt.xlabel("Distance (A)")
plt.ylabel("Free Energy (kcal/mol)")
plt.show()