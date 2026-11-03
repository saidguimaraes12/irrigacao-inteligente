talhao_1 = {
    "nome" : "Talhão 1",
    "area" : "1 Hectare",
    "umidade" : 68
}

talhao_2 = {
    "nome" : "Talhão 2",
    "area" : "1 Hectare",
    "umidade" : 61
}

talhao_3 = {
    "nome" : "Talhão 3",
    "area" : "1 Hectare",
    "umidade" : 44
}

talhao_4 = {
    "nome" : "Talhão 4",
    "area" : "1 Hectare",
    "umidade" : 31
}

talhoes = [talhao_1, talhao_2, talhao_3, talhao_4]

def precisa_irrigar(umidade, limite):
    if (umidade >= limite):
        return False
    else:
        return True

if __name__ == "__main__":
    irrigacao = []
    for talhao in talhoes:
        if precisa_irrigar(talhao['umidade'], 50):
            print(f"{talhao['nome']}: umidade {talhao['umidade']}% -> precisa irrigar")
            irrigacao.append(talhao)
        else:
            print(f"{talhao['nome']}: umidade {talhao['umidade']}% -> ok")

    irrigacao_ordenada = sorted(irrigacao, key=lambda item: item['umidade'])
    nomes = [item['nome'] for item in irrigacao_ordenada]
    print()
    print(f"Ordem de irrigação: {', '.join(nomes)}")
