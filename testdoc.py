import pandas as pd
import numpy as np
import streamlit as st


fichier_csv = st.file_uploader("Merci d'ajouter votre fichier", type="csv")

if fichier_csv is not None:
    df = pd.read_csv(fichier_csv, on_bad_lines='skip')

else:
    st.info("Merci d'ajouter un fichier .CSV (logs cutting)")
    st.stop()

st.title("Lecture des cycles de coupes - Cutting Machine (A mettre en plein ecran)")

#df = pd.read_csv('InfoLog24.csv', on_bad_lines="skip") # lis le .csv et skip les lign

def colorier_lignes(row):
    if row["MsgText"] == "Cutting Unit - Cut startet":
        return ['color: #00635D; background-color: #01172F'] * len(row)
    elif row["MsgText"] == "Cutting completed":
        return ['color: #4C212A; background-color: lightgrey'] * len(row)  # ou yellow aussi
    elif row["MsgText"] == "Cutting Unit - Cut finished":
        return ['color: #4C212A; background-color: lightgrey'] * len(row)
    else:
        return [''] * len(row)

#df_reindexed = df.reindex(columns='Test')
#convertir le temps pm en am 


df['Numero de Layer'] = df['MsgText'].str.extract(r'Layer .*?(\d+)')
df['Numero de Palette'] = df['MsgText'].str.extract(r'Pallet Nr:\s*(\d+)')

#a = []
df = df.drop(columns=['Time_ms', 'MsgProc', 'StateAfter','MsgClass','Var1','Var2','Var3','Var4','Var5','Var6','Var7','Var8','MsgNumber','PLC'])
#df = df.insert(loc=4, column='Layer', value=a)

df = df.style.apply(colorier_lignes, axis=1)


#st.dataframe(df_reindexed) # print de la dataframe df
st.dataframe(df) #print de la dataframe avec couleur, test



