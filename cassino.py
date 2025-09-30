import random
import time

# Emojis dos rolos
symbols = ["🍒", "🍋", "🔔", "🍇", "⭐", "💎", "7️⃣", "🎰"]

# Frases para dois símbolos iguais
frases_cassino = [
    "Putz, quase lá!",
    "Deposite mais, não pare!",
    "Solta a carta!!!!!",
    "Calma que o max win vem",
    "Bota mais 10zin que ele paga!"
]

def girar_slot():
    return [random.choice(symbols) for _ in range(3)]

def verificar_resultado(rolos):
    if rolos[0] == rolos[1] == rolos[2]:
        return "🎉 NIIICEEEE!!!! TRÊS IGUAIS!", 50
    elif rolos[0] == rolos[1] or rolos[1] == rolos[2] or rolos[0] == rolos[2]:
        return random.choice(frases_cassino), 20
    else:
        return "😢 Não foi dessa vez, aposta mais kk!!!", 0

def jogar():
     
    fichas = 100
    aposta = 10

    print("Pressione ENTER para girar. Ctrl+C para sair.\n")
    print("Você começa com 100 fichas.")
    print("Cada rodada custa 10 fichas.\n")

    while fichas >= aposta:
        input(f"👉 Aperte ENTER para girar (Saldo: {fichas} fichas)")
        fichas -= aposta
        print("\n🎲 Girando...\n")
        time.sleep(1)

        rolos = girar_slot()
        print(" | ".join(rolos))

        mensagem, ganho = verificar_resultado(rolos)
        print(mensagem)
        if ganho > 0:
            print(f"💰 Você ganhou {ganho} fichas!")
            fichas += ganho

        print(f"💵 Saldo atual: {fichas} fichas")
        print("="*35)

    print("\n❌ Fichas acabaram! Fim de jogo ❌")

    while True:
        input("👉 Aperte ENTER para iniciar o giro")
        print("🎲 Girando...\n")
        time.sleep(1)

        rolos = girar_slot()
        print(" | ".join(rolos))
        print(verificar_resultado(rolos))
        print("="*30)

# Inicia o jogo
jogar()
