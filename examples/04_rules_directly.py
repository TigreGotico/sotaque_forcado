"""Example — call individual rule functions without a Sotaque.

Run::

    python examples/04_rules_directly.py
"""


def main() -> None:
    try:
        from sotaque_forcado.preprocessors import (
            substituicao_v_por_b,
            substituicao_de_ou_por_oi,
            monotongacao,
            apocope_do_o,
            substituicao_de_z_por_j_ligacoes_palavras_acabadas_s_com_vogal as liaison,
        )
    except Exception as exc:
        print("skipped: preprocessors not importable:", exc)
        print("install the core requirements: pip install -r requirements.txt")
        return

    print("substituicao_v_por_b('vila')        ->", substituicao_v_por_b("vila"))
    print("substituicao_de_ou_por_oi('outro')  ->", substituicao_de_ou_por_oi("outro"))
    print("monotongacao('leite')               ->", monotongacao("leite"))
    print("monotongacao('maneira')             ->", monotongacao("maneira"))
    print("apocope_do_o('fogo')                ->", apocope_do_o("fogo"))

    # the liaison rule turns a trailing 's' into 'j' before a vowel-initial word
    print("liaison('quis', 'entrar')           ->", liaison("quis", "entrar"))
    print("liaison('quis', 'falar')            ->", liaison("quis", "falar"))


if __name__ == "__main__":
    main()
