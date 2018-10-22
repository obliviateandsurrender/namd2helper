import matplotlib.pyplot as plt
f = open('da_us.psf',"r")
a = f.read().split('#')[1]
a = a.split('\n')[1:-1]
x = []
y = []
for i in a:
    #print(i)
    b = i.split('\t')
    #print(b[0], b[1])
    x.append(float(b[0]))
    y.append(float(b[1]))
#print(a)
print(x)
print(y)
plt.plot(x,y)
plt.xlabel("Distance (A)")
plt.ylabel("Free Energy (kcal/mol)")
#plt.xlim(auto=True)
plt.show()