n = int(input())
parking = set()

for _ in range(n):
    in_or_out, plate_number = input().split(", ")

    if in_or_out == "IN":
        parking.add(plate_number)
    else:
        parking.remove(plate_number)

if parking:
    print(*parking, sep="\n")
else:
    print("Parking Lot is Empty")
