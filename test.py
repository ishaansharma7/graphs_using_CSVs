import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('prices.csv')

# All Brands
x = df['Model']
y = df['Price']

# Specified Brands
# specified = df.loc[df['Company'] == 'Samsung']
# x = specified['Model']
# y = specified['Price']

# Bar chart
# plt.xlabel('Model', fontsize=18)
# plt.ylabel('Price($)', fontsize=16)
# plt.bar(x, y)

# Pie chart
plt.pie(y, labels=x, radius=1.2,autopct='%0.01f%%', shadow=True, explode=[.05,.2,.05,.2,.05,.2,.05])

# Line Graph
# plt.xlabel('Model', fontsize=18)
# plt.ylabel('Price($)', fontsize=16)
# plt.scatter(x, y)
# plt.plot(x, y)

plt.show()