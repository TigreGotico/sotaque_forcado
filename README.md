## Usage

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

## Regras

| Transformação                                                    | Descrição                                                                   | Exemplo(s)                                  |
|------------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------|
| `substituicao_v_por_b`                                           | Substitui 'v' por 'b'.                                                      | Vila -> Bila, Votar -> Botar                |
| `substituicao_de_ou_por_oi`                                      | Substitui 'ou' por 'oi'.                                                    | Outro -> Oitro, Mouro -> Moiro              |
| `substituicao_de_z_por_j`                                        | Substitui 'z' por 'j' e intensifica 'esu'.                                  | Jesus -> Jejus, Azar -> Ajar                |
| `substituicao_de_ch_por_tch`                                     | Fortalece o som de 'ch' adicionando 't'.                                    | Chão -> Tchão, Chouriço -> Tchouriço        |
| `substituicao_de_nao_por_num`                                    | A palavra "não" vira "num".                                                 | Não quero -> Num quero                      |
| `substituicao_final_de_ar_por_a`                                 | Substitui o final 'ar' por 'á'.                                             | Passar -> Passá                             |
| `substituicao_final_de_o_por_e`                                  | Substitui o final 'o' por 'e' exceto em certos casos.                       | Osso -> Osse, Carro -> Carre                |
| `substituicao_final_de_oi_por_u`                                 | Substitui o final 'oi' por 'û'.                                             | Boi -> Bû                                   |
| `substituicao_final_de_am_por_u`                                 | Substitui o final 'am' por 'u'.                                             | Ficaram -> Ficáru, Foram -> Fôru            |
| `substituicao_de_ae_por_an`                                      | Substitui 'ães' por 'ân'.                                                   | Cães -> Cãns                                |
| `substituicao_de_oe_por_on`                                      | Substitui 'ões' por 'ôns'.                                                  | Leões -> Leôns, Verões -> Verôns            |
| `u_frances`                                                      | Aplica o som de 'u francês'.                                                | Tu -> Tiú, Mula -> Miula                    |
| `ditongacao_vogal_tonica_com_u`                                  | Adiciona 'u' antes de vogais tônicas.                                       | Olho -> Uôlho, Livro -> Lúivro              |
| `enfase_anasalado_final_com_a`                                   | Enfatiza o som nasal com 'a'.                                               | O quê -> O quâ                              |
| `perda_do_u_final_depois_de_i`                                   | Remove o 'u' final após 'i'.                                                | Viu -> Vi                                   |
| `palatizacao_consoante_l_antecedida_por_i`                       | Palataliza 'l' quando precedido por 'i'.                                    | Vila -> Vilha, Família -> Famílhia          |
| `monotongacao_ei_para_ai`                                        | Converte o ditongo 'ei' para 'âi'.                                          | Leite -> Lâite                              |
| `monotongacao`                                                   | Substitui ditongos por equivalentes monofônicos.                            | Maneira -> Manêra, Leite -> Lête            |
| `apocope_do_o`                                                   | Apócope do 'o' final.                                                       | Fogo -> Fôgue                               |
| `enfase_anasalado_final_com_e`                                   | Enfatiza o som nasal com 'e'.                                               | Meu -> Mê, Bem -> Bêm                       |
| `paragoge_em_i`                                                  | Adiciona 'i' após o 'r' final.                                              | Fazer -> Fazêri, Dizer -> Dizêri            |
| `paragoge_em_e`                                                  | Mantém o 'e' final em verbos.                                               | Fazer -> Fazêre, Comer -> Comêre            |
| `perda_silaba_intermedia_palavras_esdruxulas`                    | Remove sílabas intermediárias em palavras esdrúxulas.                       | Fenômeno -> Fenomo, Capítulo -> Capito      |
| `perda_som_o_masculino_quando_passado_plural`                    | Mantém o som tônico de 'ô' em palavras no plural ou feminino.               | Ovos -> Ôvos, Jogos -> Jôgos                |
| `substituicao_de_z_por_j_ligacoes_palavras_acabadas_s_com_vogal` | Substitui 'z' por 'j' entre palavras que terminam em 's' seguidas de vogal. | Quis entrar -> Quij entrar                  |
| `acentuacao_ditongos`                                            | Aplica acentuação em ditongos.                                              | Eu -> Ieu, Bem -> Beim                      |
| `perda_do_i_entre_consoantes`                                    | Remove o 'i' entre consoantes.                                              | Filipe -> Flipe, Lisboa -> Lsboa            |
| `abrir_ditongos`                                                 | Abre ditongos para formas mais abertas.                                     | Mãe -> Mánhe, Cães -> Cáinhes               |
| `substituicao_de_elh_por_alh`                                    | Substitui 'elh' por 'âlh'.                                                  | Coelho -> Coâlho                            |
| `substituicao_final_de_agem_por_aije`                            | Substitui 'agem' por 'aije'.                                                | Viagem -> Viaije                            |
| `substituicao_final_de_ao_por_oum`                               | Substitui o final 'ão' por 'oum'.                                           | Pão -> Poum, Mão -> Moum                    |
| `substituicao_de_en_por_ein`                                     | Substitui 'en' por 'éin', exceto quando seguido de vogal.                   | Casamento -> Casameinto                     |
| `acentuacao_elh`                                                 | Substitui 'elh' por 'eilh'.                                                 | Coelho -> Coeilho                           |
| `suavizacao_elh`                                                 | Substitui 'elh' por 'êlh'.                                                  | Coelho -> Coêlho                            |
| `acentuacao_ach`                                                 | Insere 'i' antes de 'ach'.                                                  | Bolacha -> Bolaicha                         |
| `substituicao_de_z_por_x`                                        | Substitui 'z' por 'x'.                                                      | Zebra -> Xebra                              |
| `substituicao_de_s_por_x`                                        | Substitui 'ss' por 'x' e ajusta casos com 's' e 'c'.                        | Passo -> Paxo, Cinco -> Xinco, Seis -> Xeis |
| `ditongacao_crescente`                                           | Aplica ditongação crescente em palavras específicas.                        | Porto -> Puorto, Bolo -> Buolo              |
| `paragoge_em_e_apos_z`                                           | Adiciona um 'e' no final de palavras terminadas em 'z'.                     | Nariz -> Narize                             |
| `substituicao_a_para_e_antes_de_nasal`                           | Substitui 'a' por 'ê' antes de sons nasais, exceto se houver um 'c' antes.  | Pestana -> Pestêna, Montanha -> Montênha    |
| `substituicao_de_al_por_aur`                                     | Substitui 'al' por 'aur' em palavras do dialeto minhoto central.            | Alguidar -> Aurguidar                       |
| `s_reverso`                                                      | Substitui 's' por 'z' quando está entre vogais ou no final.                 | seis -> zeis, moço -> mozo                  |
| `z_reverso`                                                      | Substitui 'z' por 's' no início da palavra ou no final.                     | zero -> cero, zona -> sona                  |
| `ditongacao_do_e_para_eu`                                        | Substitui 'e' entre consoantes por 'eu'.                                    | treze -> treuze, preto -> preuto            |
| `substituicao_como_por_cumo`                                     | A palavra "como" vira "cumo".                                               | como -> cumo                                |
| `dezoito_com_acento`                                             | "dezóito? tu pedes um biscoito ou um biscóito?"                             | dezoito -> dezóito                          |

