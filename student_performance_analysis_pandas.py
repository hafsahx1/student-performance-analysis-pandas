import pandas as pd 



# Loading Dataset
df = pd.read_csv("students.csv")
print(df.columns)

# Showing the First Five rows 
print("\nFirst Five Rows: ")
print(df.head())

# Showing Last Five Rows
print("\nLast Five Rows: ")
print(df.tail())

#Showing Information About The Dataset
print("\nInformation About Dataset: ")
print(df.info())

# Summing all the marks of all Subjects
print("\nSum Of All The Marks: ")
print(df[["Math", "Science", "English"]].sum())
# Finding Average Marks Of Each Student
print("\nAverage Marks Of Each Student:")
df["Average"]=df[["Math","Science","English"]].mean(axis=1)
print(df)

# Top Perfoming Student
top_student = df.loc[df["Average"].idxmax()]
print("\nStudent With The High Performance: ")
print(top_student)

# Lowest Performing Student
lowest_student = df.loc[df["Average"].idxmin()]
print("\nstudent WITH the Low Performance: ")
print(lowest_student)

# Students With An Average Above 80
print("\nStudents With Marks Above 80: ")
print(df[df["Average"]>80])

#  Grade Column
def grade(avg):
    if avg >= 90 :
        return "A"
    elif avg >=80 :
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "D"
df["Grade"]=df["Average"].apply(grade)

# Student From Highest To Lowest Marks
df = df.sort_values(by="Average", ascending=False)

print("\nSorted by Average Marks:")
print(df)