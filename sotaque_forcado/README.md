```python
from sotaque_forcado.sotaques import Sotaque


s = Sotaque("sotaque_forcado/sotaques/algarvio.json")


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
    print(sent, "->", s.add_accent(sent), "->", s.phonemize(sent))
    # quis entrar na piscina mas a água estava fria -> Quij entrari nã piscinã maj a água estava fria . -> kiʒ eɪŋtɹɐɾi nɐ̃ pisinɐ̃ maʒ ɐ aɡwɐ ʃtɐvɐ fɹiɐ 
    # tenho um quilo de pastilha elástica na mochila -> Tenh um quil de pastilha elástica nã mochila . -> teɲ ũŋ kil dɨ pɐʃtiʎɐ elaʃtikɐ nɐ̃ muʃilɐ 
    # o boi passou a correr porque viu a vaca a pastar -> O boi passô a corrêri porque viu a vaca a pastari . -> ʊ boɪ pɐso ɐ kuʁeɾi poɾəkɨ viʊ ɐ vakɐ ɐ pɐʃtɐɾi 
    # A Filipa tem um coelho que come cenouras o ano inteiro -> A Filipa têm um coêlh que come cenôraj o an intêr . -> ɐ filipɐ teɪŋ ũŋ kueʎ kɨ komɨ senoɾɐʒ u ɐ̃ŋ iŋteɹ 
    # o meu sotaque é especial e também se percebe bem -> O mê sotaque é especial e tambêm se percebe bêm . -> ʊ me sutakɨ ɛ ʃpesiɑl i tɐ̃mbeɪŋ sɨ peɾəsɛbɨ beɪŋ 
    # eu tenho muitos amigos mas tu és o número um -> Eu tenh muitoj amigos mas tu éj o númer um . -> eʊ teɲ muɪtoʒ ɐmiɡʊʒ mɐʃ tu ɛʒ ʊ nũmɨɹ ũŋ 
    # todos os verões eu faço uma viagem com os meus cães -> Todoj os verõj eu faç uma viagêm com os meus cães . -> tudoʒ uʒ vɨɾõʒ eʊ fas umɐ viɐʒeɪŋ kom uʒ meʊʃ kɐ̃ɨʃ 
    # o quê ? não percebi nada do que tu disseste -> O quê ? nã percebi nada do que tu disseste . -> ʊ ke nɐ̃ peɾəsɨbi nadɐ dʊ kɨ tu disɛʃtɨ 
    # dá-me a mão para irmos comprar pão porque eu tenho medo do cão -> Dá me a mã para irmos comprari pã porque eu tenh med do cã . -> da mɨ ɐ mɐ̃ pɐɾɐ iɾəmʊʃ kumpɹɐɾi pɐ̃ poɾəkɨ eʊ teɲ med dʊ kɐ̃ 
    # ó mãe olha que está vermelho -> Ó mãe olha que está vermêlh . -> ɔ mɐ̃j ɔʎɐ kɨ esta vɨɾəmeʎ 
    # a gente só sabe verdadeiramente o que sente quando está doente -> A gente só sabe verdadêramente o que sente quand está doente . -> ɐ ʒeɪŋtɨ sɔ sabɨ veɾədɐdeɾɐmeɪŋtɨ ʊ kɨ seɪŋtɨ kwɐ̃ŋd esta dueɪŋtɨ 
    # cuidado com o touro -> Cuidad com o tôr . -> kuɪdad kom ʊ toɹ 
    # não faças dessa maneira -> Nã faças dessa manêra . -> nɐ̃ fasɐʒ dɛsɐ mɐneɾɐ 
    # Já leste o livro ou ainda te doi o olho -> Já leste o livr ou ainda te doi o olh . -> ʒa lɛʃtɨ ʊ livɾ ow ɐiŋdɐ tɨ doɪ u ɔʎ 
    # O Filipe está a comer aquilo , cheio de formigas -> O Filipe está a comêri aquil , chê de formigas . -> ʊ filipɨ esta ɐ kumeɾi ɐkil ʃe dɨ fuɾəmiɡɐʃ 
    # eles foram sair e depois ficaram lá fora ao frio -> Eles foram saíri e depois ficaram lá fora ao fri . -> elɨʃ foɾɐ̃ʊ̃ sɐiɾi i dɨpoɪʃ fikaɾɐ̃ʊ̃ la fɔɾɐ aʊ fɹi 
    # tem cuidado ao sair da garagem -> Têm cuidad ao saíri da garagêm . -> teɪŋ kuɪdad aʊ sɐiɾi dɐ ɡɐɾɐʒeɪŋ 
    # faz boa viagem -> Faz boa viagêm . -> fɐʒ boɐ viɐʒeɪŋ 
    # não vamos devolver o ouro -> Nã vamos devolvêri o ôr . -> nɐ̃ vɐ̃mʊʒ dɨvulveɾi u oɹ 
    # o Ronaldo deixou cair o chouriço ao chão -> O Ronald dêxô caíri o chôriç ao chã . -> ʊ ʁonɑld dekso kɐiɾi ʊ ʃoɾis aʊ ʃɐ̃ 
    # isso dá azar! -> Iss dá azari . -> iɛsʲɛs da ɐzɐɾi 
    # que deus te ajude que Jesus já não consegue -> Que deus te ajude que Jesus já nã consegue . -> kɨ deʊʃ tɨ ɐʒudɨ kɨ ʒɨzuʒ ʒa nɐ̃ kuŋsɛɡɨ 
```