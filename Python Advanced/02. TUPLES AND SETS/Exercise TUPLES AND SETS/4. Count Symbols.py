text = input()

counters = {}

for el in text:
    if el not in counters:
        counters[el] = 1

    else:
        counters[el] += 1

sorted_counters = dict(sorted(counters.items(), key=lambda kvp: kvp[0]))

for k, v in sorted_counters.items():
    print(f"{k}: {v} time/s")