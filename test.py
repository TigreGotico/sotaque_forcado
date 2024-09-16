from sotaque_forcado.sotaques import Sotaque


s = Sotaque("sotaque_forcado/sotaques/fafe.json")


test = [
    "quis entrar na piscina mas a água estava fria",
    "tenho um quilo de pastilha elástica na mochila",
    "o boi passou a correr porque viu a vaca a pastar",
    "A Filipa tem um coelho que come cenouras o ano inteiro",
    "o meu sotaque é especial e também se percebe bem",
    "eu tenho muitos amigos mas tu és o número um",
    "todos os verões eu faço uma viagem com os meus cães",
    "o quê ? não percebi nada do que tu disseste",

    "dá-me a mão para irmos comprar pão porque eu tenho medo do cão",
    "ó mãe olha que está vermelho",
    "a gente só sabe verdadeiramente o que sente quando está doente",
    "cuidado com o touro",
    "não faças dessa maneira",
    "Já leste o livro ou ainda te doi o olho",
    "O Filipe está a comer aquilo , cheio de formigas",
    "eles foram sair e depois ficaram lá fora ao frio",
    "tem cuidado ao sair da garagem",
    "faz boa viagem",
    "não vamos devolver o ouro",
    "o Ronaldo deixou cair o chouriço ao chão",
    "isso dá azar!",
    "que deus te ajude que Jesus já não consegue"
]
for sent in test:
    print(s.phonemize(sent))