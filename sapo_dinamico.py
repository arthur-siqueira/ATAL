import sys


def resolver():
    try:
        T = int(sys.stdin.readline())
    except ValueError:
        return

    resultados = []
    for case_num in range(1, T + 1):
        line = sys.stdin.readline().split()
        if not line:
            continue

        N = int(line[0])
        D = int(line[1])

        all_stones_pos = [0]
        big_stones_pos = [0]

        if N > 0:
            stones_input = sys.stdin.readline().split()
            for stone_str in stones_input:
                tipo, pos_str = stone_str.split('-')
                pos = int(pos_str)

                all_stones_pos.append(pos)

                if tipo == 'B':
                    big_stones_pos.append(pos)

        all_stones_pos.append(D)
        big_stones_pos.append(D)

        max_jump_ida = 0
        for i in range(1, len(all_stones_pos)):
            jump = all_stones_pos[i] - all_stones_pos[i - 1]
            max_jump_ida = max(max_jump_ida, jump)

        max_jump_volta = 0
        for i in range(1, len(big_stones_pos)):
            jump = big_stones_pos[i] - big_stones_pos[i - 1]
            max_jump_volta = max(max_jump_volta, jump)


        answer = max(max_jump_ida, max_jump_volta)

        resultados.append(f"Case {case_num}: {answer}")

    print("\n".join(resultados))

resolver()