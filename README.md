# 🌍 World Passport Quest

A text-based adventure game where you travel between fictional island nations, collecting passports to become a true world citizen.

## 📖 Game Description

In World Passport Quest, you start as a citizen of a randomly selected island nation with a single passport. Your goal is to collect 4 passports by traveling to different countries, working to earn money, and navigating immigration laws.

## 🎮 Features

- **10 Unique Countries**: Each with different visa and passport fees
- **Economic System**: Work at a lemonade stand to earn coins
- **Immigration Mechanics**: Apply for visas, buy residence permits, and obtain citizenship
- **Risk/Reward Gameplay**: Attempt illegal border crossings at your own risk
- **Inventory Management**: Limited backpack space adds strategic depth

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/world-passport-quest.git
cd world-passport-quest
```

2. Run the game:
```bash
python game.py
```

## 🎯 How to Play

### Objective
Collect 4 passports from different countries to win the game.

### Game Commands

| Command | Description |
|---------|-------------|
| `countries` | View all available countries and their fees |
| `status` | Show your current location, money, and items |
| `work` | Work at lemonade stand to earn 10-70 coins |
| `visa [country]` | Apply for a visa (required for legal travel) |
| `travel [country]` | Travel to a country (requires visa/permit/passport) |
| `sneak [country]` | Attempt illegal entry (30% chance of game over) |
| `permit` | Buy residence permit for current country |
| `passport` | Buy citizenship for current country (requires permit) |
| `backpack` | View your inventory |
| `drop [item]` | Remove an item from your backpack |
| `help` | Display available commands |
| `quit` | Exit the game |

### Game Strategy

1. **Start Working**: Use the `work` command to earn coins
2. **Apply for Visas**: Get visas for countries you want to visit
3. **Travel Legally**: Use visas to travel safely between countries
4. **Get Residence Permits**: Required before you can buy passports
5. **Obtain Citizenship**: Buy passports to increase your count
6. **Manage Inventory**: Your backpack can only hold 7 items

### Immigration Path

To obtain a passport from a country:
1. Travel to the country (with visa)
2. Buy a residence permit
3. Purchase the passport

## 🏝️ Countries

The game features 10 fictional island nations, each with unique costs:

- United States of Waffleland (Most expensive)
- Schnitzelreich
- Vikingland
- Meatballonia
- Croissantia
- Chocolatia
- Spaghettiland
- Bulls
- Tzatzikistan
- Kebabistan (Least expensive)

## 🏗️ Project Structure

```
world-passport-quest/
│
├── game.py          # Main game controller and loop
├── player.py        # Player class with inventory and actions
├── country.py       # Country class with fees
├── requirements.txt # Python dependencies (none required)
└── README.md        # This file
```

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements:

- Add new countries
- Implement save/load functionality
- Add random events
- Create difficulty levels
- Add more ways to earn money

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Emre Kulaber

## 🎉 Acknowledgments

- Inspired by classic text-based adventure games
- Built as a Python learning project
