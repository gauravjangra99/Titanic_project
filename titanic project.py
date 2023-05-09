import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option("display.max_column",100, "display.width",None)
titanic=pd.read_csv("titanic_data - Copy.csv")
print(titanic.shape)
print(titanic.info())
print(titanic.describe())
titanic.rename(columns={"Parch":"parents/child"},inplace=True)
titanic.rename(columns={"SibSp":"sibling/spouse"},inplace=True)
titanic.drop(["PassengerId","Ticket","Cabin"],axis=1,inplace=True)
print(titanic.nunique())
# define a custom function to add a new column based on conditions on col1
def add_col2(row):
    if row['Age'] <=16:
        return ("Kids")
    elif row["Age"]<=35:
        return ("Young Adults")
    elif row["Age"]<=50:
        return ("Middle Aged")
    elif row["Age"]>50:
        return ("Old Aged")
    else:
        return 'Unknown Age'

# add a new column based on conditions on col1
titanic['Age Catogery'] = titanic.apply(add_col2, axis=1)

titanic["Family"]=titanic["parents/child"] +titanic["sibling/spouse"]
print(titanic.corr())
# plt.rcParams.update({'axes.facecolor':"#ff884d"})
plt.figure(figsize=(23,12),facecolor="#ffff4d")
a=plt.axes()
s1=plt.subplot(2,2,1)
sns.countplot(x="Pclass",data=titanic,hue="Survived",
              palette=["#79ff4d", "#ffff66"])
s1.set_xlabel("Passenger Class",fontsize=12)
a.set_facecolor("red")
s2=plt.subplot(2,2,2)
sns.countplot(x="Age Catogery",data=titanic,hue="Survived",color="pink",saturation=0.8)
s2.set_xlabel("Age Catogery",fontsize=12)
a.set_facecolor("red")
s3=plt.subplot(2,2,3)
sns.countplot(x="Pclass",data=titanic,hue="Survived")
s3.set_xlabel("Family",fontsize=12)
s4=plt.subplot(2,2,4)
sns.countplot(x="Embarked",data=titanic,hue="Survived",palette=["cyan", "brown"]
              ,saturation=0.24)
s4.set_xlabel("Embarked",fontsize=12)
plt.suptitle("Titanic Survival Analysis",fontsize=40,fontweight='bold')
plt.show()
plt.savefig("titanicsurvival.png",dpi=3000)
# print(titanic)


