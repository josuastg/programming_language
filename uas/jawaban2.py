class Product:
    
    #Constructor Product
    def __init__(self, productId, productName, price, amount):
        # instantiate Atributes/Fields
        self.productId = productId
        self.productName = productName
        self.price = price
        self.amount = amount

    # instance method and getter for display product data
    def getProductData(self):
        return """ ID PRODUK \t: {}\n NAMA PRODUK \t: {}\n HARGA \t\t: {}\n JUMLAH \t: {}\n
        """.format(self.productId, self.productName, self.price, self.amount)
    
    # Setter for change product name
    def setProductName(self, productName):
        self.productName = productName
    
    # Setter for change product id
    def setProductId(self, productId):
        self.productId = productId
    
    # Setter for change price
    def setPrice(self, price):
        self.price = price
    
    # Setter for change amount
    def setAmount(self, amount):
        self.amount = amount

        
# instantiate product class
macbook = Product("MAC-PRO-M1-2021", "MACBOOK PRO M1 2021 13 Inch", "Rp 21.000.000", "1 Pcs");
# using getter function
print(macbook.getProductData());

# change the product data using setter function
macbook.setProductId("MAC-AIR-M2-2022")
macbook.setProductName("MACBOOK AIR M2 2022 13 Inch")
macbook.setPrice("Rp 44.000.000")
macbook.setAmount("2 Pcs")
print(macbook.getProductData());