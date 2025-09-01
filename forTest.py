s = input()
count = 0
for i in s:
    if count > 0 and i == "Р": count += 1
    if i == "Р" and count == 0: count += 1
print(count)