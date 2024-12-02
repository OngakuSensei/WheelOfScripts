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
