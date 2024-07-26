## Raising Exceptions - Solve Real-Life Problem with Exception Handling
# What about situations where you want your code to raise exceptions? Let’s explore how to intentionally raise exceptions, using a currency example for context.
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
 
    def __repr__(self):
        return repr((self.currency, self.amount))
 
    def __add__(self, other):
        if self.currency != other.currency:
            raise Exception ("Currencies Do Not Match")
        total_amount = self.amount + other.amount
        return Currency(self.currency, total_amount)
 
value1 = Currency("USD", 20)
value2 = Currency("USD", 30)
print(value1 + value2)  # Output should be ('USD', 50)
 
## Creating a custom exception class
# We can create custom exception classes for that.

class CurrenciesDoNotMatchError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency  # Currency type like "USD", "INR" etc.
        self.amount = amount  # Numerical amount
 
    def __repr__(self):
        return repr((self.currency, self.amount))
 
    def __add__(self, other):
        if self.currency != other.currency:
            raise CurrenciesDoNotMatchError(self.currency + " " + other.currency)
        total_amount = self.amount + other.amount
        return Currency(self.currency, total_amount)
 
 
value1 = Currency("USD", 20)
value2 = Currency("INR", 30)

# print(value1 + value2) ## Should raise CurrenciesDoNotMatchError: USD INR


