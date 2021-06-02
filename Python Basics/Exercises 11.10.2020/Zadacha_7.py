import math

rekord = float(input()) #v sekundi
raztoqnie = float(input()) # v metri
vreme_za_edin_metur = float(input()) # vreme za izpluvane na 1 metar

#съпротивлението на водата го забавя на всеки 15 м. с 12.5
#секунди

zakusnenie_ot_saprotivlenie = math.floor(raztoqnie / 15) * 12.5   # v sekundi
#zabavqne_ot

vreme_na_Ivancho = raztoqnie * vreme_za_edin_metur + zakusnenie_ot_saprotivlenie

razlika_ot_rekord = abs(rekord - vreme_na_Ivancho)

if rekord > vreme_na_Ivancho:
    print(f'Yes, he succeeded! The new world record is {vreme_na_Ivancho:.2f} seconds.')
else:
    print(f'No, he failed! He was {razlika_ot_rekord:.2f} seconds slower.')