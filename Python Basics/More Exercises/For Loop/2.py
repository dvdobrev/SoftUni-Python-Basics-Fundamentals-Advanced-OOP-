period = int(input())
patient = 0
treated_patient = 7
untreated_patient = abs(patient - treated_patient)
total_treated_patient = 0
total_untreated_patient = 0

for i in range(1, period + 1):
    patient = int(input())
    if i % 3 == 0 and total_untreated_patient > total_treated_patient:
        treated_patient += 1
    if patient <= treated_patient:
        untreated_patient = 0
        treated_patient = patient
    else:
        untreated_patient = abs(patient - treated_patient)
    total_treated_patient += treated_patient
    total_untreated_patient += untreated_patient

print(f'Treated patients: {total_treated_patient}.')
print(f'Untreated patients: {total_untreated_patient}.')
