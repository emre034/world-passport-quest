import random
from typing import Optional

from country import Country
from player import Player


class Game:
    """Main game controller managing game state, player, and countries."""

    def __init__(self):
        """Initialize game with empty state."""
        self.player: Optional[Player] = None
        self.countries: list[Country] = []
        self.game_running = False
        self.winning_passport_count = 4

    def setup_game(self):
        """Initialize new game with welcome message and player setup."""
        self._display_welcome_message()
        self._create_countries()
        self._setup_player()
        self._display_initial_help()

    def _display_welcome_message(self):
        """Display game introduction and objectives."""
        print("\n" + "="*50)
        print("WORLD PASSPORT QUEST")
        print("="*50)
        print("\nExplore island nations and collect passports!")
        print(f"Goal: Collect {self.winning_passport_count} passports to win")
        print("(Your birth country passport counts)")

    def _create_countries(self):
        """Initialize all available countries with their fees."""
        self.countries = [
            Country("United States of Waffleland", 1000, 2000),
            Country("Schnitzelreich", 900, 1800),
            Country("Vikingland", 850, 1700),
            Country("Meatballonia", 800, 1600),
            Country("Croissantia", 700, 1400),
            Country("Chocolatia", 550, 1100),
            Country("Spaghettiland", 500, 1000),
            Country("Bulls", 400, 800),
            Country("Tzatzikistan", 300, 600),
            Country("Kebabistan", 200, 400)
        ]

    def _setup_player(self):
        """Create player with random starting country."""
        starting_country = random.choice(self.countries)
        print(f"\nYou were born in {starting_country.name}!")
        print("You receive your home country's passport.")
        
        self.player = Player(starting_country)
        self.player.add_money(10)

    def _display_initial_help(self):
        """Show initial commands and player status."""
        print("\nType 'help' to see available commands.")
        self.show_player_status()

    def start_game(self):
        """Start the game loop."""
        self.game_running = True
        self.setup_game()

    def show_player_status(self):
        """Display current player status and progress."""
        print(f"\nCurrent Location: {self.player.current_location.name}")
        self.player.show_inventory()
        
        passport_count = self.player.count_passports()
        print(f"Progress: {passport_count}/{self.winning_passport_count} passports")

    def show_available_commands(self):
        """Display all available game commands."""
        commands = [
            ("countries", "View all countries and their fees"),
            ("status", "Show your current status"),
            ("work", "Work at lemonade stand to earn coins"),
            ("visa [country]", "Apply for a visa"),
            ("travel [country]", "Travel to a country"),
            ("sneak [country]", "Attempt illegal entry (risky!)"),
            ("permit", "Buy residence permit for current country"),
            ("passport", "Buy passport for current country"),
            ("backpack", "View backpack contents"),
            ("drop [item]", "Drop an item from backpack"),
            ("help", "Show this help message"),
            ("quit", "Exit game")
        ]
        
        print("\nAvailable Commands:")
        for cmd, desc in commands:
            print(f"  {cmd:<20} - {desc}")

    def handle_player_input(self, command: str):
        """Process and execute player commands."""
        command = command.lower().strip()
        parts = command.split(maxsplit=1)
        action = parts[0] if parts else ""
        argument = parts[1] if len(parts) > 1 else ""

        if self.player.game_over:
            self.game_running = False
            return

        command_map = {
            "quit": self._quit_game,
            "countries": self.show_all_countries,
            "status": self.show_player_status,
            "backpack": self.player.show_inventory,
            "help": self.show_available_commands,
            "work": self.player.sell_lemonade,
            "limon": self.player.sell_lemonade,  # Legacy support
            "permit": lambda: self.player.buy_residence_permit(self.player.current_location),
            "passport": self._handle_passport_purchase
        }

        if action in command_map:
            command_map[action]()
        elif action == "drop" and argument:
            self.player.drop_item(argument)
        elif action == "visa" and argument:
            self._handle_visa_application(argument)
        elif action == "travel" and argument:
            self._handle_travel(argument)
        elif action == "move" and argument:  # Legacy support
            self._handle_travel(argument)
        elif action == "sneak" and argument:
            self._handle_sneak(argument)
        else:
            print("Unknown command. Type 'help' for available commands.")

    def _quit_game(self):
        """Exit the game."""
        self.game_running = False
        print("\nThanks for playing World Passport Quest!")

    def _handle_visa_application(self, country_name: str):
        """Handle visa application for specified country."""
        target = self._find_country(country_name)
        if target:
            self.player.apply_for_visa(target)

    def _handle_travel(self, country_name: str):
        """Handle travel to specified country."""
        target = self._find_country(country_name)
        if target:
            self.player.travel_to(target)

    def _handle_sneak(self, country_name: str):
        """Handle sneaking into specified country."""
        target = self._find_country(country_name)
        if target:
            self.player.attempt_illegal_entry(target)

    def _handle_passport_purchase(self):
        """Handle passport purchase and check win condition."""
        self.player.buy_passport(self.player.current_location)
        
        if self.player.count_passports() >= self.winning_passport_count:
            self._handle_victory()

    def _handle_victory(self):
        """Handle game victory."""
        print("\n" + "="*50)
        print("CONGRATULATIONS! YOU WON!")
        print("="*50)
        print(f"\nYou've collected {self.winning_passport_count} passports!")
        print("You are now a true world citizen!")
        self.game_running = False

    def _find_country(self, name: str) -> Optional[Country]:
        """Find country by name (case-insensitive)."""
        name = name.lower()
        for country in self.countries:
            if country.name.lower() == name:
                return country
        print(f"Country '{name}' not found. Type 'countries' to see all available countries.")
        return None

    def show_all_countries(self):
        """Display information about all available countries."""
        print("\n" + "="*30)
        print("AVAILABLE COUNTRIES")
        print("="*30)
        for country in self.countries:
            country.display_info()


def main():
    """Main game entry point."""
    game = Game()
    game.start_game()

    while game.game_running:
        try:
            command = input("\n> ")
            game.handle_player_input(command)
        except (KeyboardInterrupt, EOFError):
            print("\n\nGame interrupted. Thanks for playing!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()