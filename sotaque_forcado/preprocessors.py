import re
from typing import List, Optional


def substituicao_v_por_b(w: str) -> str:
    """
    Replace 'v' with 'b'. Examples: Vila -> Bila, Votar -> Botar, Dívida -> Díbida.
    """
    return w.replace("v", "b")


def substituicao_de_ou_por_oi(w: str) -> str:
    """
    Replace 'ou' with 'oi'. Examples: outro -> oitro, Mouro -> Moiro.
    """
    if len(w) > 2:
        if w.endswith("ou"):
            w = w[:-2].replace("ou", "oi") + "ou"
        else:
            w = w.replace("ou", "oi")
    return w


def substituicao_de_z_por_j(w: str) -> str:
    """
    Replace 'z' with 'j'. Examples: Jesus -> Jejus, Azar -> Ajar.
    """
    w = w.replace("z", "j")
    w = w.replace("esu", "eju")
    return w


def substituicao_de_ch_por_tch(w: str) -> str:
    """
    Strengthen the 'ch' sound by adding a 't'. Examples: Chão -> Tchão, Chouriço -> Tchoiriço.
    """
    w = w.replace("ch", "tch").replace("x", "tx")
    return w


def substituicao_final_de_ar_por_a(w: str) -> str:
    """
    Replace final 'ar' with 'á'. Example: passar -> passá.
    """
    if w.endswith("ar"):
        w = w[:-2] + "á"
    return w


def substituicao_final_de_o_por_e(w: str) -> str:
    """
    Replace final 'o' with 'e'. Examples: osso -> osse, carro -> carre, macaco -> macaque.
    """
    if w.endswith("o") and not w.endswith("ão") and len(w) > 2:
        if w.endswith("co"):
            w = w[:-1] + "que"
        elif w.endswith("go"):
            w = w[:-1] + "gue"
        else:
            w = w[:-1] + "e"
    return w


def substituicao_final_de_oi_por_u(w: str) -> str:
    """
    Replace final 'oi' with 'û'. Example: boi -> bû.
    """
    if len(w) > 2 and w.endswith("oi"):
        w = w[:-2] + "û"
    return w


def substituicao_final_de_am_por_u(w: str) -> str:
    """
    Replace final 'am' with 'u'. Examples: ficaram -> ficáru, foram -> fôru.
    """
    if w.endswith("am"):
        if w.endswith("aram"):
            w = w[:-4] + "áru"
        elif w.endswith("oram"):
            w = w[:-4] + "ôru"
        else:
            w = w[:-2] + "u"
    return w


def substituicao_de_ae_por_an(w: str) -> str:
    """
    Replace 'ães' with 'ân'. Example: cães -> cãns.
    """
    return w.replace("ães", "ân")


def ditongacao_crescente(w: str) -> str:
    """Ditongação crescente
    Porto -> Puorto
    Bolo -> Buolo
    """
    if w.startswith("por"):
        w = "puor" + w[3:]
    if w.startswith("bol"):
        w = "buol" + w[3:]
    return w


def paragoge_em_e_apos_z(w: str) -> str:
    """Adiciona um 'e' no final de palavras terminadas em 'z'.
    exemplo: nariz -> narize"""
    if w.endswith("z"):
        w = w + "e"
    return w


def substituicao_a_para_e_antes_de_nasal(w: str) -> str:
    """Muda 'a' para 'ê' antes de sons nasais ('n', 'm'), exceto se houver um 'c' antes.
    exemplos: pestana > pestêna, montanha > montênha, cana -> cana (não modifica)"""
    # Regex para 'a' seguido de sons nasais ('n', 'm'), exceto se houver um 'c' antes
    w = re.sub(r'(?<!c)a(?=[nm])', 'ê', w)
    return w


def substituicao_de_al_por_aur(w: str) -> str:
    """Passagem de 'al' para 'aur' no minhoto central
    exemplo: alguidar > aurguidar"""
    if len(w) > 3:
        w = w.replace('al', 'aur')
    return w


def substituicao_de_oe_por_on(w: str) -> str:
    """
    Replace 'ões' with 'ôns'. Example: leões -> leôns. verões -> verôns.
    """
    return w.replace("ões", "ôns")


def u_frances(w: str) -> str:
    """
    Apply the 'french u' sound .
    Example: tu -> tiú, müla -> miula
    """
    if w == "tu":
        w = "tiú"
    # palavras terminadas com "o" são mais parecidas com o som "u"
    elif len(w) > 2 and w.endswith("o") and w[-2] != "ã":
        w = w[:-1] + "iú"
    return w


