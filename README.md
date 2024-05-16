# Звіт з лабораторної роботи №7. Клас даних.
> Виконала студентка групи ІКМ-М223в **Павленко Дарина**
> 
### Мета: Рефакторінг коду з проблемою «Клас даних».

### Завдання 1: Наданий код
    
   
    
    class Product:
        def __init__(self, product_id, name, category, price):
            self.product_id = product_id  # Це поле має бути приватним
            self.name = name  # Це поле має бути приватним
            self.category = category  # Це поле має бути приватним
            self.price = price  # Це поле має бути приватним

    class InventoryManagement:
          def __init__(self, products):
            self.products = products

        def print_product_details(self, product_id):
            for product in self.products:
                if product.product_id == product_id:
                    print(f"Product ID: {product.product_id}, Name: {product.name}, Category: {product.category}, Price: {product.price}")

### Рішення
Під час рефакторингу коду класу Product, нам потрібно приховати публічні поля product_id, name, category та price, щоб забезпечити кращу ізоляцію даних та зменшити ризик неправильного використання або зміни цих даних ззовні класу. 

    class Product:
        def __init__(self, product_id, name, category, price):
            self._product_id = product_id
            self._name = name
            self._category = category
            self._price = price

    def get_product_id(self):
        return self._product_id

    def get_name(self):
        return self._name

    def get_category(self):
        return self._category

    def get_price(self):
        return self._price


    class InventoryManagement:
        def __init__(self, products):
            self._products = products
  
    def print_product_details(self, product_id):
        for product in self._products:
            if product.get_product_id() == product_id:
                print(f"Product ID: {product.get_product_id()}, Name: {product.get_name()}, Category: {product.get_category()}, Price: {product.get_price()}")

Тепер поля класу Product (_product_id, _name, _category, _price) зроблені приватними, і створено методи доступу (get_product_id(), get_name(), get_category(), get_price()), щоб отримати значення цих полів ззовні класу. Це забезпечує кращу ізоляцію даних та зменшує залежність зовнішнього коду від структури даних класу.
Ще одна можливість для поліпшення - додати метод для зміни ціни товару в класі Product, щоб забезпечити контрольований доступ до цього поля:

    class Product:
        def __init__(self, product_id, name, category, price):
            self._product_id = product_id
            self._name = name
            self._category = category
            self._price = price

        def get_product_id(self):
            return self._product_id

        def get_name(self):
            return self._name

        def get_category(self):
            return self._category

        def get_price(self):
            return self._price

        def set_price(self, new_price):
            self._price = new_price


    class InventoryManagement:
        def __init__(self, products):
            self._products = products

    def print_product_details(self, product_id):
        for product in self._products:
            if product.get_product_id() == product_id:
                print(f"Product ID: {product.get_product_id()}, Name: {product.get_name()}, Category: {product.get_category()}, Price: {product.get_price()}")
