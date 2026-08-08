##################################################################################################################################################
#                                                                                                                                                #
#                                                           Author : Brandon Rebelo                                                              #
#                                                                                                                                                #
##################################################################################################################################################

import pandas as pd
import streamlit as st

# Gestion du fichier csv, puis importation comme reference dans df
fichier_csv = st.file_uploader("Merci d'ajouter votre fichier", type="csv")
if fichier_csv is not None:
    df = pd.read_csv(fichier_csv, on_bad_lines='skip')

else:
    st.info("Merci d'ajouter un fichier .CSV (logs cutting)")
    st.stop()

# Titre
st.title("Lecture des cycles de coupes - Cutting Machine (A mettre en plein ecran)")

# Structure et mise en forme des colonnes pas necessaires
df = df.drop(columns=['Time_ms', 'MsgProc', 'StateAfter','MsgClass','Var1','Var2','Var3','Var4','Var5','Var6','Var7','Var8','MsgNumber','PLC'])


# Colores les lignes souhaitées
def colorier_lignes(row):
    if row["MsgText"] == "Cutting Unit - Cut startet":
        return ['color: #00635D; background-color: #01172F'] * len(row)
    elif row["MsgText"] == "Cutting completed":
        return ['color: #4C212A; background-color: lightgrey'] * len(row)  # ou yellow aussi
    elif row["MsgText"] == "Cutting Unit - Cut finished":
        return ['color: #4C212A; background-color: lightgrey'] * len(row)
    else:
        return [''] * len(row)

# Rajout de la colone Layer et Palett voulu
df['Numero de Layer'] = df['MsgText'].str.extract(r'Layer .*?(\d+)')
df['Numero de Palette'] = df['MsgText'].str.extract(r'Pallet Nr:\s*(\d+)')

df = df.style.apply(colorier_lignes, axis=1)



# Print de la dataframe finale
st.dataframe(df) 



