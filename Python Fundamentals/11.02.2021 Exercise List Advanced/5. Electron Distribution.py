electron_numbers = int(input())
shell_index = 1
eletrons = []


while electron_numbers > 0:
    max_numbers_of_electrons_in_shell = 2 * (shell_index ** 2)
    if electron_numbers < max_numbers_of_electrons_in_shell:
        eletrons.append(electron_numbers)
    else:
        eletrons.append(max_numbers_of_electrons_in_shell)

    electron_numbers -= max_numbers_of_electrons_in_shell
    shell_index += 1


print(eletrons)