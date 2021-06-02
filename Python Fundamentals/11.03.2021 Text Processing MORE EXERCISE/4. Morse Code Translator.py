morse_code = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"}
#a = {"b": 3, "c": 4}
data = input().split()
text = [el.replace("|", " ") for el in data]
for el in text:
    if el == " ":
        print(el, end="")
    if el in morse_code:
        print(morse_code.get(el), end="")




