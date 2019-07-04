import numpy as np
import pandas as pd
from pandas.plotting import parallel_coordinates
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
pd.set_option('display.max_columns', None)

### pokemon generation 1-7 ####
df = pd.read_csv('pokemon.csv')



### Getting rid of the mega evolutions and other buffs some pokemon get ###
df = df[df.Name.str.contains("Black") == False]
df = df[df.Name.str.contains("White") == False]
df = df[df.Name.str.contains("Mega") == False]
df = df[df.Name.str.contains("Primal") == False]
df = df[df.Name.str.contains("%") == False]
df = df[df.Name.str.contains("Forme") == False]
df = df[df.Name.str.contains("Confined") == False]


### pokemon generation 1-6 that have a higher total than 600 but aren't legendary ###
df_non_leg_strong = df[(df['Total'] >= 600) & (df['Legendary'] == False)]
### bar chart of secondary typing ### 
df_non_leg_strong['Type 2'].value_counts().plot.bar()
print(df_non_leg_strong)



### legendary pokemon generation 1-6 ###
df_leg = df[df['Legendary'] == True]
### bar chart of secondary typing ### 
df_leg['Type 2'].value_counts().plot.bar()
print(df_leg)




### averages of each column stat ###
avgTotal = df['Total'].sum() / len(df)
avgHP = df['HP'].sum() / len(df)
avgAttack = df['Attack'].sum() / len(df)
avgDefense = df['Defense'].sum() / len(df)
avgSpAtk = df['Sp. Atk'].sum() / len(df)
avgSpDef = df['Sp. Def'].sum() / len(df)
avgSpeed = df['Speed'].sum() / len(df)



print("average speed: " + str(avgTotal))
print("average HP: " + str(avgHP))
print("average Attack: " + str(avgAttack))
print("average Defense: " + str(avgDefense))
print("average Sp. Atk: " + str(avgSpAtk))
print("average Sp. Def: " + str(avgSpDef))
print("average speed: " + str(avgSpeed))


### viewing different stats for the pokemon ###
df.drop(['#','Total','Generation'], 1, inplace=False).describe().loc[['mean', 'std', 'min','25%','50%','75%','max']].plot.bar()


print("Pokemon with highest totals:")
print(df[df['Total'] >= 675])

print("Best attacking pokemon:")
print(df[df['Attack'] > 160])

print("Best defensive pokemon:")
print(df[df['Defense'] > 200])

print("Best special attacking pokemon:")
print(df[df['Sp. Atk'] > 150])

print("Best special defensive pokemon:")
print(df[df['Sp. Def'] > 150])

print("Highest Hit Points pokemon:")
print(df[df['HP'] >= 159])

print("Fastest pokemon:")
print(df[df['Speed'] >  130])

### dragon type is my favourite type so just looking at them ###
df_dragon = df[(df['Type 1'] == 'dragon') | (df['Type 2'] == 'dragon')]
df_dragon['Generation'].value_counts().plot.bar()
print(df_dragon)
plt.show()
