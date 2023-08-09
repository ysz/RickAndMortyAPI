import os
import requests
import json
import uuid
from datetime import datetime

# Base URL for the RickAndMorty API
API_BASE_URL = "https://rickandmortyapi.com/api/"


def fetch_data(endpoint):
    """
    Fetches data from the given API endpoint, handles pagination, and returns all results.

    :param endpoint: Endpoint to fetch data from (e.g., 'character', 'location', 'episode')
    :return: List of all fetched data
    """
    results = []
    url = f"{API_BASE_URL}{endpoint}"

    while url:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise exception for HTTP errors
            data = response.json()
            results.extend(data['results'])
            url = data['info']['next']
        except requests.RequestException as e:
            print(f"An error occurred while fetching data: {e}")
            url = None

    return results


def process_data(data, data_type):
    """
    Processes the given data, formats it into the desired structure, and saves to a JSON file.

    :param data: List of data items to process
    :param data_type: Type of data ('characters', 'locations', 'episodes')
    :return: List of processed data
    """
    processed_data = []
    for item in data:
        processed_item = {
            "Id": str(uuid.uuid4()),
            "Metadata": item["name"],
            "RawData": item
        }
        processed_data.append(processed_item)

    # Create the 'data' directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    with open(f'data/{data_type}.json', 'w') as file:
        json.dump(processed_data, file)

    return processed_data


def log_episodes(processed_episodes, start_year=2017, end_year=2021, min_characters=3):
    """
    Logs the names of episodes aired between the specified years and containing more than the specified number of characters.

    :param processed_episodes: List of processed episode data
    :param start_year: Starting year for filtering episodes (default 2017)
    :param end_year: Ending year for filtering episodes (default 2021)
    :param min_characters: Minimum number of characters to include in the log (default 3)
    """
    print(f"Episodes aired between {start_year} and {end_year} with more than {min_characters} characters:")
    for episode in processed_episodes:
        air_date = datetime.strptime(episode['RawData']['air_date'], '%B %d, %Y')
        if start_year <= air_date.year <= end_year and len(episode['RawData']['characters']) > min_characters:
            print(episode['RawData']['name'])


def log_odd_episode_locations(processed_episodes, characters, odd_only=True):
    """
    Logs locations that appear on odd or even episode numbers based on the given flag.

    :param processed_episodes: List of processed episode data
    :param characters: Dictionary of all characters
    :param odd_only: Whether to log only odd episode locations (default True)
    """
    filtered_locations = set()

    for episode in processed_episodes:
        episode_number = int(episode['RawData']['episode'].split('E')[-1])
        if (episode_number % 2 != 0 and odd_only) or (episode_number % 2 == 0 and not odd_only):
            for character_url in episode['RawData']['characters']:
                character_id = int(character_url.split('/')[-1])
                character = characters.get(character_id)
                if character:
                    location_name = character['location']['name']
                    filtered_locations.add(location_name)

    print(f"\nLocations which appear only on {'odd' if odd_only else 'even'} episode numbers:")
    for location in filtered_locations:
        print(location)


def main():
    # Fetching and processing characters, locations, and episodes
    characters_data = fetch_data('character')
    locations = fetch_data('location')
    episodes = fetch_data('episode')

    process_data(characters_data, 'characters')
    process_data(locations, 'locations')
    processed_episodes = process_data(episodes, 'episodes')

    # Creating a dictionary of characters by ID for quick lookup
    characters = {character['id']: character for character in characters_data}

    # Logging required information with custom parameters
    log_episodes(processed_episodes, start_year=2017, end_year=2021, min_characters=3)
    log_odd_episode_locations(processed_episodes, characters, odd_only=True)


if __name__ == '__main__':
    main()
