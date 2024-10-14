import streamlit as st
import time
import random

# Funzione per mostrare i messaggi con ritardo
def mostra_messaggi_con_ritardo():
    # Riserva uno spazio per aggiornare i messaggi
    messaggio = st.empty()
    time.sleep(2)  # Attendi 2 secondi
    # Mostra il messaggio di benvenuto
    messaggio.write("Benvenuto nella Magic Ball!")
    time.sleep(3)  # Attendi 2 secondi

    # Mostra il primo messaggio e aspetta 3 secondi
    messaggio.write("Vuoi scoprire cosa il destino ha in serbo per te? Fai una domanda sul futuro!")
    time.sleep(6)

    # Mostra il secondo messaggio e aspetta 3 secondi
    messaggio.write("Vorresti conoscere meglio Simone e le sue capacità lavorative? Fai una domanda su di lui!")
    time.sleep(6)
    messaggio.empty()

# Funzione principale
def main():
    # Titolo dell'app
    st.title("✨ Magic Ball! Seconda Bozza✨")

    # Mostra i messaggi iniziali
    mostra_messaggi_con_ritardo()

    # Scelta dell'azione in una schermata separata
    scelta = st.radio("Scegli cosa chiedere:", ("Futuro", "Simone"))



if __name__ == "__main__":
    main()
