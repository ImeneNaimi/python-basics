import pandas as pd
import numpy as np

grades=pd.Series([17,15,12,19,18])
print(grades)

print(grades[0])
print(grades[1])
print(grades[1:4])

#DataFrame

data={
    "Name": ["Imene","Amina","Bouchra"],
    "Age": [21,22,23],
    "Major":["AI","CS","English"],
    "Grade": [17,15,19]
}
df=pd.DataFrame(data)
print(df)
#par défaut, Pandas affiche les 5 premières lignes.
print(df.head())
print(df.head(2))
#les 5 dernières lignes.
print(df.tail())

print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()
print(df["Name"])#Sélectionner une colonne
print(df[["Name", "Grade"]])#ou plusieurs

#statistiques

print(df["Grade"].mean())
print(df["Grade"].max())
print(df["Grade"].min())
print(df["Grade"].sum())

print(df["Grade"].describe())

#Exercies

#1
ages=pd.Series([18,20,21,19,22])
print(ages)
print(ages[0])
print(ages[4])
print(len(ages))

#2

data={
    "Name": ["Imene","Amina","Bouchra","Hana"],
    "Age": [21,20,22,19],
    "Grade":[17,15,19,14]
}
df=pd.DataFrame(data)
print(df)

#3
print(df.head(2))
print(df.columns)
print(df.shape)
print(df.dtypes)

#4
print(df["Grade"])
print(df["Grade"].max())
print(df["Grade"].min())

#challenge

df["Passed"]= df["Grade"]>=10
print(df)

#filtrage et sélection

print(df[df["Grade"] >=15])
print(df[(df["Grade"] >=15) & (df["Age"]>=21)])
print(df[(df["Grade"] >=15) | (df["Age"]<=20)])

print(df[df["Name"]=="Imene"])
print(df[df["Name"].str.startswith("B")])
print(df[df["Name"].str.contains("a")])

#loc[]sélectionner des lignes et colonnes par leurs labels.
df.loc[0]
df.loc[0,"Name"]
df.loc[0:2]
#iloc[]fonctionne avec les positions numériques, comme les index classiques de Python.
df.iloc[0]#premiere ligne
df.iloc[0,2]#premiere ligne, 2eme colonne
df.iloc[0:2]#ligne 0 et 1

#Trier les données

print(df.sort_values("Grade"))
print(df.sort_values("Grade", ascending=False))
print(df.sort_values("Age"))

data = {
    "Name": ["Imene", "Amina", "Bouchra", "Hana"],
    "Major": ["AI", "CS", "AI", "AI"]
}

df = pd.DataFrame(data)
print(df["Major".value_counts()])

#Exercices
data = {
    "Name": ["Imene", "Amina", "Bouchra", "Hana"],
    "Age": [21, 20, 22, 19],
    "Grade": [17, 15, 19, 14]
}

df = pd.DataFrame(data)
#1
print(df[df["Grade"]>=16])
#2
print(df[(df["Grade"]>=15) & (df["Age"]>=21)])
#3
print(df[(df["Grade"]>=18) | (df["Age"]<20)])
#4
print(df[df["Grade"]>=15][["Name","Grade"]])
#5
print(df.sort_values("Grade",ascending=False).iloc[0])
#challenge
data = {
    "Name": ["Imene", "Amina", "Bouchra", "Hana", "Souhila", "Yasmine"],
    "Major": ["AI", "CS", "AI", "CS", "AI", "AI"],
    "Grade": [17, 15, 19, 12, 18, 14]
}

df = pd.DataFrame(data)
print((df["Major"]=="AI").sum())

print(df[(df["Major"]=="AI") & (df["Grade"]>=16)])

print(df["Major"].value_counts())

print(df.sort_values("Grade",ascending=False))

print(df[df["Major"]=="AI"]["Grade"].mean())

#Pandas — loc et iloc


data = {
    "Name": ["Imene", "Amina", "Bouchra", "Hana"],
    "Age": [21, 20, 22, 19],
    "Grade": [17, 15, 19, 14]
}

df = pd.DataFrame(data)

print(df.iloc[0])#ligne1
print(df.iloc[2])#ligne3
print(df.iloc[0,2])#ligne 0, colonne 2

print(df.loc[0,"Name"])
print(df.loc[2,"Grade"])

#Modifier une valeur

df.loc[0,"Grade"]=18
print(df)
df.loc[df["Grade"]<15, "Grade"]+=1 #df.loc[condition, "colonne"] = nouvelle_valeur
print(df)

#Ajouter une colonne

df["Passed"]=df["Grade"]>=10
df["Double_Grade"] = df["Grade"] * 2
df["GPA"]=(df["Grade"]*4)/20

#Supprimer une colonne drop()

df=df.drop("Double_Grade",axis=1)

#Supprimer une ligne 

df=df.drop(2,axis=0)

#Exercices
data = {
    "Name": ["Imene", "Amina", "Bouchra", "Hana"],
    "Age": [21, 20, 22, 19],
    "Grade": [17, 15, 19, 14]
}

df = pd.DataFrame(data)

#1
print(df.iloc[2,0])

#2
print(df.loc[1,"Grade"])

#3
df.loc[0,"Grade"]+=1
print(df)

#4
df["Passed"]=df["Grade"]>=10

#5
df["Grade_2"] = df["Grade"] * 2

#6
df.loc[df["Grade"]<16,"Grade"]+=2

print(df)

#challenge

df=df.drop("Grade_2",axis=1)
df=df.drop(3,axis=0)
print(df)


#Pandas — Les valeurs manquantes (NaN)

data = {
    "Name": ["Imene", "Amina", "Bouchra", "Hana"],
    "Age": [21, np.nan, 22, 19],
    "Grade": [17, 15, np.nan, 14]
}

df = pd.DataFrame(data)

print(df)

#Détecter les valeurs manquantes : isna()
print(df.isna())

#Compter les valeurs manquantes
print(df.isna().sum())

#Supprimer les valeurs manquantes : dropna()
df=df.dropna()

#Remplacer les valeurs manquantes : fillna()
df=df.fillna(0)
#Remplacer par la moyenne
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Grade"]=df["Garde"].fillna(df["Grade"].mean())
print(df)

#Remplacer une valeur texte
df["Name"]= df["Name"].fillna("Unknown")

#Les valeurs les plus fréquentes : mode()
df["Major"]=df["Major"].fillna(df["Major"].mode()[0])

#Exercices

data = {
    "Name": ["Imene", "Amina", "Bouchra", "Hana", None],
    "Age": [21, None, 22, None, 20],
    "Major": ["AI", "CS", None, "AI", "AI"],
    "Grade": [17, 15, None, 14, 18]
}

df = pd.DataFrame(data)

#1
print(df)
print(df.isna())

#2
print(df.isna().sum())

#3
clean_df=df.dropna()
print(clean_df)

#4
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Grade"]=df["Grade"].fillna(df["Grade"].mean())
df["Name"]= df["Name"].fillna("Unknown")
df["Major"]=df["Major"].fillna(df["Major"].mode()[0])

