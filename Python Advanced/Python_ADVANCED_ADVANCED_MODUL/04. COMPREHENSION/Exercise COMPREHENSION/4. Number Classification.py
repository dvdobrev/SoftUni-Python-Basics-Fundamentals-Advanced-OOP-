# text = [int(el) for el in input().split(", ")]
# positive = print(f"Positive: {', '.join([str(el) for el in text if el >= 0])}")
# negativ = print(f"Negative: {', '.join([str(el) for el in text if el < 0])}")
# even = print(f"Even: {', '.join([str(el) for el in text if el % 2 == 0])}")
# odd = print(f"Odd: {', '.join([str(el) for el in text if not el % 2 == 0])}")

text = [int(el) for el in input().split(", ")]
positive = [el for el in text if el >= 0]
negativ = [el for el in text if el < 0]
even = [el for el in text if el % 2 == 0]
odd = [el for el in text if not el % 2 == 0]
print("Positive: ", end="")
print(*positive, sep=", ")
print("Negative: ", end="")
print(*negativ, sep=", ")
print("Even: ", end="")
print(*even, sep=", ")
print("Odd: ", end="")
print(*odd, sep=", ")