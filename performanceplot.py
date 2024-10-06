import matplotlib.pyplot as plt
import pandas as pd
scores = pd.read_csv("Student_Performance.csv")
yaxis = scores.groupby('Hours Studied')['Performance Index'].mean() # Relation Between Hours Studied and Performance is very singificant and are related linearly
min = scores['Hours Studied'].min()
max = scores['Hours Studied'].max()
xaxis = list(range(min,max+1))
plt.plot(xaxis,yaxis)
plt.xlabel("Hours Studied")
plt.ylabel("Performance Index")
plt.ylim(0,100)
plt.show()
yaxis = scores.groupby('Sleep Hours')['Performance Index'].mean() # Relation between Sleep hours and Performance Index is noticable and are related linearly
min = scores['Sleep Hours'].min()
max = scores['Sleep Hours'].max()
xaxis = list(range(min,max+1))
plt.plot(xaxis,yaxis)
plt.xlabel("Sleep Hours")
plt.ylabel("Performance Index")
plt.ylim(0,100)
plt.show()
xaxis = ['Yes','No']
yaxis = scores.groupby('Extracurricular Activities')['Performance Index'].mean() # Relation between Extra Curricular Activities and Performance is negligible 
plt.plot(xaxis,yaxis)
plt.xlabel("Extracurricular activities")
plt.ylabel("Performance Index")
plt.ylim(0,100)
plt.show()
yaxis = scores.groupby('Sample Question Papers Practiced')['Performance Index'].mean() # Relation between Practice Papers solved and Performance Index is noticable and are related linearly
min = scores['Sample Question Papers Practiced'].min()
max = scores['Sample Question Papers Practiced'].max()
xaxis = list(range(min,max+1))
plt.plot(xaxis,yaxis)
plt.xlabel("Sample Question Papers Practiced")
plt.ylabel("Performance Index")
plt.ylim(0,100)
plt.show()
xaxis = scores['Performance Index'] 
yaxis = scores['Previous Scores']
plt.scatter(xaxis,yaxis)
plt.xlabel("Previous Paper Scores") # Previous paper Scores are directly related to Performance Index
plt.ylabel("Performance Index")
plt.show()

