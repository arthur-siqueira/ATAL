import sys

def saco_do_papai_noel():
    try:
        linha_n = sys.stdin.readline()
        if not linha_n:
            return  # Fim da entrada
        N = int(linha_n.strip())
    except (IOError, ValueError):
        return  # Encerra se não houver mais entrada

    # Itera por cada caso de teste
    for i in range(N):
        try:
            # Lê a quantidade de pacotes
            linha_pac = sys.stdin.readline()
            if not linha_pac:
                break  # Encerra se a entrada terminar inesperadamente
            Pac = int(linha_pac.strip())

            pacotes = []
            for _ in range(Pac):
                linha_pacote = sys.stdin.readline()
                if not linha_pacote:
                    break  # Encerra se a entrada terminar
                qt, peso = map(int, linha_pacote.strip().split())
                pacotes.append({'qt': qt, 'peso': peso})

            if not pacotes and Pac > 0:
                break  # Evita erro se a entrada foi interrompida

            # limite de peso da mochila (saco)
            LIMITE_PESO = 50

            # Inicializa a tabela de Programação Dinâmica
            dp = [[0 for _ in range(LIMITE_PESO + 1)] for _ in range(Pac + 1)]

            # Preenche a tabela de PD
            for i in range(1, Pac + 1):
                # Pega os dados do pacote atual (i-1 pois a lista é 0-indexada)
                qt_atual = pacotes[i - 1]['qt']
                peso_atual = pacotes[i - 1]['peso']

                for j in range(LIMITE_PESO + 1):
                    if peso_atual > j:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = max(dp[i - 1][j], qt_atual + dp[i - 1][j - peso_atual])

            max_brinquedos = dp[Pac][50]

            peso_total = LIMITE_PESO
            while peso_total > 0 and dp[Pac][peso_total - 1] == max_brinquedos:
                peso_total -= 1

            # "backtracking" para descobrir quantos pacotes foram usados
            pacotes_usados = 0
            peso_restante = peso_total

            for i in range(Pac, 0, -1):
                # verifica se o item 'i' foi o responsável pelo aumento no valor
                if dp[i][peso_restante] > dp[i - 1][peso_restante]:
                    pacotes_usados += 1
                    peso_restante -= pacotes[i - 1]['peso']

                    # se o peso zerar não precisa checar mais
                    if peso_restante == 0:
                        break

            pacotes_sobrando = Pac - pacotes_usados

            print(f"{max_brinquedos} brinquedos")
            print(f"Peso: {peso_total} kg")
            print(f"sobra(m) {pacotes_sobrando} pacote(s)")

            if i < N - 1:
                print()

        except (IOError, ValueError):
            break


saco_do_papai_noel()