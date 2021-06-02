daljina = int(input())
shirina = int(input())
visochiina = int(input())
procent_za_obem = float(input())
 
#Един литър вода се равнява на един кубичен дециметър/ 1л=1 дм3/.

obem = daljina * shirina * visochiina
obhsto_litri = obem * 0.001
procent = procent_za_obem * 0.01
izp_obem = obem * procent_za_obem / 100 * 0.001


litri = obhsto_litri - izp_obem


print(litri)