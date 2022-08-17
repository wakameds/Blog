import numpy as np
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

#dataset
np.random.seed(123)
X = np.arange(1,101,1)
err = np.random.poisson(4, size=100)
Y = np.round(np.exp(0.03*X)+err,0)
df = pd.DataFrame({'Day':X,'Sold Product':Y})


#GLM_Poisson
X = df.drop(['Sold Product'],axis=1)
Y = df['Sold Product']

#link
link = sm.families.links.log
#probability distribution
family = sm.families.Poisson(link)
#add constant to explanatry variable
X_const = sm.add_constant(X)

#model
glm_poisson = sm.GLM(endog=Y,exog=X_const, family=family)
#inference
res = glm_poisson.fit()
#output
print(res.summary())


#Visualize
#Y distribution
fig, axs = plt.subplots(1,2,figsize=(10,5))
sns.histplot(Y,stat='probability',ax=axs[0])

#Scatter plot
axs[1].plot(X,Y,'.')
axs[1].plot(X,res.mu,color='gray',linestyle='--')
axs[1].set_xlabel(r"$\mathbf{X}$: Day")
axs[1].set_ylabel(r"$\mathbf{Y}$ :Sold Product")
axs[1].text(20,20,r"$\mu = exp({:.4f}+{:.4f}X)$".format(res.params[0],res.params[1]),size=10)
plt.show()

