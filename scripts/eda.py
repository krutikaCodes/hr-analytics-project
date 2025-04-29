import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#set the seaborn theme
sns.set(style="whitegrid") 
#load the data
df=pd.read_csv('./data/WA_Fn-UseC_-HR-Employee-Attrition.csv')

#basic info of data
print("Shape:",df.shape)
print(df.head())

#checking if any missing values
print("\nMissing Values:\n",df.isnull().sum())
print("\nData Types:\n",df.dtypes)

#filling missing values in JobSatisfaction column with its mean value
df['JobSatisfaction'] = df['JobSatisfaction'].fillna(df["JobSatisfaction"].mean())

#plot attrition distrubution
sns.countplot(data=df,x="Attrition")
plt.title("Attrition Count")
plt.show()

#attrition by department
plt.figure(figsize=[10,6])
sns.countplot(x='Department',hue="Attrition",data=df,palette="pastel")
plt.title("Attrition by Department")
plt.show()
#attrition by JobRole
plt.figure(figsize=[18,6])
sns.countplot(x='JobRole',hue="Attrition",data=df,palette="Set3")
plt.title("Attrition by JobRole")
plt.show()
#Age Distribution by attrition status
plt.figure(figsize=(8,6))
sns.boxplot(x="Attrition",y="Age",data=df)
plt.title("Age vs Attrition")
plt.show()

# Correlation heatmap for numeric variables
corr = df[['Age', 'MonthlyIncome', 'YearsAtCompany', 'JobSatisfaction', 'NumCompaniesWorked']].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Correlation Heatmap of Key Numeric Variables")
plt.show()
# Age distribution by attrition status
plt.figure(figsize=(8, 6))
sns.histplot(df, x="Age", hue="Attrition", multiple="stack", kde=True, palette="Set1")
plt.title("Age Distribution by Attrition Status")
plt.show()
