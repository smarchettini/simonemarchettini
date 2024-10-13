import random
import time

# Lista di risposte della Magic 8 Ball
risposte = [
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

def magic_8_ball():
    # Introduzione coinvolgente
    print("✨ Benvenuto nella Magic 8 Ball! Poni la tua domanda e scopri cosa il destino ha in serbo per te! ✨")
    
    # Chiedi all'utente di inserire una domanda
    domanda = input("❓ Fai una domanda alla Magic 8 Ball: ")
    
    # Seleziona una risposta casuale
    risposta = random.choice(risposte)
    
    # Stampa la risposta con suspense
    print("\n🎱 La Magic 8 Ball sta pensando ", end="")
    time.sleep(1.5)
    for _ in range(3):
        print(".", end="")
        time.sleep(1)  # Attesa per creare suspense
    print("\n🎉 La Magic 8 Ball dice: ", risposta)
    print("🤔 Che sia la risposta che cercavi! ✨")  # Messaggio corretto

# Chiama la funzione
magic_8_ball()
