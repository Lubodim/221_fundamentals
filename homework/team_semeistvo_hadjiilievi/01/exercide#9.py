clients = []
paid_clients = []

while True:
    user_input = input()
    if user_input == "PAID":
        for client in clients:
            paid_clients.append(client)
        clients.clear()
    elif user_input == "END":
        break
    else:
        clients.append(user_input)


for client in paid_clients:
    print(client)

length = len(clients)
print(f'{length} people remaining.')
