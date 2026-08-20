##################################################################################################################################################
#                                                                                                                                                #
#                                                           Author : Brandon Rebelo                                                              #
#                                                                                                                                                #
##################################################################################################################################################

import csv
import pandas as pd
import streamlit as st


fichier_csv = st.file_uploader(
    "Merci d'ajouter votre fichier",
    type="csv"
)

if fichier_csv is not None:

    # Lecture brute du fichier
    contenu = fichier_csv.read().decode("utf-8-sig")
    lecteur = csv.reader(contenu.splitlines())

    # On récupère le header
    header = next(lecteur)

    donnees = []

    for ligne in lecteur:

        # Ignore la ligne technique $RT_COUNT$
        if not ligne or ligne[0] == "$RT_COUNT$":
            continue

        # CAS 1 : format normal -> 16 colonnes
        if len(ligne) == 16:
            donnees.append(ligne)

        # CAS 2 : Time_ms séparé en 2 colonnes -> 17 colonnes
        elif len(ligne) == 17:

            nouvelle_ligne = [
                ligne[0] + "." + ligne[1],  # Recompose Time_ms
                *ligne[2:]
            ]

            donnees.append(nouvelle_ligne)

    # Création du dataframe avec le vrai header
    df = pd.DataFrame(donnees, columns=header)

else:
    st.info("Merci d'ajouter un fichier .CSV (logs cutting)")
    st.stop()

# Titre
st.title("Lecture des cycles de coupes - Cutting Machine (A mettre en plein ecran)")

# Structure et mise en forme des colonnes pas necessaires
df = df.drop(columns=[
    'Time_ms',
    'MsgProc',
    'StateAfter',
    'MsgClass',
    'MsgNumber',
    'Var1',
    'Var2',
    'Var3',
    'Var4',
    'Var5',
    'Var6',
    'Var7',
    'Var8',
    'PLC'
])

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
df['Numero de Layer'] = df['MsgText'].str.extract(
    r'Layer\s+(?:Nr\.?|Number)?\s*:?\s*(\d+)',
    expand=False
)

df['Numero de Palette'] = df['MsgText'].str.extract(
    r'Pallet\s+(?:Nr\.?|Number)?\s*:?\s*(\d+)',
    expand=False
)

df = df.style.apply(colorier_lignes, axis=1)



# Print de la dataframe finale
st.dataframe(df) 



