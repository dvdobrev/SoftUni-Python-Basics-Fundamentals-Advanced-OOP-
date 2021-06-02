commands_number = int(input())

registered_users = {}

for n in range(commands_number):
    data = input().split()
    command = data[0]
    user = data[1]

    if command == "register":
        license_number = data[2]
        if user in registered_users:
            print(f"ERROR: already registered with plate number {license_number}")
        else:
            registered_users[user] = license_number
            print(f"{user} registered {license_number} successfully")

    elif command == "unregister":
        if not user in registered_users:
            print(f"ERROR: user {user} not found")
        else:
            removed = registered_users.pop(user)
            print(f"{user} unregistered successfully")
    #data = input().split()

for user, license_number in registered_users.items():
    print(f"{user} => {license_number}")
