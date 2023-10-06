import matplotlib.pyplot as plt
year=[1950,1970,1990,2010]
pop=[2.15,3.14,9,12]


#used When you have two variables with a correlation
plt.plot(year,pop)
plt.title("word population projections")
plt.xlabel("years")
plt.ylabel("population")
plt.yticks([0,2,4,6,8,10,12,14],['0','2B','4B','6B','8B','10B','12B','14B'])
plt.show()
plt.clf()

#used when we two variable have correlation
plt.scatter(year,pop)
plt.xscale('log')
plt.xlabel("year")
plt.ylabel("population")
plt.show()