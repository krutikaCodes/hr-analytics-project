from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load the data
df=pd.read_csv('./data/WA_Fn-UseC_-HR-Employee-Attrition.csv')

#encode categorical columns
label_encoder = LabelEncoder()
df['Attrition'] = label_encoder.fit_transform(df['Attrition'])
df['Department'] = label_encoder.fit_transform(df['Department'])

#selecting features (excluding non-numeric columns  for now)
features = ['Age', 'MonthlyIncome', 'TotalWorkingYears', 'YearsAtCompany', 'JobSatisfaction', 'Department']
X = df[features]   #features
y = df['Attrition'] #target variable (Attrition)


#split the data into tarin and test  set (80% train , 20% test)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#build and train Random Forest model
model = RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,y_train)

#predict on test data
y_pred = model.predict(X_test)

#evaluate the model
print("Classification Report:",classification_report(y_test,y_pred))
print("Confusion Matrix:",confusion_matrix(y_test,y_pred))

#get feature importance 
importances =model.feature_importances_

#plot feature importances
plt.figure(figsize=(10,6))
sns.barplot(x=importances,y=features)
plt.title("Feature Importance for Attrition Prediction")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.tight_layout()
plt.show()