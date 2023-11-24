n = int(input("Enter number of the invitation:"))

invitation = set()
for _ in range(n):
    invitation.add(input())
while invitation:
    command = input("Enter guest number or 'End' to finish: ")
    if command == "END":
        break
    invitation.discard(command)
print(len(invitation))
print(*sorted(invitation), sep="\n")
