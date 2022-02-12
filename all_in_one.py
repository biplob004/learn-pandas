## Do not run this file, this file is for understanding Pandas library. ::
:#: This file is under construction #

import pandas as pd

# creating dataframe
df = pd.read_csv('path_to_folder/file_name.csv') 
df = pd.read_csv('path_to_folder/file_name.csv', index_col='column_name')

# get print of few lines of data
df.head() 
df.tail() 

# get all columns names
df.columns

# get rows and columns count as (rows, columns)
df.shape 

# more information about data
df.info()

# get values using iloc
df.iloc[0]
df.iloc[0:4] 
df.iloc[[1,2,3,4]]
df.iloc[[1,2,3],[1,2]] # df.iloc[[rows_idx_list], [columns_idx_list]]

# get values using loc
df.loc[0]
df.loc[0:4]
df.loc[[1,2,3,4]]
df.loc[[1,2,3], ['email', 'name']]
df.loc[[1,2,3], 'email':'home']

# access single column, return Series type
df['column_1_name']
df['column_1_name'].value_counts() # output repeat value count

#access multiple column, return DataFrame type
df[['column_1_name', 'column_2_name', 'column_3_name']]


##### Index 
# change index to email # still iloc can use here
df.set_index('email', inplace=true)
df.index
df.loc['example@gmail.com', 'first_name']
df.reset_index(inplace=true)

##### Filter
flt = df.loc[:,'cars'] == 'BMW'
flt = df.loc[:,'cars'].isin(['None', 'BMW'])
flt = df.loc['title'].str.contains('good', na=False)

df.loc[flt] # apply filter
df.loc[~flt] # opposite with ~
df.loc[flt, 'cars'] # shortening to specified columns

##### Update columns names
df.columns = [x.lower() for x in df.columns]
df.columns = df.columns.str.replace(' ','_')
df.rename(columns={'cars':'car'}, inplace=True)
df.columns

###### update rows
# apply, map, applymap, replace
df['email'].apply(len)
def update_email(email):
  return email.upper()

df['email'].apply(update_email) # custom function
df['email'].apply(lamda x: x.upper()) # lamda function
df['email'] = df['email'].apply(lamda x: x.upper())

df['email'].apply(len)
df.apply(len)
df.apply(len, axis= 'columns')

len(df['email])
df.apply(pd.Series.min)
df.apply(lambda x: x.min())

df.applymap(len) # apply to dataframe
df.applymap(str.lower)

df['first'].map({'Corey':'Chris', 'Jane':'Mary'}) # keeps NAN when value not defined
df['first'].replace({'Corey':'Chris', 'Jane':'Mary'}) # no NAN

       

#### sorting data
df.sort_values(by=['first', 'last'], ascending=False)



