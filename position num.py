"""L1 = [1, 2, 0, 3, 5, 0, 6, 7, 9, 8, 0]
for i in L1:
    L1.append(L1.pop(L1.index(0)))
    print(L1)"""


L1 = [1, 2, 0, 3, 5, 0, 6, 7, 9, 8,0]

non_zero_elements = [x for x in L1 if x != 0]
zero_count = L1.count(0)
result = non_zero_elements + [0] * zero_count

print("Result:", result) 