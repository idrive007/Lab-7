#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[ ]:




