data = list(map(int,input().split(", ")))

positive = [str(num) for num in data if num >= 0]
negative = [str(num) for num in data if num < 0]
even = [str(num) for num in data if num % 2 == 0]
odd = [str(num) for num in data if num % 2 != 0]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")