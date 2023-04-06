import matplotlib.pyplot as plt


def silu_andmed(järjend, n):
    tulemus = []
    for i in range(len(järjend)):
        nimetaja_summa = 0
        mitu_arvestatud = 0
        for j in range(n):
            if (j+i-n+1) >= 0:
                mitu_arvestatud += 1
                nimetaja_summa += 1/järjend[i + j - n + 1]
        tulemus.append(mitu_arvestatud / nimetaja_summa)
    return tulemus

andmed = [2, 1, 3, 4, 5, 8, 2, 7, 3, 6, 4, 2]
kuud =   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

plt.plot(kuud, silu_andmed(andmed, 3))
plt.plot(kuud, andmed)
plt.xlabel("Kuud")
plt.ylabel("Hind")

plt.show()
