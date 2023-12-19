import json

def find_words_in_json(export_order_list, json_data):
    found_words = [word for word in export_order_list if find_word_in_json(word, json_data)]
    return found_words

def find_word_in_json(word, json_data):
    if isinstance(json_data, list):
        for item in json_data:
            if find_word_in_json(word, item):
                return True
    elif isinstance(json_data, dict):
        for key, value in json_data.items():
            if find_word_in_json(word, key) or find_word_in_json(word, value):
                return True
    elif isinstance(json_data, (int, float)):
        return word == json_data
    elif isinstance(json_data, str):
        return word == json_data
    return False

# List of words to find
export_order_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250]

with open('CB_PFO_RA_Neurological_Exam.json') as json_file:
    json_data = json.load(json_file)

# Find words in the JSON data
found_words = find_words_in_json(export_order_list, json_data)
found_count = len(found_words)
export_list_count = len(export_order_list)

# Print the result
print(f"Words found in the JSON data: {found_count}/{export_list_count} in \n\n {found_words}\n\n{export_order_list}")
