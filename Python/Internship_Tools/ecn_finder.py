import json


def find_words_in_json(export_order_list, json_data):
    found_words = [
        word for word in export_order_list if find_word_in_json(word, json_data)
    ]
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
export_name_list = [
    "Study_ID",
    "NEURO_Compl_Date",
    "Examiner_Name",
    "Assess_Invalid_YN",
    "Assess_Invalid_Reason",
    "Assess_Invalid_Reason_Other",
    "Comments",
    "Age",
    "Awake_Alert_YN",
    "Awake_Alert_No_Specify",
    "Interactive_YN",
    "Interactive_No_Specify",
    "Track_Appropriately_YN",
    "Track_Appropriately_No_Specify",
    "Glasses_Contacts_YN",
    "Glasses_Contacts_Yes_Specify",
    "Extraocular_Mvmt_Intact_YN",
    "Extraocular_Mvmt_Intact_No_Specify",
    "Eye_Mvmt_Conjugate_YN",
    "Eye_Mvmt_Conjugate_No_Specify",
    "Nystagmus_YN",
    "Nystagmus_No_Specify",
    "Facial_Mvmt_Symmetric_YN",
    "Facial_Mvmt_Symmetric_No_Specify",
    "Tongue_Protru_Normal_YN",
    "Tongue_Protru_Normal_No_Specify",
    "Hearing_Normal_Parent_YN",
    "Hearing_Normal_Indiv_YN",
    "Hearing_Normal_No_Specify",
    "Hypotonia_YN",
    "Hypotonia_Yes_Specify",
    "Hypertonia_YN",
    "Hypertonia_Yes_Specify",
    "Hypertonia_Yes_Other",
    "Dystonia_YN",
    "Dystonia_Yes_Specify",
    "Extremity_Mvmt_Symmetric_YN",
    "Extremity_Mvmt_Symmetric_No_Specify",
    "Weakness_YN",
    "Weakness_Yes_Specify",
    "Weakness_Yes_Other",
    "Tremor_YN",
    "Tremor_Yes_Specify",
    "Dysmetria_YN",
    "Dysmetria_Yes_Specify",
    "Walk_Indep_YN",
    "Walk_Indep_No_Specify",
    "Abn_Gait_YN",
    "Abn_Gait_Yes_Specify",
    "Abn_Gait_Yes_Other",
]

with open("CB_PFO_RA_Neurological_Exam.json") as json_file:
    json_data = json.load(json_file)

# Find words in the JSON data
found_words = find_words_in_json(export_name_list, json_data)
found_count = len(found_words)
export_list_count = len(export_name_list)

# Print the result
print(
    f"Words found in the JSON data: {found_count}/{export_list_count} in \n\n {found_words}\n\n{export_name_list}"
)
