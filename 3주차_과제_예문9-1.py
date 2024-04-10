total = 0
for i in range(3333, 10000, 1):
    if i%1234 == 0:
        continue

    total += i;
    
    if total + i > 100000:
        break
    
print(f"합계: {total}")
