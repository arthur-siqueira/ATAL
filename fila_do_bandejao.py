import sys

while True:
    try:
        # 1. Ler N e K
        linha_nk = sys.stdin.readline()
        if not linha_nk:
            break

        N, K = map(int, linha_nk.split())

        linha_posicoes = sys.stdin.readline()

        if N > 1 and not linha_posicoes.strip():
            break

        a = list(map(int, linha_posicoes.split()))

        posicoes = [0] + a

        posicoes.sort()

        distancias = []
        for i in range(N - 1):
            dist = posicoes[i+1] - posicoes[i]
            distancias.append(dist)

        distancias.sort(reverse=True)

        total_span = posicoes[-1] - posicoes[0]

        soma_das_lacunas = sum(distancias[:K-1])

        resultado = total_span - soma_das_lacunas

        print(resultado)

    except EOFError:
        break
    except Exception:
        break