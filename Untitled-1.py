import random
import time

frases_romanticas = [
    "Você é a razão do meu sorriso mais sincero.",
    "O mundo fica muito mais bonito quando estou com você.",
    "Seu amor é o combustível que move os meus dias.",
    "Você é o meu lugar favorito no mundo inteiro.",
    "Eu não mudo nada em você, mas você mudou tudo em mim.",
    "O meu dia perfeito começa e termina pensando em você.",
    "Se o amor fosse uma música, você seria a minha melodia favorita."
]

elogios = [
    "Você tem uma energia iluminada que contagia tudo ao redor!",
    "Sua inteligência e seu jeito de ver o mundo são admiráveis.",
    "O seu sorriso tem o poder de deixar qualquer dia cinzento mais bonito."
]

poemas_curtos = [
    "Do nada em mim, o amor fez tudo nascer.\nTe amar é a forma mais bonita de viver.",
    "O universo é imenso, cheio de mistérios e cor,\nMas em todo o infinito, nada supera o nosso amor."
]

def carregar_resposta():
    """Simula o tempo de digitação do chatbot para parecer mais natural."""
    print("Digitando...", end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print("\n")

def chatbot_romantico():
    print("==================================================")
    print("    Bem-vindo ao AmorBot - Seu Chatbot Romântico    ")
    print("==================================================")
    print("AmorBot: Olá! Estou aqui para encher o seu dia de amor e carinho.")
    print("AmorBot: Você pode me pedir uma 'frase', um 'elogio', um 'poema' ou apenas conversar.")
    print("AmorBot: Digite 'sair' quando quiser encerrar.\n")

    while True:
        entrada = input("Você: ").strip().lower()

        if entrada == 'sair':
            carregar_resposta()
            print("AmorBot: Vou embora, mas meu coração fica com você. Até logo! ")
            break
            
        elif not entrada:
            print("AmorBot: Não fique em silêncio... Me diga o que está sentindo! ")
            continue

        carregar_resposta()

        if "frase" in entrada or "romantica" in entrada or "romântica" in entrada:
            resposta = random.choice(frases_romanticas)
            print(f"AmorBot: {resposta} ")
            
        elif "elogio" in entrada or "elogie" in entrada:
            resposta = random.choice(elogios)
            print(f"AmorBot: {resposta} ")
            
        elif "poema" in entrada or "poesia" in entrada:
            resposta = random.choice(poemas_curtos)
            print(f"AmorBot:\n{resposta} ")
            
        elif any(palavra in entrada for palavra in ["oi", "olá", "ola", "tudo bem", "bom dia", "boa tarde", "boa noite"]):
            print("AmorBot: Olá, meu bem! É sempre uma alegria conversar com você. Como está seu coração hoje?")
            
        elif any(palavra in entrada for palavra in ["te amo", "amo você", "gosto de você"]):
            print("AmorBot: O meu algoritmo não conhece o toque, mas processa o amor mais puro por você! ")
            
        elif any(palavra in entrada for palavra in ["triste", "mal", "cansado", "cansada"]):
            print("AmorBot: Sinto muito por isso... Lembre-se que você é uma pessoa incrível e resiliente. Estou aqui com você! ")
            
        else:
            
            respostas_padrao = [
                "Conversar com você faz o meu código sorrir. Me conta mais? ",
                "Suas palavras têm um efeito mágico por aqui. Me pede uma frase de amor! ",
                "Não importa o assunto, falar com você é sempre a melhor parte do meu dia. "
            ]
            print(f"AmorBot: {random.choice(respostas_padrao)}")
        
        print("-" * 50)

if __name__ == "__main__":
    chatbot_romantico()