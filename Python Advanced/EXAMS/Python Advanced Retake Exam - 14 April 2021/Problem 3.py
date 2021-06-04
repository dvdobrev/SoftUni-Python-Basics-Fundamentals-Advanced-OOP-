def flights(*args):
    data = [el for el in args]
    flight_dict = {}
    while True:
        flight = data[0]
        if not flight == "Finish":
            passangers = int(data[1])
            if flight not in flight_dict:
                flight_dict[flight] = passangers

            else:
                flight_dict[flight] += passangers

            data.pop(0)
            data.pop(0)

        else:
            break

    return flight_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
