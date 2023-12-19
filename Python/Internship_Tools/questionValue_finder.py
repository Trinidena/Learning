import json

def clean_json(json_data):
    # Convert JSON data to a string, remove extra whitespaces and newlines, then load it back to JSON
    return json.loads(json.dumps(json_data, separators=(',', ':')))

def find_words_in_string(question_value_list, json_data, context_word, max_distance):
    # Clean the JSON data
    cleaned_json_data = clean_json(json_data)
    
    found_words = [word for word in question_value_list if is_near(word, context_word, cleaned_json_data, max_distance)]
    return found_words

def is_near(target_word, context_word, json_data, max_distance=5):
    # Check if target_word is present in the cleaned JSON
    if not any(target_word in str(value) for value in json_data.values()):
        return False

    # Check if context_word is near target_word
    target_index = str(json_data).find(target_word)
    context_index = str(json_data).find(context_word)

    return abs(target_index - context_index) <= max_distance

# List of words to find
question_value_list = ["1", "1", "2", "1", "0", "1", "0", "1", "0", "1", "2", "3", "1", "2", "3", "1", "2", "3", "1", "2", "3", "1", "2", "3", "1", "2", "3", "1", "2", "3", "1", "0", "999", "888", "1", "0", "999", "1", "2", "3", "4", "888", "1", "2", "3", "4", "888", "1", "2", "3", "4", "888", "1", "2", "3", "4", "888", "1", "2", "3", "4", "5", "6", "888", "1", "2", "3", "4", "5", "888", "1", "2", "3", "4", "5", "6", "7", "888", "1", "2", "3", "4", "5", "6", "888", "1", "2", "3", "4", "5", "6", "888", "1", "2", "3", "4", "888"]

with open('CB_PFO_RA_Neurological_Exam.json') as json_file:
    json_data = json.load(json_file)

# Specify the context word and maximum distance
context_word = 'value'
max_distance = 8500  # Adjust this based on how close you want the words to be

# Find words in the JSON data
found_words = find_words_in_string(question_value_list, json_data, context_word, max_distance)
found_count = len(found_words)
question_value_list_count = len(question_value_list)

# Print the result
print(f"Words found in the JSON data: {found_count}/{question_value_list_count} in \n\n {found_words}\n\n{question_value_list}")