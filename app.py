# lista de frutas
frutas = ["Morango", "Manga", "Uva", "Maça", "Banana", "Cajú"]

# exibe a lista
for i in range(len(frutas)):
    print(f"{i}: {frutas[i]}.")

try:
    #usuário informa o índice
    indice = int(input("Informe o índice da fruta ue deseja excluir: "))
    confirmacao = input(f"Deseja excluir a fruta {frutas[indice]}? Digite 'sim' para confirmar.")

    if confirmacao == "sim":
        del(frutas[indice])
        print("Fruta deletada com sucesso.")
    else:
        ...

except Exception as e:
    print(f"Não foi possível deletar a fruta.{e}.")
finally:
    #exibe a lista
    for i in range(len(frutas)):
        print(f"Índece {i}: {frutas[i]}.")