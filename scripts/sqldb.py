import pandas as pd
import mysql.connector
import seaborn as sns
import matplotlib.pyplot as plt

#connect to mysql
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="hr_analytics"
)

#Query and load it into a dataframe
query="select department,ROUND(AVG(MonthlyIncome),2) as avg_monthlyincome from employees group by department"
df_income=pd.read_sql(query,conn)

# print(df_income)
# plot
plt.figure(figsize=(10,6))
sns.barplot(data=df_income,x='department',y='avg_monthlyincome',palette="viridis")
plt.title("Average Monthly Income by Department")
plt.xticks(rotation=45)

plt.show()


conn.close()