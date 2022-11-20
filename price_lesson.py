#price = 100
#discount = 50

#price_with_discount = price - (price * discount / 100)
#print(price_with_discount) # наивный код - лучше так не делать

def discounted(price, discount, max_discount=20):
    price = abs(price)
    discount = abs(discount)
    if max_discount >= 100:
        raise ValueError("Максимальная скидка не должна быть больше")
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    return(price_with_discount)


product = {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 5}
product['with_discount'] = (discounted(product['price'], product['discount']))
print(product)