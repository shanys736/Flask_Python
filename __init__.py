n = int(input("Combien de nombres souhaitez-vous entrer ? "))
max_value = None

for i in range(n):
    num = int(input(f"Entrez le nombre {i + 1}: "))

    if max_value is None:
        max_value = num
    elif num > max_value:
        max_value = num

print("La valeur maximale est :", max_value)
```
