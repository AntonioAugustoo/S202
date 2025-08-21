# Python Pokedex App

## Overview
The Python Pokedex App is a simple application designed to manage and query Pokémon data. It utilizes a `Pokedex` class that interacts with a `Database` class to perform various queries and log the results.

## Project Structure
```
python-pokedex-app
├── src
│   ├── pokedex.py        # Defines the Pokedex class with query methods
│   ├── database.py       # Manages data and provides query methods
│   ├── writeAJson.py     # Logs query results in JSON format
│   └── report.md         # Documentation report for the project
└── README.md             # General information about the project
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/python-pokedex-app.git
   ```
2. Navigate to the project directory:
   ```
   cd python-pokedex-app
   ```
3. Ensure you have Python installed (version 3.6 or higher).
4. Install any required dependencies (if applicable).

## Usage
To use the Pokedex application, you can run the `pokedex.py` file, which will allow you to interact with the Pokémon data through the defined methods.

## Features
- Aggregation relationship between `Pokedex` and `Database`.
- Five distinct query methods in the `Pokedex` class.
- Logging of query results using the `writeAJson` function.

## Contribution
Feel free to fork the repository and submit pull requests for any improvements or features you would like to add.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.