## Sotaques

| Sotaque       | Regras Aplicadas                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minho         | `substituicao_v_por_b`, `acentuacao_ditongos`                                                                                                                                                                                                                                                                                                                                                                                   |
| Minho Central | `substituicao_v_por_b`, `acentuacao_ditongos`, `substituicao_de_al_por_aur`                                                                                                                                                                                                                                                                                                                                                     |
| Guimarães     | `substituicao_v_por_b`, `acentuacao_ditongos`, `abrir_ditongos`, `acentuacao_elh`, `acentuacao_ach`, `substituicao_nao_por_num` , `substituicao_como_por_cumo`                                                                                                                                                                                                                                                                  |
| Fafe          | `substituicao_v_por_b`, `acentuacao_ditongos`, `suavizacao_elh`, `substituicao_de_en_por_ein`, `substituicao_de_ou_por_oi`                                                                                                                                                                                                                                                                                                      |
| Madeirense    | `palatizacao_consoante_l_antecedida_por_i`, `paragoge_em_e`, `enfase_anasalado_final_com_e`, `substituicao_de_elh_por_alh`, `perda_do_i_entre_consoantes`, `substituicao_final_de_o_por_e`, `substituicao_final_de_agem_por_age`, `substituicao_final_de_am_por_u`, `substituicao_de_oe_por_on`, `substituicao_de_ae_por_an`, `substituicao_final_de_ar_por_a`, `perda_do_u_final_depois_de_i`, `ditongacao_vogal_tonica_com_u` |
| Famalicão     | `substituicao_v_por_b`, `acentuacao_ditongos`, `substituicao_final_de_ao_por_oum`                                                                                                                                                                                                                                                                                                                                               |
| Lisboa        | `perda_do_i_entre_consoantes`, `monotongacao_ei_para_ai`, `substituicao_de_elh_por_alh`                                                                                                                                                                                                                                                                                                                                         |
| Algarvio      | `enfase_anasalado_final_com_e`, `perda_silaba_intermedia_palavras_esdruxulas`, `perda_som_o_masculino_quando_passado_plural`, `paragoge_em_i`, `apocope_do_o`, `monotongacao`, `suavizacao_elh`, `substituicao_de_z_por_j_ligacoes_palavras_acabadas_s_com_vogal`                                                                                                                                                               |
| Açores        | `palatizacao_consoante_l_antecedida_por_i`, `substituicao_de_oe_por_on`, `substituicao_final_de_oi_por_u`, `perda_do_i_entre_consoantes`, `suavizacao_elh`, `enfase_anasalado_final_com_a`, `perda_do_u_final_depois_de_i`, `u_frances`, `substituicao_de_z_por_j_ligacoes_palavras_acabadas_s_com_vogal`                                                                                                                       |
| Porto         | `substituicao_v_por_b`, `acentuacao_ditongos`, `substituicao_final_de_ao_por_oum`, `ditongacao_crescente`, `dezoito_com_acento`, `substituicao_como_por_cumo`                                                                                                                                                                                                                                                                   |
| Alentejano    | `enfase_anasalado_final_com_e`, `suavizacao_elh`, `paragoge_em_i`, `monotongacao_ei_para_e`                                                                                                                                                                                                                                                                                                                                     |
| Viseu         | `substituicao_v_por_b`, `acentuacao_ditongos`, `substituicao_de_z_por_x`, `substituicao_de_s_por_x`                                                                                                                                                                                                                                                                                                                             |
| Transmontano  | `substituicao_v_por_b`, `substituicao_final_de_agem_por_aije`, `substituicao_de_ou_por_oi`, `substituicao_de_ch_por_tch`, `substituicao_de_z_por_j`, `paragoge_em_e_apos_z`, `substituicao_a_para_e_antes_de_nasal`, `s_reverso`, `z_reverso`                                                                                                                                                                                   |
| Estremenho    | `monotongacao_ei_para_e`, `monotongacao_ou_para_o`                                                                                                                                                                                                                                                                                                                                                                              |
| Beirão        | `paragoge_em_e_apos_z`, `ditongacao_do_e_para_eu`, `s_reverso`, `z_reverso`                                                                                                                                                                                                                                                                                                                                                     |

