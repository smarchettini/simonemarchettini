import streamlit as st
import time

# Funzione per mostrare i messaggi con ritardo
def mostra_messaggi_con_ritardo():
    # Mostra il messaggio di benvenuto
    messaggio = st.empty()
    messaggio.write("Benvenuto nella Magic Ball!")
    time.sleep(2)  # Attendi 2 secondi

    # Mostra il primo messaggio e aspetta 3 secondi
    messaggio.write("Vuoi scoprire cosa il destino ha in serbo per te? Fai una domanda sul futuro!")
    time.sleep(3)

    # Mostra il secondo messaggio e aspetta 3 secondi
    messaggio.write("Vorresti conoscere meglio Simone e le sue capacità lavorative? Fai una domanda su di lui!")
    time.sleep(3)

    # Pulisci lo spazio
    messaggio.empty()  # Rimuove il contenuto precedente

# Funzione principale
def main():
    # Titolo dell'app
    st.title("✨ Magic Ball! Seconda Bozza✨")

    # Mostra i messaggi iniziali
    mostra_messaggi_con_ritardo()

    # Spazio vuoto per separare i messaggi iniziali dalla scelta
    st.write("")  # Crea uno spazio vuoto

    # Scelta dell'azione in una schermata separata
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
