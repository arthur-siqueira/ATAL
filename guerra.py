S_line = input()
S = int(S_line.strip())

Q_line = input()

Q = list(map(int, Q_line.strip().split()))

N_line = input()
N = list(map(int, N_line.strip().split()))
Q.sort()
N.sort()

wins = 0
i = 0
j = 0

while i < S and j < S:
    if N[i] > Q[j]:
        wins += 1
        i += 1
        j += 1
    else:
        i += 1

print(wins)