## Adicionar sotaque

Ajuda a melhorar/Adiciona [o teu sotaque](sotaque_forcado/sotaques)!

exemplo: fafe.json

```json
{
  "substituicao_v_por_b": true,
  "acentuacao_ditongos": true,
  "suavizacao_elh": true,
  "substituicao_de_en_por_ein": true
}
```

exemplo: algarvio.json

```json
{
  "enfase_anasalado_final_com_e": true,
  "perda_silaba_intermedia_palavras_esdruxulas": true,
  "perda_som_o_masculino_quando_passado_plural": true,
  "paragoge_em_i": true,
  "apocope_do_o": true,
  "monotongacao": true,
  "suavizacao_elh": true,
  "substituicao_de_z_por_j_ligacoes_palavras_acabadas_s_com_vogal": true
}
```

template

```json
{
  "substituicao_v_por_b": false,
  "palatizacao_consoante_l_antecedida_por_i": false,
  "apocope_do_o": false,
  "paragoge_em_i": false,
  "paragoge_em_e": false,
  "acentuaçao_ditongos": false,
  "abrir_ditongos": false,
  "enfase_anasalado_final": false,
  "perda_do_i_entre_consoantes": false,
  "perda_do_u_final_depois_de_i": false,
  "perda_silaba_intermedia_palavras_esdruxulas": false,
  "perda_som_o_masculino_quando_passado_plural": false,
  "substituicao_de_z_por_j_ligacoes_palavras_acabadas_s_com_vogal": false,
  "substituicao_de_oe_por_on": false,
  "substituicao_de_ae_por_an": false,
  "substituicao_de_ei_por_ai": false,
  "substituicao_de_ou_por_oi": false,
  "substituicao_de_en_por_ein": false,
  "substituicao_de_ch_por_tch": false,
  "substituicao_de_elh_por_alh": false,
  "substituicao_de_z_por_j": false,
  "substituicao_de_s_por_x": false,
  "substituicao_de_x_por_x": false,
  "substituicao_final_de_o_por_e": false,
  "substituicao_final_de_ar_por_a": false,
  "substituicao_final_de_oi_por_u": false,
  "substituicao_final_de_am_por_u": false,
  "substituicao_final_de_ao_por_oum": false,
  "substituicao_final_de_agem_por_aije": false,
  "acentuacao_ach": false,
  "acentuacao_elh": false,
  "suavizacao_elh": false,
  "monotongacao_ou_para_o": false,
  "monotongacao_ei_para_e": false,
  "monotongacao_ei_para_ai": false,
  "ditongacao_vogal_tonica_com_u": false,
  "u_frances": false
}
```

## Referências

- http://ww3.aeje.pt/avcultur/hjco/GramCom/Cap06_02.htm
- https://pt.wikipedia.org/wiki/Dialetos_da_l%C3%ADngua_portuguesa
- https://pt.wikipedia.org/wiki/Dialeto_estremenho
- https://pt.wikipedia.org/wiki/Dialeto_madeirense
- https://pt.wikipedia.org/wiki/Dialeto_transmontano
- https://pt.wikipedia.org/wiki/Dialeto_algarvio
- https://pt.wikipedia.org/wiki/Dialeto_alentejano
- https://pt.wikipedia.org/wiki/Dialeto_a%C3%A7oriano
- https://www.reddit.com/r/portugal/comments/32b81c/diferen%C3%A7as_entre_sotaques/
- https://www.reddit.com/r/Portuguese/comments/mu95g9/what_are_some_accents_of_portugal_and_what
- https://www.reddit.com/r/Portuguese/comments/p5qx9q/quais_s%C3%A3o_os_diferentes_sotaques_das_regi%C3%B5es_de/