def substituicao_como_por_cumo(w):
    if w == "como":
        return "cumo"
    return w


def dezoito_com_acento(w):
    # "tu pedes um biscoito ou um biscóito?"
    if w == "dezoito":
        w = "dezóito"
    return w


def substituicao_nao_por_num(w):
    if w == "não":
        w = "num"
    return w


def s_reverso(w):
    """In standard Portuguese, "s" has a typical pronunciation, but in Transmontano, it might sound more like "z":

    seis -> zeis
    moço -> mozo
    """

    w = w.replace("ç", "z")
    # Apply 's' to 'z' transformation, considering context
    # Example: replacing 's' with 'z' when it is between vowels or at the end
    # bazilha -> bacilha
    w = re.sub(r'(?<=[aeiou])s(?=[aeiou])', 'z', w)
    return w


def z_reverso(w):
    """In standard Portuguese, "z" is pronounced as [z], but in the Transmontano dialect, it might sound more like "s":
    zero -> cero
    zona -> sona
    """
    # Replace 'z' with 's' if it is at the beginning of the word and followed by a vowel
    # seis -> zeis
    w = re.sub(r'^z(?=[aeiou])', 's', w)
    if len(w) > 2 and w.startswith("se"):
        w = "ce" + w[2:]

    # Replace 'ez' at the end of the word with 'és'
    if w.endswith("ez"):
        w = "és" + w[:-2]
    return w


def ditongacao_do_e_para_eu(w):
    """
    Apply diphthongization rules to the vowel 'e'.

    Examples:
    - "treze" -> "treuze"
    - "preto" -> "preuto"

    Args:
    - w (str): The input word.

    Returns:
    - str: The transformed word.
    """
    # replace 'e' between consonants with 'eu'
    w = re.sub(r'(?<=[^aeiou])e(?=[^aeiou])', 'eu', w)
    return w


def ditongacao_vogal_tonica_com_u(w: str) -> str:
    """
    Add 'u' before the tonic vowel. Example: olho -> uôlho, livro -> lúivro.
    """
    if w.startswith("li"):
        w = "lúi" + w[2:]
    elif w.startswith("olh"):
        w = "uôlh" + w[3:]
    else:
        w = w.replace("iga", "úiga")
    return w


def enfase_anasalado_final_com_a(w: str) -> str:
    """
    Emphasize nasal sound with 'a'. Example: o quê -> o quâ.
    """
    w = w.replace("quê", "quâ")
    if w.endswith("em") and not w.endswith("gem"):
        w = w[:-2] + "ã"
    w = substituicao_final_de_ar_por_a(w)
    return enfase_anasalado_final_com_e(w)


def perda_do_u_final_depois_de_i(w: str) -> str:
    """
    Remove final 'u' after 'i'. Example: viu -> vi.
    """
    if w.endswith("iu"):
        w = w[:-1]
    return w


def palatizacao_consoante_l_antecedida_por_i(w: str) -> str:
    """
    Palatalize 'l' when preceded by 'i'. Example: vila -> vilha, família -> famílhia.
    """
    w = w.replace("il", "ilh").replace("íl", "ílh")
    # TODO  - dont replace if next letter is already an h
    # avoid bug -> pastilha -> pastilhha
    w = w.replace("lhh", "lh")
    return w


def monotongacao_ei_para_ai(w: str) -> str:
    """
    Convert 'ei' diphthong to 'âi'. Example: leite -> lâite.
    """
    if "ei" in w:
        w = w.replace("ei", "âi")
    return w


def monotongacao(w: str, target_dits: Optional[List[str]] = None) -> str:
    """
    Replace diphthongs with their monophthong equivalents.
    """
    ditongs = {
        "éi": "é",
        "éu": "é",
        # "ái": "á", # TODO "ai" vs '"a i" de "ainda"' - não deve ser modificado
        "ei": "ê",
        "ou": "ô",
        "õe": "õ",
        "ão": "ã"
    }
    target_dits = target_dits or list(ditongs)

    # monotongação dos ditongos, como "manêra" (maneira), "lête" (leite),
    # "ôtro" (outro), "animás" (animais), "chapé" (chapéu), "fêjõs" (feijões),
    # "sês" (seis), "pã" (pão), "papés" (papéis).
    if len(w) > 2:
        for k, v in ditongs.items():
            if k not in target_dits:
                continue
            w = w.replace(k, v)
    return w


