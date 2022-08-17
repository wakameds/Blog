import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

#sample size
num_people = 500
rate_people_eat_beans = 0.95

#making dataset
np.random.seed(123)
acne_condition = np.random.uniform(size=num_people)
eat_status = np.random.choice(['eating','not_eating'],size=num_people,
                              replace=True,p=[rate_people_eat_beans,1-rate_people_eat_beans])

df = pd.DataFrame({'acne_condition':acne_condition,'eat_status':eat_status})

#boxplot
fig = sns.boxplot(data=df, x="eat_status", y="acne_condition").set(title='Boxplot with acne condition by eating status')
plt.show()

#t-test
v1 = df[df['eat_status']=='eating']['acne_condition']
v2 = df[df['eat_status']=='not_eating']['acne_condition']
res =   stats.ttest_ind(v1,v2)
print('p-value:{:.5f}'.format(res[1]))



#add color beans
colors = ['purple','brown','pink','blue','teal','salmon','red','turquoise',
          'magenta','yellow','gray','tan','cyan','green','mauve','beige',
          'lilac','black','peach','orange']

#add feature with beans color
np.random.seed(10)
beans_color = np.random.choice(colors,num_people,replace=True)
df['bean_color'] = beans_color
df.loc[df['eat_status']=='not_eating','bean_color'] = np.nan


def color_pval(eaten_color,df):
    color_check = []
    color = df['bean_color'].values

    for c in color:
        if c == eaten_color:
            color_check.append('yes')
        else:
            color_check.append('no')
    df2 = df.copy()
    df2['eaten_color'] = color_check

    # t-test
    v1 = df2[df2['eaten_color'] == 'yes']['acne_condition']
    v2 = df2[df2['eaten_color'] == 'no']['acne_condition']
    res = stats.ttest_ind(v1, v2)
    return res[1]


# store p-value by color
res_pval = {}
for c in colors:
    pval = color_pval(c,df)
    res_pval[c] = pval

# visualization
plt.figure(figsize=(8,6))
plt.scatter(res_pval.keys(),res_pval.values())
plt.hlines(0.05,0,22,linestyles='dashed',colors='gray')
plt.xticks(rotation=45)
plt.xlabel('eaten bean color')
plt.ylabel('p-value')
plt.title('p-value by eaten bean color')
plt.show()
