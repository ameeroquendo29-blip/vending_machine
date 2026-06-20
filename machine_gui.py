import tkinter as tk
from tkinter import messagebox
from vending_machine import VendingMachine
from student_buyers import EngineeringStudent
from credit_payment import CreditCard
class VendingMachineGUI:
    def __init__(self, window, machine, card, student):
        self.window = window
        self.machine = machine
        self.card = card
        self.student = student

        # Window Settings
        self.window.title("PUP Engineering Vending Machine")
        self.window.geometry("450x550")
        self.window.configure(bg="#2c3e50")

        # 1. Header Section (Student & Card Info Display)
        self.profile_frame = tk.LabelFrame(window, text=" User Account Profiles ", bg="#2c3e50", fg="#ecf0f1",
                                           font=("Arial", 10, "bold"), padx=10, pady=10)
        self.profile_frame.pack(fill="x", padx=15, pady=10)

        self.lbl_student = tk.Label(self.profile_frame,
                                    text=f"Student: {student.student_name} ({student.engineering_department} Eng)",
                                    bg="#2c3e50", fg="#bdc3c7")
        self.lbl_student.pack(anchor="w")

        self.lbl_card = tk.Label(self.profile_frame, text="", bg="#2c3e50", fg="#ea6153", font=("Arial", 10, "bold"))
        self.lbl_card.pack(anchor="w", pady=(5, 0))
        self.update_card_display()

        # 2. Vending Inventory Section
        self.inventory_frame = tk.LabelFrame(window, text=" Select an Item to Purchase ", bg="#2c3e50", fg="#ecf0f1",
                                             font=("Arial", 10, "bold"), padx=10, pady=10)
        self.inventory_frame.pack(fill="both", expand=True, padx=15, pady=5)

        self.create_inventory_buttons()

        # 3. Machine Stats Footer
        self.lbl_machine_balance = tk.Label(window, text="", bg="#2c3e50", fg="#2ecc71", font=("Arial", 11, "bold"))
        self.lbl_machine_balance.pack(pady=15)
        self.update_machine_display()

    def update_card_display(self):
        masked_number = "XXXX" + self.card.card_number[4:] if len(self.card.card_number) > 4 else "XXXX"
        self.lbl_card.config(
            text=f"Card: {masked_number}  |  Spent: ₱{self.card.current_balance:.2f} / ₱{self.card.credit_limit:.2f}"
        )

    def update_machine_display(self):
        self.lbl_machine_balance.config(text=f"Total Vending Machine Earnings: ₱{self.machine.machine_balance:.2f}")

    def create_inventory_buttons(self):
        # Dynamically build visual buttons for each item in the OOP structure
        for idx, item in enumerate(self.machine.machine_inventory):
            btn_text = f"{item.item_name}\n₱{item.item_price:.2f}"

            # Using a lambda function with default arguments captures the current loop index correctly
            btn = tk.Button(
                self.inventory_frame,
                text=btn_text,
                bg="#34495e",
                fg="#ffffff",
                font=("Arial", 11, "bold"),
                height=3,
                command=lambda i=idx: self.handle_purchase(i)
            )
            btn.pack(fill="x", pady=5)

    def handle_purchase(self, item_index):
        target_item = self.machine.machine_inventory[item_index]

        # Pass backend execution through the established system
        success = self.machine.swipe_card(item_index, self.card)

        if success:
            messagebox.showinfo("Transaction Success", f"Dispensing {target_item.item_name}!\nEnjoy your snack!")
            self.update_card_display()
            self.update_machine_display()
        else:
            messagebox.showerror("Transaction Denied",
                                 f"Could not charge ₱{target_item.item_price:.2f}.\nYou have exceeded your credit limit!")

if __name__ == "__main__":
    # 1. Initialize OOP Backend Data Structures
    my_machine = VendingMachine()
    my_machine.add_item("Coke Classic", 35.00)
    my_machine.add_item("Fudgee Barr (Chocolate)", 12.00)
    my_machine.add_item("Bottled Mineral Water", 15.00)
    my_machine.add_item("Potato Chips", 25.00)

    # Simulating standard active runtime definitions
    active_student = EngineeringStudent(student_name="Kenny", student_age=23, engineering_department="Computer")
    active_card = CreditCard(card_holder=active_student.student_name, card_number="123456789012", credit_limit=100.00)

    # 2. Boot Up the Tkinter Engine Window Workspace
    root_window = tk.Tk()
    app = VendingMachineGUI(root_window, my_machine, active_card, active_student)
    root_window.mainloop()