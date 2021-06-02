data = input()

companys = {}

while not data == "End":
    company_name, id = data.split(" -> ")
    if company_name not in companys:
        companys[company_name] = []
    if id not in companys[company_name]:
        companys[company_name].append(id)

    data = input()

sorted_companys = sorted(companys.items(), key=lambda kvp: kvp[0])

for company, id in sorted_companys:
    print(company)
    for each in id:
        print(f"-- {each}")

# for val in companys.values():
#     print(val)
