class Filme:
    def __init__(self, titulo, ano_lancamento, diretor, genero, duracao):
        self.titulo = titulo
        self.ano_lancamento = ano_lancamento
        self.diretor = diretor
        self.genero = genero
        self.duracao = duracao

class CatalogoFilmes:
    def __init__(self):
        self.filmes = []

    def cadastrar_filme(self, filme):
        self.filmes.append(filme)

    def listar_filmes(self):
        for filme in self.filmes:
            print(f"Título: {filme.titulo}, Ano de Lançamento: {filme.ano_lancamento}, Diretor: {filme.diretor}, Gênero: {filme.genero}, Duração: {filme.duracao} minutos")

# Criando o catálogo de filmes
catalogo = CatalogoFilmes()

# Cadastro de filmes
filme1 = Filme("Interestelar", 2014, "Christopher Nolan", "Ficção Científica", 169)
filme2 = Filme("O Poderoso Chefão", 1972, "Francis Ford Coppola", "Drama", 175)
filme3 = Filme("Matrix", 1999, "Lana Wachowski, Lilly Wachowski", "Ação", 136)

catalogo.cadastrar_filme(filme1)
catalogo.cadastrar_filme(filme2)
catalogo.cadastrar_filme(filme3)

# Listando os filmes cadastrados
catalogo.listar_filmes()
