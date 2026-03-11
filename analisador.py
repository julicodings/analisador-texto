#Receber um texto
#Determinar quantas palavras,carateres e linhas o texto tem

def analisar_texto(texto):
    #contar linhas
    linhas=texto.splitlines()
    numero_linhas=len(linhas)

    #contar palavras
    palavras=texto.split()
    numero_palavras=len(palavras)

    #contar caracteres
    caracteres=len(texto)

    return numero_linhas,numero_palavras,caracteres


def main():
    print("-----------------------------------")
    print("Bem-vindo ao Analisador de Textos!")
    print("-----------------------------------")
    print("Digite seu texto abaixo, e para finalizar pressione Enter 2x")
    print("-----------------------------------")

#Entrada do texto
    texto = ""
    while True:
        linha = input()
        #Condicao de encerramento:

        if linha == "": #se a linha for vazia quebra o loop
            break
        texto += linha + "\n" # senão for vazia concatena o texto + uma quebra de linha
    
    linhas, palavras, caracteres = analisar_texto(texto)

    print("\n-----------------------------------")

    print(f"O texto tem {linhas} linhas.")
    print(f"O texto tem {palavras} palavras.")
    print(f"O texto tem {caracteres} caracteres.")

    print("\n-----------------------------------")


if __name__ == "__main__":
    main()