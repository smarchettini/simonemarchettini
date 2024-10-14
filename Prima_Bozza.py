import streamlit as st
import time

# Funzione per mostrare i messaggi con ritardo
def mostra_messaggi_con_ritardo(messaggio):
    # Riserva uno spazio per aggiornare i messaggi
    st.empty().write(messaggio)
    time.sleep(2)

# Funzione principale
def main():
    # Titolo dell'app
    st.title("✨ Magic Ball! Seconda Bozza✨")

    # Mostra i messaggi iniziali
    messaggio_1 = "Benvenuto nella Magic Ball!"
    mostra_messaggi_con_ritardo(messaggio_1)

    messaggio_2 = "Vuoi scoprire cosa il destino ha in serbo per te? Fai una domanda sul futuro!"
    mostra_messaggi_con_ritardo(messaggio_2)

    messaggio_3 = "Vorresti conoscere meglio Simone e le sue capacità lavorative? Fai una domanda su di lui!"
    mostra_messaggi_con_ritardo(messaggio_3)

    # Pulisci la schermata
    st.empty()  # Questo ripulirà l'area dei messaggi

    # Scelta dell'azione
    scelta = st.radio("Scegli cosa chiedere:", ("Futuro", "Simone"))

    # Pulsante per avviare l'interazione
    if st.button("Avvia Interazione"):
        if scelta == "Futuro":
            st.write("Hai scelto di chiedere sul futuro!")
            # Qui puoi aggiungere logica per gestire le domande sul futuro
        else:
            st.write("Hai scelto di chiedere su Simone!")
            # Qui puoi aggiungere logica per gestire le domande su Simone

if __name__ == "__main__":
    main()
