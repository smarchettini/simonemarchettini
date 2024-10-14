import streamlit as st
import random
import time

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
        time.sleep(2)

# Interfaccia Streamlit
st.title("✨ Benvenuto nella Magic Ball! ✨")

# Spiegazione iniziale
st.write("Puoi fare una domanda sul futuro o chiedere informazioni su Simone!")

# Scelta dell'azione
scelta = st.radio("Scegli cosa chiedere:", ("Futuro", "Simone"))

# Suggerimenti per le domande
if scelta == "Futuro":
    st.write("💡 Esempi di domande:")
    for esempio in suggerisci_domanda("futuro"):
        st.write(f"- {esempio}")
    domanda = st.text_input("Fai una domanda sul futuro:")
    
    if st.button("Chiedi alla Magic Ball"):
        if domanda.strip() == "":
            st.warning("Per favore, inserisci una domanda!")
        else:
            crea_suspense()
            risposta = random.choice(risposte_futuro)
            st.success(f"🎉 La Magic Ball dice: {risposta}")

elif scelta == "Simone":
    st.write("💡 Esempi di domande:")
    for esempio in suggerisci_domanda("simone"):
        st.write(f"- {esempio}")
    domanda = st.text_input("Fai una domanda su Simone:")
    
    if st.button("Chiedi alla Magic Ball"):
        if domanda.strip() == "":
            st.warning("Per favore, inserisci una domanda!")
        else:
            crea_suspense()
            risposta = random.choice(risposte_simone)
            st.success(f"🎉 La Magic Ball dice: {risposta}")

# Opzione per uscire dal gioco
st.write("Quando hai finito, chiudi la pagina per terminare il gioco! 👋")