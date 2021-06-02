daljina = int(input()) / 10
shirina = int(input()) /10
visochiina = int(input()) /10
procent_za_obem = float(input())

#Един литър вода се равнява на един кубичен дециметър/ 1л=1 дм3/.

obem = daljina * shirina * visochiina
izp_obem = obem * procent_za_obem / 100

litri = obem - izp_obem
print(litri)