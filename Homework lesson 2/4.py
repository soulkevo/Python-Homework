price = int(input("Введіть ціну: "))
discount = int(input("Введіть знижку (%): "))

sale_price = price - (price * (discount / 100))

print("Ціна зі знижкою: ", sale_price)