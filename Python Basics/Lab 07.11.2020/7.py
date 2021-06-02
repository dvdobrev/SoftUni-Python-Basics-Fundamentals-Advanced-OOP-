film_name = input()
student = 0
standard = 0
kid = 0
total_tickets = 0

while film_name != 'Finish':
    a = student + standard + kid
    free_seats = int(input())
    ticket_type = input()
    tickets = 0
    while ticket_type != 'End':
        free_seats = free_seats
        if ticket_type == 'student':
            student += 1
            tickets += 1
            total_tickets += 1
        elif ticket_type == 'standard':
            standard += 1
            tickets += 1
            total_tickets += 1
        elif ticket_type == 'kid':
            kid += 1
            tickets += 1
            total_tickets += 1
        if tickets == free_seats:
            print(f'{film_name} - {(tickets / free_seats) * 100:.2f}% full.')
            break
        ticket_type = input()
    else:
        print(f'{film_name} - {(tickets / free_seats) * 100:.2f}% full.')
    film_name = input()
print(f'Total tickets: {total_tickets}')
print(f'{(student / (student + standard + kid)) * 100:.2f}% student tickets.')
print(f'{(standard / (student + standard + kid)) * 100:.2f}% standard tickets.')
print(f'{(kid / (student + standard + kid)) * 100:.2f}% kids tickets.')

