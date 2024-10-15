import streamlit as st
import time
import random

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

# Funzione per creare suspense
def crea_suspense():
    with st.spinner("🎱 La Magic Ball sta pensando..."):
        time.sleep(2)

# Funzione principale
def main():
    st.title("✨ Magic Ball! Versione Migliorata ✨")
    
    # Check per vedere se i messaggi iniziali sono già stati mostrati
    if 'mostra_messaggi' not in st.session_state:
        mostra_messaggi_con_ritardo()
        st.session_state['mostra_messaggi'] = True

    scelta = st.radio("Scegli cosa chiedere:", ("Futuro", "Simone"))

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
