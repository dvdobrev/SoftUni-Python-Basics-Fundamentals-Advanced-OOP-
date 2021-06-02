def is_jackpot(ticket):
    for win_symbol in winning_symbols:
        if win_symbol in ticket:
            if ticket.count(win_symbol) == 20:
                print(f"ticket \"{ticket}\" - 10{win_symbol} Jackpot!")
                return True

def is_winning_ticket(ticket):
    left_half = ticket[:10]
    right_half = ticket[10:]
    for win_symbol in winning_symbols:
        if win_symbol*6 in left_half and win_symbol*6 in right_half:
            left_symbol_count = left_half.count(win_symbol)
            right_symbol_count = right_half.count(win_symbol)
            match_result = min(left_symbol_count, right_symbol_count)
            print(f"ticket \"{ticket}\" - {match_result}{win_symbol}")
            return True
    return False

tickets = [el.strip() for el in input().split(", ")]

winning_symbols = ['@', '#', '$', '^']

for ticket in tickets:
    if not len(ticket) == 20:
        print(f"invalid ticket")
        continue

    if is_jackpot(ticket):
        continue

    if is_winning_ticket(ticket):
        continue

    print(f"ticket \"{ticket}\" - no match")


