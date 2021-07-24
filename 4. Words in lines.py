words = list(input().split())
num=1
for i in words:
    print(f"№{num}. {i[:10]}")
    num += 1
