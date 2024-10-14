import random
import time

# Lista di risposte per domande sul futuro
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

# Lista di risposte per domande su Simone
risposte_simone = [
    "Non molto, ma ha un grande potenziale! 🤔",  # Leggermente negativa
    "Abbastanza, ma c'è spazio per crescere! 📈",  # Neutra
    "Sì, decisamente! 👍",  # Positiva
    "Molto, è un valore aggiunto! 🌟",  # Positiva
    "Assolutamente, non ti deluderà! 🚀"  # Estremamente positiva
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
    print("\n🎱 La Magic Ball sta pensando", end="")
    time.sleep(1.5)
    for _ in range(4):
        print(".", end="", flush=True)
        time.sleep(1)

# Funzione principale del gioco
def magic_ball():
    print("\n✨ Benvenuto nella Magic Ball! ✨")
    time.sleep(2)
    
    print("\n1️⃣ Vuoi scoprire cosa il destino ha in serbo per te? Fai una domanda sul futuro!")
    time.sleep(4)
    print("2️⃣ Vorresti conoscere meglio Simone e le sue capacità lavorative? Fai una domanda su di lui!")
    time.sleep(4)
    print("3️⃣ Vuoi uscire dal gioco?")
    time.sleep(2)

    scelta = input("➡️ Seleziona un'opzione (1, 2 o 3): ")

    if scelta == "1":
        print("\n❓ Fai una domanda sul futuro.")
        time.sleep(2)
        print("💡 Esempi di domande: ")
        for esempio in suggerisci_domanda("futuro"):
            print(f"- {esempio}")
        domanda = input("\nInserisci la tua domanda: ")
        risposta = random.choice(risposte_futuro)
        crea_suspense()
        print(f"\n🎉 La Magic Ball dice: {risposta}")

    elif scelta == "2":
        print("\n❓ Fai una domanda su Simone.")
        time.sleep(2)
        print("💡 Esempi di domande: ")
        for esempio in suggerisci_domanda("simone"):
            print(f"- {esempio}")
        domanda = input("\nInserisci la tua domanda: ")
        risposta = random.choice(risposte_simone)
        crea_suspense()
        print(f"\n🎉 La Magic Ball dice: {risposta}")

    elif scelta == "3":
        print("Grazie per aver giocato! A presto! 👋")

    else:
        print("⚠️ Opzione non valida. Riprova.")
        
    while True:
        # Ripetizione dell'interazione
        time.sleep(2)
        print("\nCosa vuoi fare ora?")
        print("1️⃣ Fai una domanda sul futuro.")
        print("2️⃣ Fai una domanda su Simone.")
        print("3️⃣ Esci dal gioco.")
        
        scelta = input("➡️ Seleziona un'opzione (1, 2 o 3): ")
        
        if scelta == "1":
            print("\n❓ Fai una domanda sul futuro.")
            time.sleep(2)
            print("💡 Esempi di domande: ")
            for esempio in suggerisci_domanda("futuro"):
                print(f"- {esempio}")
            domanda = input("\nInserisci la tua domanda: ")
            risposta = random.choice(risposte_futuro)
            crea_suspense()
            print(f"\n🎉 La Magic Ball dice: {risposta}")
        
        elif scelta == "2":
            print("\n❓ Fai una domanda su Simone.")
            time.sleep(2)
            print("💡 Esempi di domande: ")
            for esempio in suggerisci_domanda("simone"):
                print(f"- {esempio}")
            domanda = input("\nInserisci la tua domanda: ")
            risposta = random.choice(risposte_simone)
            crea_suspense()
            print(f"\n🎉 La Magic Ball dice: {risposta}")
        
        elif scelta == "3":
            print("Grazie per aver giocato! A presto! 👋")
            break
        
        else:
            print("⚠️ Opzione non valida. Riprova.")

# Avvia il gioco
magic_ball()
