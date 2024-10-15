import streamlit as st
import time
import random

# Funzione per mostrare i messaggi con ritardo
def mostra_messaggi_con_ritardo():
    # Mostra il messaggio di benvenuto
    messaggio = st.empty()
    time.sleep(1)

    messaggio.write("Benvenuto nella Magic Ball!")
    time.sleep(3)  # Attendi 3 secondi

    # Mostra il primo messaggio e aspetta 5 secondi
    messaggio.write("Vuoi scoprire cosa il destino ha in serbo per te? Fai una domanda sul futuro!")
    time.sleep(5)

    # Mostra il secondo messaggio e aspetta 5 secondi
    messaggio.write("Vorresti conoscere meglio Simone e le sue capacità lavorative? Fai una domanda su di lui!")
    time.sleep(5)

    # Pulisci lo spazio
    messaggio.empty()  # Rimuove il contenuto precedente

# Liste di risposte
risposte_futuro = [
    "Sì, sicuramente. 🚀",
    "Non so, chiedi di nuovo. 🤔",
    "Sembra improbabile. ❌",
    "Sì. 🎉",
    "Non contare su di esso. 😬",
    "È certo. 🌟",
    "Le prospettive non sono buone. 😕",
    "Sì, in effetti. 💯",
    "Non è il momento giusto. ⏳",
    "Certo, perché no? 👍"
]

risposte_simone = [
    "Non molto, ma ha un grande potenziale! 🤔",
    "Abbastanza, ma c'è spazio per crescere! 📈",
    "Sì, decisamente! 👍",
    "Molto, è un valore aggiunto! 🌟",
    "Assolutamente, non ti deluderà! 🚀"
]

# Funzione per creare suspense
def crea_suspense():
    with st.spinner("🎱 La Magic Ball sta pensando..."):
        time.sleep(2)

# Funzione principale
def main():
    # Titolo dell'app
    st.title("✨ Magic Ball! Prima Bozza✨")

    # Mostra i messaggi iniziali
    mostra_messaggi_con_ritardo()

    # Spazio vuoto per separare i messaggi iniziali dalla scelta
    st.write("")  # Crea uno spazio vuoto
    
    # Scelta dell'azione in una schermata separata
    scelta = st.radio("Scegli cosa chiedere:", ("Futuro", "Simone"))

    # Suggerimenti per le domande
    if scelta == "Futuro":
        domanda = st.text_input("Fai una domanda sul futuro:")
        
        if st.button("Chiedi alla Magic Ball"):
            if domanda.strip() == "":
                st.warning("Per favore, inserisci una domanda!")
            else:
                crea_suspense()
                risposta = random.choice(risposte_futuro)
                st.success(f"🎉 La Magic Ball dice: {risposta}")
    
    elif scelta == "Simone":
        domanda = st.text_input("Fai una domanda su Simone:")
        
        if st.button("Chiedi alla Magic Ball"):
            if domanda.strip() == "":
                st.warning("Per favore, inserisci una domanda!")
            else:
                crea_suspense()
                risposta = random.choice(risposte_simone)
                st.success(f"🎉 La Magic Ball dice: {risposta}")

if __name__ == "__main__":
    main()
