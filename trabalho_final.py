import math
import random
import datetime

print("=" * 50)
print("      CHATBOT EM PYTHON")
print("Digite 'ajuda' para ver os comandos.")
print("Digite 'sair' para encerrar.")
print("=" * 50)

nome = ""

while True:
    mensagem = input("\nVocê: ").lower().strip()

    if mensagem == "sair":
        print("Bot: Até logo!")
        break

    elif mensagem == "ajuda":
        print("""
Comandos disponíveis:

- oi
- olá
- bom dia
- boa tarde
- boa noite
- tudo bem
- qual seu nome
- meu nome é ...
- que horas são
- que dia é hoje
- obrigado
- ajuda
- soma
- subtração
- multiplicação
- divisão
- potência
- raiz quadrada
- sair
""")

    elif mensagem in ["oi", "olá", "ola"]:
        print("Bot: Olá! Como posso ajudar?")

    elif mensagem == "bom dia":
        print("Bot: Bom dia! Espero que seu dia seja excelente!")

    elif mensagem == "boa tarde":
        print("Bot: Boa tarde! Em que posso ajudar?")

    elif mensagem == "boa noite":
        print("Bot: Boa noite! Como posso ajudar?")

    elif "meu nome é" in mensagem:
        nome = mensagem.replace("meu nome é", "").strip().title()
        print(f"Bot: Prazer em conhecer você, {nome}!")

    elif mensagem == "qual seu nome":
        print("Bot: Meu nome é ChatBot Python.")

    elif mensagem == "tudo bem":
        respostas = [
            "Estou muito bem!",
            "Tudo certo por aqui!",
            "Estou funcionando perfeitamente!"
        ]
        print("Bot:", random.choice(respostas))

    elif mensagem == "que horas são":
        agora = datetime.datetime.now()
        print("Bot:", agora.strftime("%H:%M:%S"))

    elif mensagem == "que dia é hoje":
        hoje = datetime.datetime.now()
        print("Bot:", hoje.strftime("%d/%m/%Y"))

    elif mensagem == "obrigado":
        print("Bot: De nada! 😊")

    elif mensagem == "soma":
        a = float(input("Primeiro número: "))
        b = float(input("Segundo número: "))
        print("Resultado =", a + b)

    elif mensagem == "subtração":
        a = float(input("Primeiro número: "))
        b = float(input("Segundo número: "))
        print("Resultado =", a - b)

    elif mensagem == "multiplicação":
        a = float(input("Primeiro número: "))
        b = float(input("Segundo número: "))
        print("Resultado =", a * b)

    elif mensagem == "divisão":
        a = float(input("Primeiro número: "))
        b = float(input("Segundo número: "))

        if b == 0:
            print("Bot: Não é possível dividir por zero.")
        else:
            print("Resultado =", a / b)

    elif mensagem == "potência":
        a = float(input("Base: "))
        b = float(input("Expoente: "))
        print("Resultado =", a ** b)

    elif mensagem == "raiz quadrada":
        a = float(input("Número: "))

        if a < 0:
            print("Bot: Não existe raiz quadrada real de número negativo.")
        else:
            print("Resultado =", math.sqrt(a))

    else:
        respostas = [
            "Não entendi. Digite 'ajuda' para ver os comandos.",
            "Pode explicar de outra forma?",
            "Ainda estou aprendendo. Tente outro comando.",
            "Desculpe, não consegui compreender."
        ]

        print("Bot:", random.choice(respostas))