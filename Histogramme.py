
import matplotlib.pyplot as plt
import random

values=[]
for i in range(0,10):
    values.append(random.randint(0,100))
    print(values[i])

plt.hist(values,bins=3)
plt.show()