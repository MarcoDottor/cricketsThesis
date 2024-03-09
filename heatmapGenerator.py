import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#open correct csv
if is27:
    df=pd.read_csv('results27WithSize.csv')
else:
    df=pd.read_csv('results29WithSize.csv')

# Create a pivot table for heatmap
heatmap_data = df.pivot('bigDays', 'smallDays', 'profit')[::-1]

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, cmap="coolwarm", annot=False, fmt=".2f", linewidths=.5)

# Set labels and title
plt.xlabel('NUM DAYS IN SMALL CONDOS')
plt.ylabel('NUM DAYS IN BIG CONDOS')
plt.title('Heatmap of Profit with size condos as limiting factor')

plt.savefig('heatmap29.png')

# Show the plot
plt.show()
