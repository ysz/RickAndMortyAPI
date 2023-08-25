 # RickAndMorty API Integration

This project is a simple integration connector (client) for the RickAndMorty API (https://rickandmortyapi.com/) - test task solution. It fetches data related to characters, locations, and episodes from the RickAndMorty API and performs specified tasks.

## Objectives:

1. **Fetch Entire API Data**: Retrieve the entire dataset from the API for the entities:
   - Character
   - Location
   - Episode

2. **JSON File Output**: The fetched data is stored in distinct JSON files.

3. **JSON Data Structure**: The structure for each JSON file is:
   - `Id`: A generated unique GUID.
   - `Metadata`: The name extracted from the respective entity.
   - `RawData`: The comprehensive fetched JSON data presented as a dictionary.

Upon the program's successful execution, it will display:
   1. Names of episodes aired between 2017 and 2021 that encompass more than three characters.
   2. Locations that are exclusively mentioned in episodes with odd numbers (e.g., episodes 1, 3, 9 irrespective of their season).


## Requirements

- Python 3.6 or higher
- Requests library

## Installation

1. Clone this repository.
2. Create a virtual environment: `python3 -m venv myenv`.
3. Activate the virtual environment: `source myenv/bin/activate` (Linux/Mac) or `myenv\Scripts\activate` (Windows).
4. Install the required packages: `pip3 install -r requirements.txt`.

## Usage

Simply run the main script:

```bash
python3 main.py
