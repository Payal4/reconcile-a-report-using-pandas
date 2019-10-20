# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df = pd.read_csv(path)

df['state'] = df['state'].str.lower()

df['total'] = df['Jan'] + df['Feb'] + df['Mar']
print(df.head())
sum_row = df[['Jan','Feb','Mar','total']].sum()
df_final= df.append(sum_row,ignore_index=True)
df_final
# Code ends here


# --------------
import requests

# Code starts here
url = "https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations"
response = requests.get(url)
df1 = pd.read_html(response.content)[0]
#df1 = df1.iloc[11:,:]
#df1 = df1.rename(columns=df1.iloc[0,:]).iloc[1:,:]
df1 = df1[11:]
df1.columns = df1.iloc[0].values
df1 = df1.iloc[1:]
df1["United States of America"] = df1["United States of America"].apply(lambda x: x.replace(" ",""))

df1



# Code ends here


# --------------

# Code starts here
#scraped = pd.read_csv("../data/scraped.csv")
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)
mapping = dict(zip(df1['United States of America'],df1['US']))
df_final.insert(6,'abbr',np.nan)
df_final['abbr']=df_final['state'].map(mapping)
df_final


# Code ends here


# --------------
# Code stars here
df_mississipi = df_final[df_final['state'] == 'mississipi'].replace(np.nan,"MS")
df_tenessee = df_final[df_final['state'] == 'tenessee'].replace(np.nan,"TN")
df_final.replace(df_final.iloc[6],df_mississipi, inplace=True)
df_final.replace(df_final.iloc[10],df_tenessee, inplace=True)
df_final
# Code ends here


# --------------
# Code starts here
df_sub = df_final[['abbr','Jan','Feb','Mar','total']].groupby("abbr").sum()
formatted_df = df_sub.applymap(lambda x:"${:,.0f}".format(x))
formatted_df
# Code ends here


# --------------
# Code starts here
sum_row = df[['Jan','Feb','Mar','total']].sum()
df_sub_sum = sum_row.to_frame().transpose()
df_sub_sum = df_sub_sum.applymap(lambda x:"${:,.0f}".format(x))

final_table = formatted_df.append(df_sub_sum)
final_table.rename(index={0: "Total"},inplace=True)
print(final_table)
# Code ends here


# --------------
# Code starts here
import matplotlib.pyplot as plt

df_sub['total']
plt.pie(df_sub['total'])
plt.show()

# Code ends here


