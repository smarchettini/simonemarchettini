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
    messaggio.write("Benvenuto nella Magic Ball!")
    time.sleep(3)
    messaggio.write("Vuoi scoprire cosa il destino ha in serbo per te? Fai una domanda sul futuro!")
    time.sleep(5)
    messaggio.write("Vorresti conoscere meglio Simone e le sue capacità lavorative? Fai una domanda su di lui!")
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
    "Non molto, ma ha un grande potenziale! 🤔",
    "Abbastanza, ma c'è spazio per crescere! 📈",
    "Sì, decisamente! 👍",
    "Molto, è un valore aggiunto! 🌟",
    "Assolutamente, non ti deluderà! 🚀"
]

# Funzione per suggerire domande
def suggerisci_domanda(tipo):
    if tipo == "futuro":
        return [
            "Come sarà il futuro della mia azienda?",
            "L'intelligenza artificiale cambierà il mio settore?",
            "Ci sarà una promozione per me quest'anno?",
            "La mia azienda avrà successo l'anno prossimo?",
            "Il prossimo progetto avrà un impatto positivo?"
        ]
    elif tipo == "simone":
        return [
            "Simone è un buon lavoratore?",
            "Simone è affidabile in team?",
            "Simone è pronto per nuove sfide?",
            "Simone è un candidato ideale per la mia azienda?",
            "Simone si integra bene con il gruppo?"
        ]

# Funzione per creare suspense
def crea_suspense():
    with st.spinner("🎱 La Magic Ball sta pensando..."):
        time.sleep(4)

# Funzione per chiudere il gioco
def chiudi_gioco():
    st.session_state['gioco_attivo'] = False  # Imposta il gioco come chiuso

# Funzione principale
def main():
    # Titolo dell'app
    st.title("✨ Magic Ball ✨")

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
                for esempio in suggerisci_domanda("futuro"):
                    st.write(f"- {esempio}")
            elif scelta == "Simone":
                st.write("💡 Esempi di domande:")
                for esempio in suggerisci_domanda("simone"):
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

        # Bottone per chiudere il gioco
        if st.button("Chiudi il gioco"):
            chiudi_gioco()  # Imposta lo stato del gioco come chiuso
            st.rerun()  # Ricarica l'app per riflettere il cambiamento di stato

    else:
        # Se il gioco è chiuso, mostra solo il messaggio di ringraziamento
        st.write("Grazie per aver giocato! A presto! 👋")

if __name__ == "__main__":
    main()
