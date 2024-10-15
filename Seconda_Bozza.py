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
            "L'intelligenza artificiale cambierà