def apocope_do_o(w: str) -> str:
    """
    Apocope of final 'o'. Example: fogo -> fôg.
    cumprimento -> cumpriment, fervid -> fervid, amigo -> amig
    """
    #
    if w.endswith("ogo"):
        w = w[:-3] + "ôg"
    elif w.endswith("o") and w[-1] in "shçc":
        w = w[:-1] + "e"
    elif w.endswith("o") and len(w) > 2:
        w = w[:-1]
    if w.endswith("g"):  # otherwise reads as "j", we want "g"
        w = w + "ue"  # ensure ending with "gue"
    return w


def enfase_anasalado_final_com_e(w: str) -> str:
    """
    Emphasize nasal sound with 'e'. Example: meu -> mê, bem -> bêm.
    """
    if w == "meu":
        w = "mê"
    elif w.endswith("em") or w.endswith("ém"):
        w = w[:-2] + "êm"
    elif w.endswith("na"):
        w = w[:-2] + "nã"
    elif w.endswith("re"):
        w = w[:-2] + "rê"
    return w


def paragoge_em_i(w: str) -> str:
    """
    Add 'i' after final 'r'. Example: fazer -> fazêri, dizer -> dizêri, dormir -> dormiri
    """
    if w.endswith("er"):
        w = w[:-2] + "êri"
    elif w.endswith("ir"):
        w = w[:-2] + "íri"
    elif w.endswith("r"):
        w = w + "i"
    return w


def paragoge_em_e(w: str) -> str:
    """
    Preserve final 'e' in verbs. Example: fazer -> fazêre, comer -> comêre, falar -> falare
    """
    if w.endswith("r"):
        if w.endswith("rrer"):
            w = w[:-2] + "oerê"
        elif w.endswith("er"):
            w = w[:-2] + "êre"
        elif w.endswith("ir"):
            w = w[:-2] + "íri"
        else:
            w += "e"
    return w


def perda_silaba_intermedia_palavras_esdruxulas(w: str) -> str:
    """
    Remove the intermediate syllable in esdrúxulas words.

    Examples:
    - "fenómeno" -> "fenomo"
    - "triângulo" -> "triango"
    - "capítulo" -> "capito"
    - "estômago" -> "estômo"
    - "árvore" -> "arve"

    Args:
    - w (str): The input word.

    Returns:
    - str: The transformed word.
    """
    if w == "fenómeno":
        w = "fenomo"
    elif w == "triângulo":
        w = "triango"
    elif w == "capítulo":
        w = "capito"
    elif w == "estômago":
        w = "estômo"
    elif w == "árvore":
        w = "arve"
    return w


def perda_som_o_masculino_quando_passado_plural(w: str) -> str:
    """
    Maintain the tonic 'ô' sound in masculine words when converted to plural or feminine.

    Examples:
    - "ovos" -> "ôvos"
    - "carinhosa" -> "carinhôsa"
    - "jogos" -> "jôgos"
    - "manhôsa" -> "manhôsas"

    Args:
    - w (str): The input word.

    Returns:
    - str: The transformed word.
    """
    if w == "ovos":
        w = "ôvos"
    elif w == "carinhosa":
        w = "carinhôsa"
    elif w == "jogos":
        w = "jôgos"
    elif "nhos" in w:
        w = w.replace("nhos", "nhôs")
    return w


def substituicao_de_z_por_j_ligacoes_palavras_acabadas_s_com_vogal(w: str, nextw: Optional[str]) -> str:
    """
    Replace 'z' with 'j' in the linkage of words ending in 's' followed by a vowel.

    Examples:
    - "quis entrar" -> "quij entrar"
    - "mas a água" -> "maj a água"

    Args:
    - w (str): The current word.
    - nextw (Optional[str]): The next word in the sequence.

    Returns:
    - str: The transformed word.
    """
    if nextw and w.endswith("s") and nextw[0] in "aeiou":
        w = w[:-1] + "j"
    return w


def acentuacao_ditongos(w: str) -> str:
    """
    Apply accentuation rules to diphthongs.

    Examples:
    - "eu" -> "ieu"
    - "em" -> "eim"
    - "quê" -> "quiê"

    Args:
    - w (str): The input word.

    Returns:
    - str: The transformed word.
    """
    w = w.replace("eu", "ieu")
    # bem -> beim
    w = w.replace("em", "eim")
    # o quê -> o quiê
    w = w.replace("quê", "quiê")
    return w


def perda_do_i_entre_consoantes(w: str) -> str:
    """
    Remove the 'i' between consonants.

    Examples:
    - "Filipe" -> "Felipe"
    - "Lisboa" -> "Lesboa"

    Args:
    - w (str): The input word.

    Returns:
    - str: The transformed word.
    """
    w = re.sub(r'(?<=[^aeiouhx])i(?=[^aeiougçcvh])', 'e', w, count=1)
    return w


