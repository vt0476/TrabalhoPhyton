class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int) -> None:
      
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_informacoes(self) -> None:
        """Exibe as informações do produto."""
        print(f"Nome: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")

    def atualizar_preco(self, novo_preco: float) -> None:

        self.preco = novo_preco
        print(f"Preço atualizado para R${self.preco:.2f}")

    def atualizar_quantidade(self, nova_quantidade: int) -> None:
      
        self.quantidade = nova_quantidade
        print(f"Quantidade atualizada para {self.quantidade}")
