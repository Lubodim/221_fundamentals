n = int(input())

all_invitations = [input() for _ in range(n)]

arrived_guests = set()

while True:
    command = input()
    if command == "END":
        break
    arrived_guests.add(command)

missing_guests = set(all_invitations) - arrived_guests

teachers_invitations = sorted(inv for inv in missing_guests if inv[0].isdigit())
students_invitations = sorted(inv for inv in missing_guests if not inv[0].isdigit())

print(len(missing_guests))
print("\n".join(teachers_invitations))
print("\n".join(students_invitations))