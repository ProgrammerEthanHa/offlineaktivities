import streamlit as st
import pandas as pd
import altair as alt

st.header("Vergleich der Häufigkeit der Offline-Aktivitäten mit Freundinnen und Freunden")
st.subheader("1 = nie bis 6 = täglich / 2021")

source = pd.DataFrame({
        'Häufigkeit': [4.81, 2.17, 3.21, 3.00, 4.37],
        'Aktivitäten': ['Treffen in Schule, Ausbildung, Studium oder Arbeit', 'Treffen in Verein, Jugendgruppe oder Jugendzentrum', 'Treffen an öffentlichen Orten', 'Gemeinsame Freizeitaktivitäten', 'Über persönliche Dinge reden']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Häufigkeit:Q',
        x='Aktivitäten:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis n = 1126; Jugendliche
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle:  AID:A 2021")