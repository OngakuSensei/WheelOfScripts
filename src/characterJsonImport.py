import json
import re
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_database_schema import Base, Character, Jinx  # Import your database models

def scriptSortOrder(input_str):
    # Strip leading/trailing spaces from the input string
    input_str = input_str.strip()

    # Mapping of conditions to sort order
    conditions = {
        "You start knowing": 1,
        "Each night*": 3,
        "Each night": 2,
        "Each day": 4,
        "Once per day": 5,
        "Once per game, at night*": 7,
        "Once per game, at night": 6,
        "Once per game, during the day": 8,
        "Once per game": 9,
        "On your 1st night": 10,
        "On your 1st day": 11,
        "You think": 12,
        "You are": 13,
        "You have": 14,
        "You do not know": 15,
        "You might": 16,
        "You": 17,
        "When you die": 18,
        "When you learn that you died": 19,
        "When": 20,
        "If you die": 21,
        "If you died": 22,
        "If you are “mad”": 23,
        "If you": 24,
        "If the Demon dies": 25,
        "If the Demon kills": 26,
        "If the Demon": 27,
        "If both": 28,
        "If there are 5 or more players alive": 29,
        "If": 30,
        "All players": 31,
        "All": 32,
        "The 1st time": 33,
        "The": 34,
        "Minions": 35,
    }

    # Check conditions in descending order of key length to match the most specific condition first
    for key in sorted(conditions.keys(), key=len, reverse=True):
        if input_str.startswith(key):
            return conditions[key]

    # Default return value if no match found
    return 36

def import_characters(session, json_data):
    """
    Import characters from JSON data
    """
    # Valid team types
    valid_teams = {
        'townsfolk': 'Townsfolk',
        'minion': 'Minion',
        'outsider': 'Outsider', 
        'demon': 'Demon',
        'traveler': 'Traveler',
        'fabled': 'Fabled'
    }

    # Characters to be added
    characters_to_add = []

    for entry in json_data:
        # Check if team is valid
        team = entry.get('team', '').lower()
        if team not in valid_teams:
            continue

        # Determine edition and source
        edition = entry.get('edition', '').lower()
        if edition in ['tb', 'bmr', 'snv']:
            character_source = 'Base 3'
        else:
            character_source = 'Kickstarter Experimental'

        # Create character object
        character = Character(
            identifier=entry.get('id', ''),
            name=entry.get('name', ''),
            character_type=valid_teams[team],
            description=entry.get('ability', ''),
            sort_order=script_sort_order(entry.get('ability', '')),
            character_source=character_source
        )
        
        characters_to_add.append(character)

    # Bulk add characters
    session.add_all(characters_to_add)
    session.commit()

    return characters_to_add

def import_jinxes(session, json_data, characters):
    """
    Import jinxes from JSON data
    """
    # Create a dictionary to quickly look up characters by identifier
    character_dict = {char.identifier: char for char in characters}

    # Existing jinxes to avoid duplicates
    existing_jinxes = set()

    # Jinxes to be added
    jinxes_to_add = []

    for entry in json_data:
        # Check if jinxes exist
        jinxes = entry.get('jinxes', [])
        if not jinxes:
            continue

        # Current character's id
        current_id = entry.get('id')

        for jinx in jinxes:
            # Get the jinxed character's id
            jinx_id = jinx.get('id')

            # Create a sorted tuple of ids to check for duplicates
            jinx_pair = tuple(sorted([current_id, jinx_id]))
            
            # Skip if this jinx combination already exists
            if jinx_pair in existing_jinxes:
                continue

            # Find the characters for this jinx
            char1 = character_dict.get(current_id)
            char2 = character_dict.get(jinx_id)

            # Skip if either character not found
            if not char1 or not char2:
                continue

            # Create jinx object
            new_jinx = Jinx(
                character_id_1=char1.id,
                character_id_2=char2.id,
                description=jinx.get('reason', '')
            )

            jinxes_to_add.append(new_jinx)
            existing_jinxes.add(jinx_pair)

    # Bulk add jinxes
    session.add_all(jinxes_to_add)
    session.commit()

def main():
    # Database connection
    engine = create_engine('your_database_connection_string')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Load JSON data
    with open('characters.json', 'r') as f:
        json_data = json.load(f)

    # Import characters first
    characters = import_characters(session, json_data)

    # Then import jinxes
    import_jinxes(session, json_data, characters)

    session.close()

if __name__ == '__main__':
    main()
