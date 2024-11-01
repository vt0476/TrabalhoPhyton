class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int) -> None:
        """Inicializa o produto com o nome, preço e quantidade fornecidos.
        
        Args:
            nome (str): Nome do produto.
            preco (float): Preço do produto.
            quantidade (int): Quantidade disponível do produto.
        """
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_informacoes(self) -> None:
        """Exibe as informações do produto."""
        print(f"Nome: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")

    def atualizar_preco(self, novo_preco: float) -> None:
        """Atualiza o preço do produto.
        
        Args:
            novo_preco (float): Novo preço do produto.
        """
        self.preco = novo_preco
        print(f"Preço atualizado para R${self.preco:.2f}")

    def atualizar_quantidade(self, nova_quantidade: int) -> None:
        """Atualiza a quantidade do produto.
        
        Args:
            nova_quantidade (int): Nova quantidade do produto.
        """
        self.quantidade = nova_quantidade
        print(f"Quantidade atualizada para {self.quantidade}")