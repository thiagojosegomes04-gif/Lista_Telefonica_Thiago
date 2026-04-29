class Contato:
    def __init__(self, nome: str, telefone: str):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome} | Telefone: {self.telefone}"


class ListaTelefonica:
    def __init__(self):
        # ArrayList em Python → lista dinâmica
        self.contatos = []

    # CREATE
    def adicionar_contato(self, nome: str, telefone: str):
        if self.buscar_contato(nome) is not None:
            print("Contato já existe!")
            return
        
        novo_contato = Contato(nome, telefone)
        self.contatos.append(novo_contato)
        print("Contato adicionado com sucesso!")

    # READ
    def listar_contatos(self):
        if not self.contatos:
            print("Lista telefônica vazia.")
            return
        
        for contato in self.contatos:
            print(contato)

    # SEARCH
    def buscar_contato(self, nome: str):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                return contato
        return None

    # UPDATE
    def atualizar_contato(self, nome: str, novo_telefone: str):
        contato = self.buscar_contato(nome)
        if contato is None:
            print("Contato não encontrado!")
        else:
            contato.telefone = novo_telefone
            print("Contato atualizado com sucesso!")

    # DELETE
    def remover_contato(self, nome: str):
        contato = self.buscar_contato(nome)
        if contato is None:
            print("Contato não encontrado!")
        else:
            self.contatos.remove(contato)
            print("Contato removido com sucesso!")


# =============================
# MENU (INTERFACE SIMPLES)
# =============================

def menu():
    lista = ListaTelefonica()

    while True:
        print("\n--- LISTA TELEFÔNICA ---")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Atualizar contato")
        print("5. Remover contato")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            lista.adicionar_contato(nome, telefone)

        elif opcao == "2":
            lista.listar_contatos()

        elif opcao == "3":
            nome = input("Nome para busca: ")
            contato = lista.buscar_contato(nome)
            if contato:
                print(contato)
            else:
                print("Contato não encontrado!")

        elif opcao == "4":
            nome = input("Nome do contato: ")
            telefone = input("Novo telefone: ")
            lista.atualizar_contato(nome, telefone)

        elif opcao == "5":
            nome = input("Nome do contato: ")
            lista.remover_contato(nome)

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")


# Execução do sistema
if __name__ == "__main__":
    menu()