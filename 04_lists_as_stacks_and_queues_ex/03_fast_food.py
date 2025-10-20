from collections import deque


quantity_of_food = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))

while orders and  orders[0] <= quantity_of_food:
    current_order = orders.popleft()
    quantity_of_food -= current_order

if orders:
    print(f"Orders left: {' '.join(map(str, orders))}")
else:
    print("Orders complete")
