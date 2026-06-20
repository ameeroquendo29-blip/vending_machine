class VendingItem:
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price


class VendingMachine:
    def __init__(self):
        self.__machine_balance = 0.0
        self.machine_inventory = []

    @property
    def machine_balance(self):
        return self.__machine_balance

    def add_item(self, item_name, item_price):
        self.machine_inventory.append(VendingItem(item_name, item_price))

    def swipe_card(self, selected_index: int, selected_payment: PaymentMethod) -> bool:
        if not (0 <= selected_index < len(self.machine_inventory)):
            return False
        target_item = self.machine_inventory[selected_index]
        if selected_payment.process_payment(target_item.item_price):
            self.__machine_balance += target_item.item_price
            return True
        return False