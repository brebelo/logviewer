import pandas as pd
import numpy as np
import streamlit as st


df = pd.read_csv('InfoLog54.csv', on_bad_lines="skip") # lis le .csv et skip les lign
df.info() #debug sur les lignes/colonnes 

def couleur(row):
    couleur_cellule = 'background-color: yellow' if row["MsgText"] == "Cutting Unit - Cut startet" else ''
    styles = [couleur_cellule] * len(row)
    return styles

def couleur(row):
    couleur_cellule = 'background-color: yellow' if row["MsgText"] == "Cutting completed" else ''
    styles = [couleur_cellule] * len(row)
    return styles

#df_reindexed = df.reindex(columns='Test')
#convertir le temps pm en am 
#
df = df.drop(columns=['Time_ms', 'MsgProc', 'StateAfter','MsgClass','Var1','Var2','Var3','Var4','Var5','Var6','Var7','Var8','PLC'])


df = df.style.apply(couleur, axis=1)


#st.dataframe(df_reindexed) # print de la dataframe df
st.dataframe(df) #print de la dataframe avec couleur, test

