flour_price = float(input())
kg_flour = float(input())
kg_suger = float(input())
eggs = int(input())
yeast = int(input())
suger_price = flour_price - (flour_price * 0.25)
price_eggs = flour_price + (flour_price * 0.1)
price_yeast = suger_price - (suger_price * 0.8)

total_price = (flour_price * kg_flour) + (kg_suger * suger_price) + (eggs * price_eggs) + (yeast * price_yeast)

print(f'{total_price:.2f}')