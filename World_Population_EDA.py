import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Setting the format float numbers are going to be shown in here (2 decimals)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

#calling the world population csv file from my directory
df = pd.read_csv(r"F:\Business Analytics\Knowledge\Py\Exploratory Data Analysis\World Population\world_population.csv")

#sorting the data frame based of the last year of the report (2022)
df = df.sort_values(by = '2022 Population', ascending= False)

#Since Pycharm needs to separate str from numbers for the corr() to work
#I have to manually take only the columns with the numbers in them
cor = df[['2022 Population',
       '2020 Population', '2015 Population', '2010 Population',
       '2000 Population', '1990 Population', '1980 Population',
       '1970 Population', 'Area (km²)', 'Density (per km²)', 'Growth Rate',
       'World Population Percentage']].corr()

#the heatmap of the correlation between different numerical attributes
sns.heatmap(cor , annot= True)
#making the plot bigger so annotations are more readable
plt.rcParams['figure.figsize'] = (20,10)
plt.show()

#now Let's take a look on population through the years based on different
#continents

#group by continents
df2 = df[['Continent', '1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].groupby('Continent').mean()

#as we can see Asian has always been the most
#populated continents. Its population growth rate
#actually increased from 1990-2000, thankls China and Indai :|
df2 = df2.transpose()
df2.plot()
plt.show()


#Since this is a world population, obviously we're having lots of outliers.
#Let's take a look at these outliers in our data
df[['1970 Population','1980 Population', '1990 Population',
    '2000 Population','2010 Population', '2015 Population',
    '2020 Population','2022 Population']].boxplot()
plt.show()

#Although Asia has the highest share of the world's population
#initial exploratory analysis on the world population cencus data
#shows from 1970-2022, china and India are the countries with
#highest contribution to the world's population. They have
#almost 35% of the world's population!

