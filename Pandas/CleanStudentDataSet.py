import pandas as pd

data = {
    "Name": ["Imene", "Amina", "Bouchra", "Hana", "Souhila", "Imene"],
    "Age": [21, None, 22, 19, None, 21],
    "Major": ["AI", "CS", None, "AI", "CS", "AI"],
    "Grade": [17, 15, None, 14, 18, 17]
}

df = pd.DataFrame(data)
#1

print(df)
print(df.shape)
print(df.isna().sum())

#2
clean_df= df.copy()
clean_df=clean_df.drop_duplicates()
print(clean_df)

clean_df["Age"]=clean_df["Age"].fillna(clean_df["Age"].mean())
clean_df["Grade"]=clean_df["Grade"].fillna(clean_df["Grade"].mean())
clean_df["Major"]=clean_df["Major"].fillna(clean_df["Major"].mode()[0])


#3
print(clean_df.isna().sum())
print(clean_df.shape)

#4
clean_df["Passed"]= clean_df["Grade"]>=10
print(clean_df)
print(clean_df[clean_df["Major"]=="AI"])
print(clean_df.sort_values("Grade",ascending=False).iloc[0])
print(clean_df["Grade"].max())
print(clean_df["Grade"].mean())
print(clean_df.sort_values("Grade",ascending=False))

