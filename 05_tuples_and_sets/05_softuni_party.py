n = int(input())
guests = set()

for _ in range(n):
    guests.add(input())

while True:
    reservation_code = input()

    if reservation_code == "END":
        break
    if reservation_code in guests:
        guests.remove(reservation_code)

print(len(guests))
print(*sorted(guests), sep="\n")
