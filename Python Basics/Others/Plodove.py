cena_qgodi = float(input())
banani = float(input())
portokali = float(input())
malini = float(input())
kg_qgodi = float(input())


cena_malini = cena_qgodi / 2
cena_portokali = cena_malini - (cena_malini * 0.4)
cena_banani = cena_malini - (cena_malini * 0.8)

total_qgodi = cena_qgodi * kg_qgodi
total_banani = banani * cena_banani
total_portokali = portokali * cena_portokali
total_malini = malini * cena_malini

suma = total_qgodi + total_banani + total_portokali + total_malini
print(suma)
