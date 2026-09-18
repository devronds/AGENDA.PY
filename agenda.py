def add_contato(contatos, nome_contato, numero_contato, email):
    contato = {"nome": nome_contato.upper(), "numero": numero_contato, "email": email, "fav": False}
    contatos.append(contato) 

def view_contatos(contatos):
    print("\n" + "-" * 5 + "AGENDA" + "-" * 5)
    if contatos == []:
        print("\nSEM CONTATOS")
    for i, contato in enumerate(contatos, start=1):
        favorito = "♡" if contato["fav"] == True else ""
        print(f"{i}. NOME: {contato['nome']} TELEFONE: {contato['numero']} FAVORITO? | {favorito} |")

def update_contato(contatos, i_contato, novo_nome, novo_num, novo_email, favoritar):
    i_ajustado = int(i_contato) - 1
    if i_ajustado >= 0 and i_ajustado < len(contatos):
        contatos[i_ajustado]["nome"] = novo_nome 
        contatos[i_ajustado]["numero"] = novo_num
        contatos[i_ajustado]["email"] = novo_email
        while True:
            if favoritar == "yes":
                contatos[i_ajustado]["fav"] = True
                break
            elif favoritar == "no":
                contatos[i_ajustado]["fav"] = False
                break
            else:
                favoritar = input("DIGITE UMA OPÇÃO VÁLIDA(yes/no): ")
    else:
        print("CONTATO NÃO EXISTE")

def favoritar(contatos, i_contato_fav):
    i_ajustado = int(i_contato_fav) -1
    if i_ajustado >= 0 and i_ajustado < len(contatos):
        contatos[i_ajustado]["fav"] = True
    else:
        print("VALOR INVÁLIDO!")

def lista_favoritos(contatos):
    print("\nLISTA DE FAVORITOS")
    for i, contato in enumerate(contatos, start=1):
        if contato["fav"] == True:
            print(f"\n-{i}.  {contato['nome']} - Nº: {contato['numero']}")
        else:
            ""
def deletar_contato(contatos, i_contato):
    i_ajustado = int(i_contato) -1
    if i_ajustado >= 0 and i_ajustado < len(contatos):
        del contatos[i_ajustado]
    else:
        print("CONTATO INVÁLIDO")


contatos = []

while True:
    print("\n" + "=" *10 + "AGENDA DE CONTATOS" + "=" *10)
    print("\n1. ADD CONTATO")
    print("2. VER AGENDA")
    print("3. EDITAR CONTATO")
    print("4. MARCAR COMO FAVORITO")
    print("5. LISTA DE FAVORITOS")
    print("6. DELETAR CONTATO")
    print("7. SAIR DA AGENDA")

    i_opcao = input("\nESCOLHA A OPÇÃO DESEJADA: ")

    if i_opcao == "1":
        nome_c = input("DIGITE O NOME DO CONTATO: ")
        num_c = input("DIGITE O NÚMERO DO CONTATO: ")
        email_c = input("DIGITE O EMAIL DO CONTATO: ")
        add_contato(contatos, nome_c, num_c, email_c)
        print(contatos)
    elif i_opcao == "2":
        view_contatos(contatos)
    elif i_opcao == "3":
        view_contatos(contatos)
        i_contato = input("DIGITE O ÍNDICE DO CONTATO QUE DESEJA ATUALIZAR: ")
        novo_nome = input("DIGITE O NOME DO CONTATO: ")
        novo_numero = input("DIGITE O NÚMERO DO CONTATO: ")
        novo_email = input("DIGITE O EMAIL DO CONTATO: ")
        fav_opcao = input("FAVORITAR?(yes/no): ")

        update_contato(contatos, i_contato, novo_nome, novo_numero, novo_email, fav_opcao)
    elif i_opcao == "4":
        view_contatos(contatos)
        i_contato_fav = input("QUAL CONTATO QUER FAVORITAR? ")
        favoritar(contatos, i_contato_fav)
    elif i_opcao == "5":
        lista_favoritos(contatos)
    elif i_opcao == "6":
        i_contato = input("QUAL CONTATO DESEJA DELETAR?")
        deletar_contato(contatos, i_contato)
    elif i_opcao == "7":
        print("SAIU DA AGENDA")
        break
    else:
        print("DIGITE UM INDICE VÁLIDO!")