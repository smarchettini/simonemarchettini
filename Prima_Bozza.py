import streamlit as st
import time
import random

# Funzione per mostrare i messaggi con ritardo
def mostra_messaggi_con_ritardo():

    time.sleep(2)  # Attendi 2 secondi
    # Mostra il messaggio di benvenuto
    st.empty().write("Benvenuto nella Magic Ball!")
    time.sleep(3)  # Attendi 2 secondi

    # Mostra il primo messaggio e aspetta 3 secondi
    st.empty().write("Vuoi scoprire cosa il destino ha in serbo per te? Fai una domanda sul futuro!")
    time.sleep(6)

    # Mostra il secondo messaggio e aspetta 3 secondi
    st.empty().write("Vorresti conoscere meglio Simone e le sue capacità lavorative? Fai una domanda su di lui!")
    time.sleep(6)
    st.empty()
    

# Funzione principale
def main():
    # Titolo dell'app
    st.title("✨ Magic Ball! Prima Bozza!✨")

    # Mostra i messaggi iniziali
    mostra_messaggi_con_ritardo()

    # Scelta dell'azione in una schermata separata
    scelta = st.radio("Scegli cosa chiedere:", ("Futuro", "Simone"))



if __name__ == "__main__":
    main()
