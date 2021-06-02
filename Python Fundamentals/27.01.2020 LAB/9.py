# High = 89#Low = 28#Medium = 77#Low = 23

cells = input().split("x")
water = int(input())
rescued_cells = []
Effort = 0
total_fire = 0

for each_cell in cells:
    each_cell = each_cell.split("=")
    water_needed = int(each_cell[1])
    if water > water_needed:
        if each_cell[0] == "High" and 81 < water_needed < 125:
            water -= water_needed
            Effort += water_needed * 0.25
            total_fire += water_needed
            rescued_cells.append(water_needed)

        elif each_cell[0] == "Medium" and 51 < water_needed < 80:
            water -= water_needed
            Effort += water_needed * 0.25
            total_fire += water_needed
            rescued_cells.append(water_needed)

        elif each_cell[0] == "Low" and 1 < water_needed < 50:
            water -= water_needed
            Effort += water_needed * 0.25
            total_fire += water_needed
            rescued_cells.append(water_needed)

    else:
        continue
print("Cells:")

for each_rescued_cell in rescued_cells:
    print(f" - {each_rescued_cell}")

print(f"Effort: {Effort}")
print(f"Total Fire: {total_fire}")


