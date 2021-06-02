#1. Брой страници в текущата книга – цяло число;
#2. Страници, които може да прочита за 1 час – цяло число;
#3. Броя на дните, за които трябва да прочете книгата – цяло число;
#Да се отпечата на конзолата броят часове, които Жоро трябва да отделя за четене всеки ден.
#212
#20
#2
#5.3


stranici = int(input())
stranici_za_chas = int(input())
dni = int(input())
str_na_den = stranici / dni
chasov_na_den = str_na_den / stranici_za_chas
print(chasov_na_den)
