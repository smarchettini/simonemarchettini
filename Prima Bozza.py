import streamlit as st
import time

# Funzione per mostrare i messaggi con ritardo
def mostra_messaggi_con_ritardo():
    # Riserva uno spazio per aggiornare i messaggi
    messaggio_1 = st.empty()

    # Mostra il primo messaggio e aspetta 4 secondi
    messaggio_1.write("1️⃣ Vuoi scoprire cosa il destino ha in serbo per te? Fai una domanda sul futuro!")
    time.sleep(4)

    # Mostra il secondo messaggio e aspetta 4 secondi
    messaggio_1.write("2️⃣ Vorresti conoscere meglio Simone e le sue capacità lavorative? Fai una domanda su di lui!")
    time.sleep(4)

# Titolo dell'app
st.title("Interazione sequenziale in Streamlit")

# Bottone per avviare l'interazione
if st.button("Inizia"):
    mostra_messaggi_con_ritardo()
