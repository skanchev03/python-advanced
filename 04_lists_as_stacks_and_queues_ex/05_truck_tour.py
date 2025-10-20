from collections import  deque


n = int(input())
gas_stations = deque()

for _ in range(n):
    fuel, distance = [int(x) for x in input().split()]
    gas_stations.append((fuel, distance))

starting_position = 0
gas_stations_visited = 0

while gas_stations_visited < n:
    fuel_in_truck = 0
    for fuel, distance in gas_stations:
        fuel_in_truck += fuel
        if fuel_in_truck < distance:
            gas_stations.rotate(-1)
            starting_position += 1
            gas_stations_visited = 0
            break
        fuel_in_truck -= distance
        gas_stations_visited += 1

print(starting_position)
