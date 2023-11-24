invitations = []

n = int(input())

for i in range(n):
    invitation = input()
    invitations.append(invitation)

while True:
    attended = input()
    if attended != "END":
        if attended in invitations:
            invitations.remove(attended)
    else:
        break

rearranged_invitations = []

invitations.reverse()

for inv in invitations:
    if inv[0].isdigit():
        rearranged_invitations.insert(0, inv)
    else:
        rearranged_invitations.append(inv)

print(len(rearranged_invitations))
for inv in rearranged_invitations:
    print(inv)