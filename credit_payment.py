from payment_mode import PaymentMethod
class CreditCard(PaymentMethod):
    def __init__(self, card_holder, card_number, credit_limit=8000.0):
        self.card_holder = card_holder
        self.card_number = card_number
        self.__current_balance = 0.0
        self.__credit_limit = credit_limit

    @property
    def current_balance(self):
        return self.__current_balance

    @property
    def credit_limit(self):
        return self.__credit_limit

    def charge(self, amount):
        if self.__current_balance + amount > self.__credit_limit:
            return False
        self.__current_balance += amount
        return True

    def process_payment(self, amount: float) -> bool:
        return self.charge(amount)