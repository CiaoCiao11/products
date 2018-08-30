products=[]
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':#quit
       break
    price=input('請輸入價格:')
    products.append([name, price])
print(products)

for p in products:
    print(p[0],'的價格是',p[1])

with open('products.csv','w',encoding='utf8') as f:
    f.write('商品,價格\n')
    for product in products:
        f.write(product[0]+','+product[1]+'\n')
