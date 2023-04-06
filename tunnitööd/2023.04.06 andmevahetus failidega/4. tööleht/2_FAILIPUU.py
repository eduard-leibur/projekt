import os


def failipuu(kaust, sügavus):
    for element in os.listdir(kaust):
        if os.path.isdir(os.path.join(kaust, element)):
            sõne = ""
            for i in range(sügavus):
                sõne += "\t"
            sõne += element
            print(sõne)
            failipuu(os.path.join(kaust, element), sügavus + 1)
        else:
            sõne = ""
            for i in range(sügavus):
                sõne += "\t"
            sõne += element
            print(sõne)


failipuu("C:\\Users\\Eduard Leibur\\Documents\\MS Visual Studio Code projektid\\projekt\\tunnitööd", 0)
