import os


def suurima_faili_leidmine(kaust):
    suurim_suurus = 0
    suurim_fail = ""
    for element in os.listdir(kaust):
        if os.path.isdir(os.path.join(kaust, element)):
            suurus = suurima_faili_leidmine(os.path.join(kaust, element))[1]
            element = suurima_faili_leidmine(os.path.join(kaust, element))[0]
        else:
            suurus = os.path.getsize(os.path.join(kaust, element))
        
        if suurus > suurim_suurus:
            suurim_suurus = suurus
            suurim_fail = element
    return [suurim_fail, suurim_suurus]


print(suurima_faili_leidmine("C:\\Users\\Eduard Leibur\\Documents\\MS Visual Studio Code projektid\\projekt\\tunnitööd"))
