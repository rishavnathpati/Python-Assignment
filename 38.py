def ack(M, N):
    if M == 0:
        return N + 1
    elif N == 0:
        return ack(M - 1, 1)
    else:
        return ack(M - 1, ack(M, N - 1))


print(ack(1, 2))
