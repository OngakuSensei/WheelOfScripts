from flask import Flask, render_template

app = Flask(__name__)

# Color codes for each character type
COLORS = {
    "townsfolk": "#1d55d6",
    "outsider": "#38a9cb",
    "minion": "#c75405",
    "demon": "#ad0101",
    "jinxes": "#a08a00",
}

# Data Processing Function
def process_data(characters, jinxes):
    grouped_characters = {key: [] for key in COLORS.keys()}

    # Group characters by type and sort by sort_order, then by description length
    for char in characters:
        grouped_characters[char['character_type']].append(char)
    for key in grouped_characters:
        grouped_characters[key].sort(key=lambda c: (c['sort_order'], len(c['description'])))
    
    # Process jinxes and group them
    grouped_jinxes = []
    for jinx in jinxes:
        char1 = next((c for c in characters if c['id'] == jinx['character_id_1']), None)
        char2 = next((c for c in characters if c['id'] == jinx['character_id_2']), None)
        if char1 and char2:
            grouped_jinxes.append({
                'char1': char1,
                'char2': char2,
                'description': jinx['description']
            })

    return grouped_characters, grouped_jinxes

@app.route('/')
def index():
    # Example Data Arrays
    characters = [
        {"id": 1, "identifier": "char1", "name": "Character One", "character_type": "townsfolk", "description": "This is a character.", "sort_order": 1},
        {"id": 2, "identifier": "char2", "name": "Character Two", "character_type": "outsider", "description": "Another description.", "sort_order": 2}
    ]
    jinxes = [
        {"character_id_1": 1, "character_id_2": 2, "description": "These characters are jinxed."}
    ]

    grouped_characters, grouped_jinxes = process_data(characters, jinxes)

    return render_template('index.html', characters=grouped_characters, jinxes=grouped_jinxes, colors=COLORS)

if __name__ == '__main__':
    app.run(debug=True)
// JavaScript Document