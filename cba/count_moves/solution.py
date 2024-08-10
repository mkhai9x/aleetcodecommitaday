def solution(S, T):
    # Convert strings to lists of integers to easily manipulate the digits
    S = list(map(int, S))
    T = list(map(int, T))

    n = len(S)
    moves = 0
    diff = []
    for i in range(n):
        if T[i] > S[i]:
            _diff = T[i] - S[i]
        elif T[i] < S[i]:
            _diff = 10 + T[i] - S[i]
        else:
            _diff = 0

        diff.append(_diff)

    print(diff)

    for i in range(n):
        next_index = (i + 1) % n
        print(i, next_index)

        if diff[i] != 0 and diff[next_index] != 0:
            moves += min(diff[i], diff[next_index])
            if diff[i] >= diff[next_index]:
                diff[i] = diff[i] - diff[next_index]
                diff[next_index] = 0
            else:
                diff[next_index] = diff[next_index] - diff[i]
                diff[i] = 0
            print(diff)
    print(moves)

    return moves if sum(diff) == 0 else -1


s = "115"
t = "116"


s = "557"
t = "557"

s = "13471"
t = "59604"

s = "557"
t = "403"
print(solution(s, t))
