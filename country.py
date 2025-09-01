
class Country:
    """Represents a country in the game with visa and passport fees."""

    def __init__(self, name, visa_fee, passport_fee):
        """
        Initialize a country with its fees.
        
        Args:
            name: Name of the country
            visa_fee: Cost to obtain a visa
            passport_fee: Cost to obtain citizenship
        """
        self.name = name
        self.visa_fee = visa_fee
        self.passport_fee = passport_fee

    def display_info(self):
        """Display country information including visa and passport fees."""
        print(f"\n{self.name}:")
        print(f"  - Visa fee: {self.visa_fee} coins")
        print(f"  - Passport fee: {self.passport_fee} coins")