def abrir_ditongos(w: str) -> str:
    """
    Open diphthongs to more open forms.

    Examples:
    - "mãe" -> "mánhe"
    - "cães" -> "cáinhes"

    Args:
    - w (str): The input word.

    Returns:
    - str: The transformed word.
    """
    if w == "mãe":
        w = "mánhe"
    elif w.endswith("ães"):
        w = w[:-3] + "áinhes"
    return w


def substituicao_de_elh_por_alh(w: str) -> str:
    """
    Replace 'elh' with 'âlh', except when 'elh' is preceded by 'v'.

    Examples:
    - "coelho" -> "coâlho"
    - "vermelho" -> "vermâlho"
    - "velho" -> "velho" (no change, since 'elh' is preceded by 'v')

    Args:
    - w (str): The input word.

    Returns:
    - str: The transformed word.
    """
    # Define the pattern: 'elh' not preceded by 'v'
    pattern = r'(?<!v)elh'
    # Replace 'elh' with 'âlh' where the pattern matches
    result = re.sub(pattern, 'âlh', w)
    return result


def substituicao_final_de_agem_por_aije(w: str) -> str:
    """
    Replace the ending 'agem' with 'aije'.

    Examples:
    - "viagem" -> "viaije"
    - "garagem" -> "garaije"

    Args:
    - w (str): The input word.

    Returns:
    - str: The transformed word.
    """
    if w.endswith("agem"):
        w = w[:-4] + "aije"
    return w


def substituicao_final_de_ao_por_oum(w: str) -> str:
    """
    Replace the ending 'ão' with 'oum'.

    Examples:
    - "Famalicão" -> "Famalicoum"
    - "coração" -> "coraçoum"
    - "pão" -> "poum"
    - "mão" -> "moum"

    Args:
    - w (str): The input word.

    Returns:
    - str: The transformed word.
    """
    # “oum” em vez de “ão” (ex: Famalicoum, coum, poum, moum, coraçoum)
    if w.endswith("ão"):
        w = w[:-2] + "oum"
    return w


def substituicao_de_en_por_ein(w: str) -> str:
    """
    Replace 'en' with 'éin'.

    Examples:
    - "casamento" -> "casameinto"
    - "doeinte" -> "doeinte"

    Args:
    - w (str): The input word.

    Returns:
    - str: The transformed word.
    """
    # Define the pattern: 'en' not followed by a vowel (a, e, i, o, u)
    pattern = r'en(?![aeiou])'
    # Replace 'en' with 'éin' where the pattern matches
    result = re.sub(pattern, 'éin', w)
    return result


def acentuacao_elh(w: str) -> str:
    """
    Replace 'elh' with 'eilh'.

    Examples:
    - "vermelho" -> "vermeilho"
    - "coelho" -> "coeilho"

    Args:
    - w (str): The input word.

    Returns:
    - str: The transformed word.
    """
    w = w.replace("elh", "eilh")
    return w


def suavizacao_elh(w: str) -> str:
    """
    Replace 'elh' with 'êlh'.

    Examples:
    - "vermelho" -> "vermêlho"
    - "coelho" -> "coêlho"

    Args:
    - w (str): The input word.

    Returns:
    - str: The transformed word.
    """
    w = w.replace("elh", "êlh")
    return w


def acentuacao_ach(w: str) -> str:
    """
    Insert 'i' before 'ch' or 'lh'.

    Examples:
    - "bolacha" -> "bolaicha"

    Args:
    - w (str): The input word.

    Returns:
    - str: The transformed word.
    """
    w = w.replace("ach", "aich")
    return w


def substituicao_de_z_por_x(w: str) -> str:
    """
    Replace 'z' with 'x'.

    Examples:
    - "zebra" -> "xebra"

    Args:
    - w (str): The input word.

    Returns:
    - str: The transformed word.
    """
    w = w.replace("z", "x")
    return w


def substituicao_de_s_por_x(w: str) -> str:
    """
    Replace 'ss' with 'x' and handle special cases for 's' and 'c'.

    Examples:
    - "passo" -> "paxo"
    - "cesso" -> "xesso"
    - "cinco" -> "xinco"
    - "seis" -> "xeis"
    - "sete" -> "xete"

    Args:
    - w (str): The input word.

    Returns:
    - str: The transformed word.
    """
    w = w.replace("ss", "x")
    if any(w.startswith(_) for _ in ["s", "ce", "ci"]):
        w = "x" + w[1:]
    return w
