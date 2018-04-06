import matplotlib.pyplot as plt
 
# Data to plot
labels = 'KFC', 'Pizza Hut', 'Mc.Donalds', 'Dominos'
sizes = [20, 35, 30, 15]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=False, startangle=140)
 
plt.axis('equal')
plt.show()