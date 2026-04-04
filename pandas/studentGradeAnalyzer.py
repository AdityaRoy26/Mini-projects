# importing th basic libraries 
import numpy as np
import pandas as pd

# taking the raw data
students=["Aditya","Prakitesh","Harsh","Hirok","Amit"] 
maths = [88,97,45,60,10]
science= [66,46,78,98,23]
english= [56,67,89,45,53]

# making it into tabluar form
df=pd.DataFrame({
    "Students": students,
    "Maths" : maths,
    "Science" : science,
    "English" : english
})

# calculating the marks of each subject
scores =np.array([maths,
                  science,
                  english])
df["Average"]=np.mean(scores ,axis=0).round(1)

# creating a function for grading system uk , just simple if,else
def grade(avg):
    if avg>= 90: return "A"
    elif avg>=80: return "B"
    elif avg>=70: return "C"
    else: return "D"

# adding a new col inside the df while calling the grade func and putting
# "A" , "B" , "C" according to their avg marks 
df["Grade"]=df["Average"].apply(grade)

# now simply just printing the basic statements and the functions 
print(df.to_string(index=False))
print("\n--- CLASS PERFORMANCE--- ")
print(f"Highest Performance : {df['Average'].max()}")
print(f"Class Avg : {df['Average'].mean():.1f}")
top = df.loc[df["Average"].idxmax(), "Students"]
print(f"Topper Student :  {top}")

