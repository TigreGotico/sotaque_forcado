import json

from quebra_frases import word_tokenize

from sotaque_forcado.preprocessors import substituicao_v_por_b, substituicao_de_oe_por_on, substituicao_de_ae_por_an, \
    substituicao_de_en_por_ein, substituicao_de_elh_por_alh, substituicao_de_ou_por_oi, substituicao_de_ch_por_tch, \
    substituicao_de_z_por_j, substituicao_de_z_por_x, substituicao_de_s_por_x, substituicao_final_de_agem_por_aije, \
    substituicao_final_de_oi_por_u, substituicao_final_de_o_por_e, substituicao_final_de_ar_por_a, \
    substituicao_final_de_ao_por_oum, substituicao_final_de_am_por_u, ditongacao_vogal_tonica_com_u, \
    substituicao_de_z_por_j_ligacoes_palavras_acabadas_s_com_vogal, monotongacao, monotongacao_ei_para_ai, \
    acentuacao_ditongos, palatizacao_consoante_l_antecedida_por_i, paragoge_em_i, paragoge_em_e, apocope_do_o, \
    enfase_anasalado_final_com_a, suavizacao_elh, perda_do_u_final_depois_de_i, abrir_ditongos, acentuacao_ach, \
    acentuacao_elh, perda_som_o_masculino_quando_passado_plural, perda_silaba_intermedia_palavras_esdruxulas, \
    perda_do_i_entre_consoantes, enfase_anasalado_final_com_e, u_frances, substituicao_nao_por_num, \
    paragoge_em_e_apos_z, substituicao_de_al_por_aur, substituicao_a_para_e_antes_de_nasal, ditongacao_do_e_para_eu, \
s_reverso, z_reverso
from sotaque_forcado.utils import normalize


class Sotaque:
    def __init__(self, config_file):
        self.path = config_file
        with open(config_file, 'r') as file:
            self.rules = json.load(file)

    def __repr__(self):
        return f"Sotaque({self.path.split('/')[-1].split('.json')[0]})"

    def add_accent(self, text: str) -> str:
        text = normalize(text)
        words = word_tokenize(text)
        for idx, w in enumerate(words):
            nextw = words[idx + 1] if idx < len(words) - 1 else ""
            if self.rules.get('substituicao_v_por_b'):
                w = substituicao_v_por_b(w)
            if self.rules.get("s_reverso"):
                w = s_reverso(w)
            if self.rules.get("z_reverso"):
                w = z_reverso(w)
            if self.rules.get("ditongacao_do_e_para_eu"):
                w = ditongacao_do_e_para_eu(w)
            if self.rules.get("substituicao_a_para_e_antes_de_nasal"):
                w = substituicao_a_para_e_antes_de_nasal(w)
            if self.rules.get("paragoge_em_e_apos_z"):
                w = paragoge_em_e_apos_z(w)
            if self.rules.get("substituicao_de_al_por_aur"):
                w = substituicao_de_al_por_aur(w)
            if self.rules.get('substituicao_nao_por_num'):
                w = substituicao_nao_por_num(w)
            if self.rules.get('substituicao_de_oe_por_on'):
                w = substituicao_de_oe_por_on(w)
            if self.rules.get('substituicao_de_ae_por_an'):
                w = substituicao_de_ae_por_an(w)
            if self.rules.get('substituicao_de_en_por_ein'):
                w = substituicao_de_en_por_ein(w)
            if self.rules.get('substituicao_de_elh_por_alh'):
                w = substituicao_de_elh_por_alh(w)
            if self.rules.get('substituicao_de_ou_por_oi'):
                w = substituicao_de_ou_por_oi(w)
            if self.rules.get('substituicao_de_ch_por_tch'):
                w = substituicao_de_ch_por_tch(w)
            if self.rules.get('substituicao_de_z_por_j'):
                w = substituicao_de_z_por_j(w)
            if self.rules.get('substituicao_de_z_por_x'):
                w = substituicao_de_z_por_x(w)
            if self.rules.get('substituicao_de_s_por_x'):
                w = substituicao_de_s_por_x(w)
            if self.rules.get('substituicao_final_de_agem_por_aije'):
                w = substituicao_final_de_agem_por_aije(w)
            if self.rules.get('substituicao_final_de_oi_por_u'):
                w = substituicao_final_de_oi_por_u(w)
            if self.rules.get('substituicao_final_de_o_por_e'):
                w = substituicao_final_de_o_por_e(w)
            if self.rules.get('substituicao_final_de_ar_por_a'):
                w = substituicao_final_de_ar_por_a(w)
            if self.rules.get('substituicao_final_de_ao_por_oum'):
                w = substituicao_final_de_ao_por_oum(w)
            if self.rules.get('substituicao_final_de_am_por_u'):
                w = substituicao_final_de_am_por_u(w)
            if self.rules.get('ditongacao_vogal_tonica_com_u'):
                w = ditongacao_vogal_tonica_com_u(w)
            if self.rules.get('substituicao_de_z_por_j_ligacoes_palavras_acabadas_s_com_vogal'):
                w = substituicao_de_z_por_j_ligacoes_palavras_acabadas_s_com_vogal(w, nextw)
            if self.rules.get('monotongacao'):
                w = monotongacao(w)
            if self.rules.get('monotongacao_ei_para_ai'):
                w = monotongacao_ei_para_ai(w)
            if self.rules.get('acentuacao_ditongos'):
                w = acentuacao_ditongos(w)
            if self.rules.get('palatizacao_consoante_l_antecedida_por_i'):
                w = palatizacao_consoante_l_antecedida_por_i(w)
            if self.rules.get('paragoge_em_i'):
                w = paragoge_em_i(w)
            if self.rules.get('paragoge_em_e'):
                w = paragoge_em_e(w)
            if self.rules.get('apocope_do_o'):
                w = apocope_do_o(w)
            if self.rules.get('enfase_anasalado_final_com_a'):
                w = enfase_anasalado_final_com_a(w)
            if self.rules.get('suavizacao_elh'):
                w = suavizacao_elh(w)
            if self.rules.get('perda_do_u_final_depois_de_i'):
                w = perda_do_u_final_depois_de_i(w)
            if self.rules.get('abrir_ditongos'):
                w = abrir_ditongos(w)
            if self.rules.get('acentuacao_ach'):
                w = acentuacao_ach(w)
            if self.rules.get('acentuacao_elh'):
                w = acentuacao_elh(w)
            if self.rules.get('perda_som_o_masculino_quando_passado_plural'):
                w = perda_som_o_masculino_quando_passado_plural(w)
            if self.rules.get('perda_silaba_intermedia_palavras_esdruxulas'):
                w = perda_silaba_intermedia_palavras_esdruxulas(w)
            if self.rules.get('perda_do_i_entre_consoantes'):
                w = perda_do_i_entre_consoantes(w)
            if self.rules.get('enfase_anasalado_final_com_e'):
                w = enfase_anasalado_final_com_e(w)
            if self.rules.get('u_frances'):
                w = u_frances(w)
            words[idx] = w
        return " ".join(words)

    def phonemize(self, text):
        from phonemizer import phonemize
        text = self.add_accent(text)
        return phonemize(text, language="pt")
