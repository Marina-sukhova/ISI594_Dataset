"""
Created on Mon Mar  7 20:15:57 2022

@author: Marina Sukhova
"""
import sys
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

# create a series with city population data
df = pd.read_csv(r'C:\Users\19176\Desktop\ISI 300\project\NYPD_Arrest_Data__Year_to_Date_ (1).csv')
df.head()
df_historical = pd.read_csv(r'C:\Users\19176\Desktop\ISI 300\project\NYPD_Arrests_Data__Historic_.csv')
df.head()

df = df.drop(df.columns[[0, 2, 3, 4, 6, 10, 14, 15, 16, 17, 18]], axis=1)
df_historical = df_historical.drop(df_historical.columns[[0, 2, 3, 4, 6, 10, 14, 15, 16, 17, 18]], axis=1)
df = df.rename(columns={'ARREST_DATE': 'Date_of_arrest', 'OFNS_DESC': 'Description_of_offense_2021','AGE_GROUP': 'Age_Group', 'LAW_CAT_CD': 'Level_of_offense_2021', 'ARREST_BORO': 'Borough_2021',
                        'PERP_RACE': 'Race_2021', 'PERP_SEX': 'Sex_2021', 'ARREST_PRECINCT': 'Precinct_2021'})

#df.info()
df_historical['ARREST_DATE'] = pd.to_datetime(df_historical['ARREST_DATE'])
df_historical['ARREST_DATE'] = df_historical['ARREST_DATE'].dt.strftime('%Y')
df_historical['ARREST_DATE'] = df_historical['ARREST_DATE'].astype(int)

# Create New DataFrame  
df_static = pd.DataFrame({
            '2009': ['', '', '', '', ''], '2010': ['', '', '', '',''], '2011': ['', '', '', '', ''],
            '2012': ['', '', '', '', ''], '2013': ['', '', '', '',''], '2014': ['', '', '', '', ''], 
            '2015': ['', '', '', '', ''], '2016': ['', '', '', '',''], '2017': ['', '', '', '', ''],
            '2018': ['', '', '', '', ''], '2019': ['', '', '','', ''], '2020': ['', '', '', '', ''],},
             index= ['K','B','Q','M','S'])     

df_static_2021 = pd.DataFrame({'2021': ['1', '2', '3', '4', '5']},index=['K','B','Q','M','S']) 


def set_value_for_2021():
    for boro in df_static_2021.index:
        df_static_2021.at[boro, '2021'] = sum(df.Borough_2021 == boro)
        
def set_value_for():
      for year in df_static.columns:
          for boro in df_static.index: 
              df_static.at[boro, year] = df_historical['ARREST_DATE'][(df_historical.ARREST_DATE == int(year))&(df_historical.ARREST_BORO  == boro)].count()


set_value_for()
set_value_for_2021()

print("The histrocal number of Arrests (2009-2020): \n", df_static, '\n', "Number of Arrests 2021 Year: \n", df_static_2021, '\n' )

new_merged_data = pd.concat([df_static, df_static_2021], axis=1, join='inner')

pd.options.display.float_format = '{:,.2f}'.format
print("The Mean of Arrests :\n",new_merged_data.mean(axis='columns'))
print('\n','\n')
print("The highest number of arrests by borough:\n",new_merged_data.max(axis='columns'))
print('\n','\n')
print("The highest number of arrests y-t-y: \n",new_merged_data.max(axis='rows'))


new_merged_data['max value'] = new_merged_data[['2009','2010','2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']].max(axis=1)

print("The summary table: \n ", new_merged_data , '\n')

sex_of_offender =df['Sex_2021']
pd.options.display.float_format = '{:,.2%}'.format
print("Sex of offender 2021:\n",sex_of_offender.value_counts())

print("Percentage ratio Race\n",df['Race_2021'].value_counts(normalize=True), '\n')
race_table = df['Race_2021'].value_counts(normalize=True)
print('\n')

pd.options.display.float_format = '{:,.2%}'.format

print("Percentage ratio Age\n", df['Age_Group'].value_counts(normalize=True), '\n')

print("Percentage ratio M vs F\n",df['Sex_2021'].value_counts(normalize=True), '\n')

df['Age_Group'].value_counts(normalize=True).plot.pie(title='The Arrest Age Composition',subplots=True, radius= 1)
plt.legend(loc='lower right', bbox_to_anchor=(1.5,.5 , .5, 1))

pie((df['Sex_2021']).value_counts(),labels=['M','F'], radius= 1,
autopct = "%0.2f%%",labeldistance=None)
plt.legend(loc='lower right', bbox_to_anchor=(2,.6 , .2, 1))

plt.pie((df['Race_2021'].value_counts()),labels=['BLACK','HISPANIC','WHITE','WHITE HISPANIC','ASIAN/PACIFIC','BLACK HISPANIC','UNKNOWN'],
autopct = "%0.2f%%",labeldistance=None,radius= 1)
df['Age_Group'].value_counts(normalize=True).plot.pie(
plt.legend(loc='lower right', bbox_to_anchor=(2,.6 , .2, 1))


df_historical.groupby('ARREST_BORO')["ARREST_PRECINCT"].nunique().plot()
plt.title('Max Arrest Number 2006-2020')
plt.ylabel("Number of arrests", fontsize = 14)
plt.xlabel("Boroughs", fontsize = 14)
plt.show()

new_merged_data['max value'].plot.bar(title='Max Arrest Number 2009-2020',fontsize =11)
plt.ylabel("Number of arrests", fontsize = 14)
plt.xlabel("Boroughs", fontsize = 14)
plt.show

df_static_2021.plot.bar(title='Max Arrest Number 2021',fontsize =11)
plt.ylabel("Number of arrests", fontsize = 14)
plt.xlabel("Boroughs", fontsize = 14)
