import random


class Player:
    """Manages player state, inventory, and actions in the game."""

    def __init__(self, current_location):
        """Initialize player with starting location and inventory."""
        self.current_location = current_location
        self.money = 10
        self.backpack = []
        self.backpack_limit = 7
        self.game_over = False
        self.add_to_backpack("Passport", current_location.name)

    def add_money(self, amount):
        """Add coins to player's money."""
        self.money += amount
        print(f"Earned {amount} coins. Total: {self.money} coins.")

    def spend_money(self, amount):
        """Attempt to spend money. Returns True if successful."""
        if self.money >= amount:
            self.money -= amount
            return True
        return False

    def add_to_backpack(self, doc_type, country_name):
        """Add document to backpack if space available."""
        item = f"{country_name} {doc_type}"
        if len(self.backpack) >= self.backpack_limit:
            print("Your backpack is full! Cannot add more items.")
            return False
        if item not in self.backpack:
            self.backpack.append(item)
            print(f"Added {item} to your backpack")
            return True
        return False

    def has_document(self, doc_type, country_name):
        """Check if player has specific document."""
        return f"{country_name} {doc_type}" in self.backpack

    def show_inventory(self):
        """Display player's money and backpack contents."""
        print(f"Money: {self.money} coins")
        print("\nBackpack contents:")
        if len(self.backpack) == 0:
            print("  Empty")
        else:
            for item in self.backpack:
                print(f"  - {item}")
        print(f"Space remaining: {self.backpack_limit - len(self.backpack)}/{self.backpack_limit} slots")

    def sell_lemonade(self):
        """Sell lemonade to earn coins."""
        profit = random.randint(10, 70)
        self.add_money(profit)
        print(f"You sold lemonade and earned {profit} coins!")

    def apply_for_visa(self, target_country):
        """Apply for visa to target country."""
        if len(self.backpack) >= self.backpack_limit:
            print("Your backpack is full! Drop an item first.")
            return

        if self.current_location == target_country:
            print(f"You are already in {target_country.name}!")
            return

        if self.has_document("Visa", target_country.name):
            print(f"You already have a visa for {target_country.name}!")
            return

        if self.spend_money(target_country.visa_fee):
            self.add_to_backpack("Visa", target_country.name)
            print(f"Visa approved for {target_country.name}!")
        else:
            print(f"You need {target_country.visa_fee} coins for a {target_country.name} visa.")
            print(f"Current balance: {self.money} coins")

    def travel_to(self, target_country):
        """Travel to target country if player has required documents."""
        has_visa = self.has_document("Visa", target_country.name)
        has_passport = self.has_document("Passport", target_country.name)
        has_permit = self.has_document("Permit", target_country.name)

        if self.current_location == target_country:
            print(f"You are already in {target_country.name}!")
            return

        if has_visa or has_passport or has_permit:
            print(f"Traveling to {target_country.name}...")
            print(f"Welcome to {target_country.name}!")
            self.current_location = target_country
            return
        print(f"You need a visa, permit, or passport to enter {target_country.name}!")

    def attempt_illegal_entry(self, target_country):
        """Attempt to sneak into country without documents (risky!)."""
        if self.current_location == target_country:
            print(f"You are already in {target_country.name}!")
            return False

        chance = random.random()
        if chance < 0.3:
            print(f"Border patrol caught you trying to sneak into {target_country.name}!")
            print("You've been deported!")
            print("\nGAME OVER")
            self.game_over = True
            return False
        else:
            print(f"Sneaking into {target_country.name}...")
            self.current_location = target_country
            print("Success! You made it in, but you should get a residence permit to stay legally.")
            return True

    def buy_residence_permit(self, country):
        """Purchase residence permit for current country."""
        if len(self.backpack) >= self.backpack_limit:
            print("Your backpack is full! Drop an item first.")
            return

        if self.has_document("Passport", country.name):
            print(f"You are already a citizen of {country.name}!")
            return

        if self.has_document("Permit", country.name):
            print(f"You already have a residence permit for {country.name}!")
            return

        permit_cost = int(country.visa_fee * 1.5)

        if self.spend_money(permit_cost):
            self.add_to_backpack("Permit", country.name)
            print(f"Residence permit acquired for {country.name}!")
        else:
            print(f"You need {permit_cost} coins for a residence permit.")
            print(f"Current balance: {self.money} coins")

    def buy_passport(self, target_country):
        """Purchase passport (citizenship) for current country."""
        if len(self.backpack) >= self.backpack_limit:
            print("Your backpack is full! Drop an item first.")
            return

        if self.current_location != target_country:
            print(f"You must be in {target_country.name} to buy their passport!")
            return

        if self.has_document("Passport", target_country.name):
            print(f"You are already a citizen of {target_country.name}!")
            return

        if not self.has_document("Permit", target_country.name):
            print(f"You need a residence permit for {target_country.name} first!")
            return

        if self.spend_money(target_country.passport_fee):
            self.add_to_backpack("Passport", target_country.name)
            print(f"Congratulations! You are now a citizen of {target_country.name}!")
        else:
            print(f"You need {target_country.passport_fee} coins for a {target_country.name} passport.")
            print(f"Current balance: {self.money} coins")

    def drop_item(self, item_name):
        """Remove item from backpack."""
        for item in self.backpack:
            if item.lower() == item_name.lower():
                self.backpack.remove(item)
                print(f"Dropped: {item}")
                return True
        print(f"Item '{item_name}' not found in backpack!")
        return False

    def count_passports(self):
        """Count number of passports in backpack."""
        return sum(1 for item in self.backpack if "Passport" in item)