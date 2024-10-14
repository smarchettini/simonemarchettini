import streamlit as st
import time

# Funzione per mostrare i messaggi con ritardo
def mostra_messaggi_con_ritardo():
    # Riserva uno spazio per aggiornare i messaggi
    time.sleep(3)
    messaggio_1 = st.empty()
    messaggio_2 = st.empty()

    # Mostra il primo messaggio e aspetta 4 secondi
    messaggio_1.write("1️⃣ Vuoi scoprire cosa il destino ha in serbo per te? Fai una domanda sul futuro!")
    time.sleep(6)

    # Mostra il secondo messaggio e aspetta 4 secondi
    messaggio_2.write("2️⃣ Vorresti conoscere meglio Simone e le sue capacità lavorative? Fai una domanda su di lui!")
    time.sleep(4)

# Titolo dell'app
st.title("✨ Benvenuto nella Magic Ball! ✨")

# Bottone per avviare l'interazione
mostra_messaggi_con_ritardo()
