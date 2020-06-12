import file
import  corrector

print("Probíhá načítání slovníku...", end="")
file = file.File()
file.seradPodleVelikosti()
slovnik = file.ziskejSlovnik()
print(" done")

corrector = corrector.Corrector(slovnik)
veta_k_oprave = input("Zadejte větu k opravě: ")
print("Hledám...", end="")

oprava = list()
for pismeno in ".,!?-+*/\\@#{}[]":
    veta_k_oprave = veta_k_oprave.replace(pismeno, "")

for slovo_k_oprave in veta_k_oprave.split(" "):
    oprava.append(corrector.ziskejOpravy(slovo_k_oprave))

print(" done")
print("\n\nNalezená slova: ")

for x in range(len(veta_k_oprave.split(" "))):
    print(veta_k_oprave.split(" ")[x].lower(), "=> ", end="")
    if oprava[x]:
        for slovo in oprava[x]:
            print(slovo, end=" ")
    else:
        print("Nebylo nalezené žádné podobné slovo")
    print("\n", end="")