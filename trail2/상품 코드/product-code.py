product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.


class Product():
    def __init__(self, name= "codetree",code=50):
        self.n= name
        self.c= code

num1= Product()
print(f"product {num1.c} is {num1.n}")
num2= Product(name=product_name, code= product_code)
print(f"product {num2.c} is {num2.n}")