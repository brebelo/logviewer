# Analyseur de logs machine industrielle

Outil d'analyse de logs CSV issus de systèmes PLC/HMI industriels : extraction 
automatique des opérations, calcul des durées (en developpement), détection des transitions d'état, 
via une interface web interactive.

![screenshot]("1.png")
![screenshot]("2.png")


## Stack
- Python avec pandas
- Streamlit
- Html
- Markdown

## Contexte

En environnement industriel, les logs machine (format CSV horodaté) contiennent 
des centaines d'événements bruts, difficiles à exploiter manuellement par lecture visuelle sur Excel. 
Ariane transforme ces logs en tableaux de bord exploitables : durée des opérations, 
temps d'arrêt, anomalies.

## Fonctionnalités

- 📂 Upload de fichier CSV directement depuis l'interface
- 🔍 Extraction automatique des opérations (paires start/finish)
- 🎨 Mise en surbrillance conditionnelle des lignes selon leur statut
- 📊 [ajoute ce que tu as / comptes ajouter]

## 🛠️ Stack technique

- Python 3.x
- pandas — traitement des données
- Streamlit — interface web interactive

## 🚀 Installation

\`\`\`bash
git clone [https://github.com/ton-pseudo/ariane.git](https://github.com/brebelo/logviewer)
cd logviewer
pip install -r requirements.txt
streamlit run main.py
\`\`\`

## Format de retour attendu

<img width="437" height="81" alt="image" src="https://github.com/user-attachments/assets/a008a652-0082-4e64-bbd4-363901112151" />

## 🧠 Ce que j'ai appris sur ce projet

- Gestion de fichiers CSV malformés (lignes hétérogènes, encodages)
- Refacto
- Reconstruction d'événements appariés à partir d'un flux de logs brut
- Apprentissage de la stack pandas

## 📄 Licence

MIT
