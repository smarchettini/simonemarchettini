
import streamlit as st
import time
import random

# Funzione per mostrare i messaggi con ritardo
def mostra_messaggi_con_ritardo():
    # Riserva uno spazio per aggiornare i messaggi
    messaggio_1 = st.empty()
    time.sleep(2)
    messaggio_1.write("Benvenuto nella Magic Ball!")
    time.sleep(3)

    # Mostra il primo messaggio e aspetta 4 secondi
    messaggio_1.write("Vuoi scoprire cosa il destino ha in serbo per te? Fai una domanda sul futuro!")
    time.sleep(6)

    # Mostra il secondo messaggio e aspetta 4 secondi
    messaggio_1.write("Vorresti conoscere meglio Simone e le sue capacità lavorative? Fai una domanda su di lui!")
    time.sleep(6)


    
    
# Funzione principale
def main():
    # Titolo dell'app
    st.title("✨ Magic Ball! Prima Bozza✨")

    # Mostra i messaggi iniziali
    mostra_messaggi_con_ritardo()

    # Scelta dell'azione in una schermata separata
    scelta = st.radio("Scegli cosa chiedere:", ("Futuro", "Simone"))



if __name__ == "__main__":
    main()


