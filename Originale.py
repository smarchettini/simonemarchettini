import streamlit as st
import time
import random

# Inizializza lo stato della sessione
if 'gioco_attivo' not in st.session_state:
    st.session_state['gioco_attivo'] = True  # Indica se il gioco è attivo
if 'mostra_messaggi' not in st.session_state:
    st.session_state['mostra_messaggi'] = False  # Controlla se i messaggi iniziali sono già stati mostrati

# Funzione per mostrare i messaggi con ritardo
def mostra_messaggi_con_ritardo():
    messaggio = st.empty()
    time.sleep(1)
    messaggio.write("🎱 Benvenuto nella Magic 8 Ball!")
    time.sleep(3)
    messaggio.write("🎱 Vuoi scoprire cosa il destino ha in serbo per te? Fai una domanda sul futuro!")
    time.sleep(5)
    messaggio.write("🎱 Vorresti sapere quali sono i talenti nascosti di Simone a lavoro? Chiedilo alla Magic 8 Ball!")
    time.sleep(5)
    messaggio.empty()

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
"L’arte del delegare con tale grazia che sembra sia lui a fare tutto. 🎭",
"In realtà, ha semplicemente perfezionato l'arte di sembrare impegnato mentre pianifica il weekend. 🏖️",
"Simone è abile a mescolare umorismo sottile e silenzi riflessivi: funziona sempre. 🤔",
"La sua capacità di improvvisare è tale che gli altri pensano sia tutto pianificato. 🎩",
"Simone sa esattamente quando annuire e quando far sembrare che stia ascoltando profondamente. 👂"
]

# Funzione per suggerire domande
def suggerisci_domanda(tipo):
    if tipo == "Futuro":
        return [
            "Come sarà il futuro della mia azienda?",
            "L'intelligenza artificiale cambierà il mio settore?",
            "Ci sarà una promozione per me quest'anno?",
            "La mia azienda avrà successo l'anno prossimo?",
            "Il prossimo progetto avrà un impatto positivo?"
        ]
    elif tipo == "Simone":
        return [
"Qual è il talento di Simone?",
"Che abilità speciale ha Simone?",
"Qual è il segreto del successo di Simone?",
"Quale superpotere Simone possiede?"
        ]

# Funzione per creare suspense
def crea_suspense():
    with st.spinner("🎱 La Magic 8 Ball sta pensando..."):  # Mostra il messaggio di suspense
        progress_bar = st.progress(0)  # Crea una progress bar al 0%
        for percent_complete in range(101):
            time.sleep(0.03)  # 0.04 secondi per ogni incremento (100 incrementi totali = 4 secondi)
            progress_bar.progress(percent_complete)  # Aggiorna la barra con il valore attuale

# Funzione per chiudere il gioco
def chiudi_gioco():
    st.session_state['gioco_attivo'] = False  # Imposta il gioco come chiuso

# Funzione principale
def main():
    # Titolo dell'app
    st.markdown("<h1 style='text-align: center;'>✨ Magic 8 Ball ✨</h1>", unsafe_allow_html=True)


    st.write("")  # Prima riga vuota
    st.write("")  # Seconda riga vuota
    st.write("")  # Prima riga vuota
    st.write("")  # Seconda riga vuota

    # Controlla se il gioco è attivo
    if st.session_state['gioco_attivo']:
        # Mostra i messaggi iniziali solo una volta
        if not st.session_state['mostra_messaggi']:
            mostra_messaggi_con_ritardo()
            st.session_state['mostra_messaggi'] = True

        # Spazio per scegliere cosa chiedere
        scelta = st.radio("Scegli cosa chiedere:", ("Futuro", "Simone"))

        if st.button("Mostra i suggerimenti"):
            if scelta == "Futuro":
                st.write("💡 Esempi di domande:")
                for esempio in suggerisci_domanda("Futuro"):
                    st.write(f"- {esempio}")
            elif scelta == "Simone":
                st.write("💡 Esempi di domande:")
                for esempio in suggerisci_domanda("Simone"):
                    st.write(f"- {esempio}")

        # Gestione delle domande
        if scelta == "Futuro":
            domanda = st.text_input("Fai una domanda sul futuro:")
            if st.button("Chiedi alla Magic Ball"):
                if domanda.strip() == "":
                    st.warning("Per favore, inserisci una domanda!")
                else:
                    crea_suspense()
                    risposta = random.choice(risposte_futuro)
                    st.success(f"🎱 La Magic 8 Ball dice: {risposta}")
        
        elif scelta == "Simone":
            domanda = st.text_input("Fai una domanda su Simone:")
            if st.button("Chiedi alla Magic Ball"):
                if domanda.strip() == "":
                    st.warning("Per favore, inserisci una domanda!")
                else:
                    crea_suspense()
                    risposta = random.choice(risposte_simone)
                    st.success(f"🎱 La Magic 8 Ball dice: {risposta}")

        # Bottone per chiudere il gioco
        if st.button("Chiudi il gioco"):
            chiudi_gioco()  # Imposta lo stato del gioco come chiuso
            st.rerun()  # Ricarica l'app per riflettere il cambiamento di stato

    else:
        # Se il gioco è chiuso, mostra solo il messaggio di ringraziamento
        st.write(" Grazie per aver giocato! 🎉 ")
        st.write(" Non dimenticare di condividere le tue profezie in riunione! 😉 ")
        st.write(" A presto! 👋")

        
if __name__ == "__main__":
    main()
