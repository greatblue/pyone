import urllib.request
import json


class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance

    def stampajbre(self):
        """stampaj ime i balans na ekranu"""
        self.balance = float('1200.0')
        print(self.name + '    ' + str(self.balance))


class FunWithOs(object):
    """zezanje sa operativnim sistemom"""

    def __init__(self, text):
        self.text = text

    def writefile(self):
        print('creating new file ')
        file = open('test.txt', 'a')
        file.write(str(self.text))
        file.close()


urlData = ""
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
print(data)
encoding = webURL.info().get_content_charset('utf-8')
JSON_object = json.loads(data.decode(encoding))

writeToFile = FunWithOs(JSON_object)
writeToFile.writefile()
