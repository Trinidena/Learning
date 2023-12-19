def find_words_in_string(input_string, word_list):
    found_words = [word for word in word_list if word in input_string]
    return found_words

# Example usage
input_string = '''
{
    "title": "RA - Rapid Dysmorphology Screen [RDS]",
    "pages": [
     {
      "name": "page1",
      "elements": [
       {
        "type": "text",
        "name": "RDS_1",
        "title": "Study ID",
        "description": "<br>(site ID 1xx, family ID xxx, sub ID 101, 130, 140)<br><br>",
        "isRequired": true,
        "Export Column Name": "Study_ID",
        "Export Column Order": 5,
        "Pii flag": true,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Admin"
       },
       {
        "type": "text",
        "name": "RDS_2",
        "title": "Date of completing the RDS",
        "isRequired": true,
        "Export Column Name": "RDS_Compl_Date",
        "Export Column Order": 10,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Admin",
        "inputType": "date"
       },
       {
        "type": "text",
        "name": "RDS_3",
        "title": "Name of the Examiner",
        "isRequired": true,
        "Export Column Name": "Examiner_Name",
        "Export Column Order": 15,
        "Pii flag": true,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Admin"
       },
       {
        "type": "checkbox",
        "name": "RDS_4",
        "title": "Please indicate here if assessment is considered invalid.",
        "titleLocation": "hidden",
        "Export Column Name": "Invalid_YN",
        "Export Column Order": 20,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Admin",
        "choices": [
         {
          "value": "1",
          "text": "Please indicate here if assessment is considered invalid."
         }
        ]
       },
       {
        "type": "checkbox",
        "name": "RDS_4_REASON",
        "visibleIf": "{RDS_4} = [1]",
        "title": "If assessment is invalid, please indicate the reason(s):",
        "isRequired": true,
        "Export Column Name": "Invalid_Reason",
        "Export Column Order": 25,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Admin",
        "choices": [
         {
          "value": "1",
          "text": "Child behavioral issues (e.g., difficulty with cooperation, etc.) impacted assessment"
         },
         {
          "value": "2",
          "text": "Other"
         }
        ]
       },
       {
        "type": "text",
        "name": "RDS_4_REASON_OTHER",
        "visibleIf": "{RDS_4_REASON} contains 2",
        "title": "Specify other reason",
        "isRequired": true,
        "Export Column Name": "Invalid_Reason_Other",
        "Export Column Order": 30,
        "Pii flag": true,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Admin"
       }
      ]
     },
     {
      "name": "page2",
      "elements": [
       {
        "type": "html",
        "name": "Page2Instructions",
        "Export Column Order": 35,
        "IsNotPull-ForwardEligible": true,
        "html": "<div style=\"font-size: large;\"><b>Introduction: This assessment includes a brief physical exam along with some photos [if photos are to be taken during telehealth]. I'll also ask some questions about your child's [or your (if self-reporting)] physical development along with some family history questions.</b></div>"
       },
       {
        "type": "panel",
        "name": "Family_History_Panel",
        "elements": [
         {
          "type": "radiogroup",
          "name": "RDS_5",
          "title": "Is there any family history of developmental disabilities like intellectual disability or autism for example?",
          "isRequired": true,
          "Export Column Name": "Fam_Hx_Dev_Disab_YN",
          "Export Column Order": 40,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Family",
          "choices": [
           {
            "value": "1",
            "text": "Yes"
           },
           {
            "value": "0",
            "text": "No"
           }
          ]
         },
         {
          "type": "comment",
          "name": "RDS_5_DETAIL",
          "visibleIf": "{RDS_5} = 1",
          "title": "Family History Detail ",
          "isRequired": true,
          "Export Column Name": "Fam_Hx_Dev_Disab_Detail",
          "Export Column Order": 45,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Family"
         },
         {
          "type": "radiogroup",
          "name": "RDS_6",
          "title": "Is there any family history of differences in the  structure of the body (malformations, birth defects) like cleft palate, heart defects, or spina bifida for example? ",
          "isRequired": true,
          "Export Column Name": "Fam_Hx_Structure_Abn_YN",
          "Export Column Order": 50,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Family",
          "choices": [
           {
            "value": "1",
            "text": "Yes"
           },
           {
            "value": "0",
            "text": "No"
           }
          ]
         },
         {
          "type": "comment",
          "name": "RDS_6_DETAIL",
          "visibleIf": "{RDS_6} = 1",
          "title": "Body Structure Detail ",
          "isRequired": true,
          "Export Column Name": "Fam_Hx_Structure_Abn_Detail",
          "Export Column Order": 55,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Family"
         },
         {
          "type": "radiogroup",
          "name": "RDS_7",
          "title": "Are you and the child's other biological parent related in anyway?\n<br><br>\nOR\n<br><br>\n[If non biological caregiver is informant ask:] Are\nthe biological parents related in anyway?",
          "isRequired": true,
          "Export Column Name": "Bio_Parents_Related_YN",
          "Export Column Order": 60,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Family",
          "choices": [
           {
            "value": "1",
            "text": "Yes"
           },
           {
            "value": "0",
            "text": "No"
           }
          ]
         },
         {
          "type": "comment",
          "name": "RDS_7_DETAIL",
          "visibleIf": "{RDS_7} = 1",
          "title": "Consanguinity Detail ",
          "isRequired": true,
          "Export Column Name": "Bio_Parents_Related_Detail",
          "Export Column Order": 65,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Family"
         }
        ],
        "title": "Family History"
       },
       {
        "type": "panel",
        "name": "Measurements_at_Birth_Panel",
        "elements": [
         {
          "type": "text",
          "name": "RDS_8",
          "title": "Gestation at Birth ",
          "isRequired": true,
          "requiredErrorText": "Validation:  Must be > 18",
          "Export Column Name": "Gestation_at_Birth_wks",
          "Export Column Order": 70,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Birth Stats",
          "inputType": "number",
          "min": "18"
         },
         {
          "type": "html",
          "name": "RDS_8_text",
          "startWithNewLine": false,
          "html": "<br><br><div>weeks</div>"
         },
         {
          "type": "text",
          "name": "RDS_9",
          "title": "Gestation, Date Measurement Obtained ",
          "isRequired": true,
          "Export Column Name": "Gestation_Msmt_Date",
          "Export Column Order": 75,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Birth Stats",
          "inputType": "date"
         },
         {
          "type": "radiogroup",
          "name": "RDS_10",
          "title": "Gestation Source",
          "isRequired": true,
          "Export Column Name": "Gestation_Source",
          "Export Column Order": 80,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Birth Stats",
          "choices": [
           {
            "value": "1",
            "text": "Clinic"
           },
           {
            "value": "2",
            "text": "Self-Report"
           },
           {
            "value": "3",
            "text": "Other"
           }
          ]
         },
         {
          "type": "text",
          "name": "RDS_10_OTHER",
          "visibleIf": "{RDS_10} = 3",
          "title": "Other Gestation Source",
          "isRequired": true,
          "Export Column Name": "Gestation_Source_Other",
          "Export Column Order": 85,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Birth Stats"
         },
         {
          "type": "text",
          "name": "RDS_11",
          "title": "Birth Weight",
          "isRequired": true,
          "Export Column Name": "Birth_Wt_kg",
          "Export Column Order": 90,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Birth Stats",
          "inputType": "number",
          "min": "0"
         },
         {
          "type": "html",
          "name": "RDS_11_text",
          "startWithNewLine": false,
          "html": "<br><br><div>kilograms</div>"
         },
         {
          "type": "text",
          "name": "RDS_12",
          "title": "Birth Weight, Date Measurement Obtained ",
          "isRequired": true,
          "Export Column Name": "Birth_Wt_Date",
          "Export Column Order": 95,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Birth Stats",
          "inputType": "date"
         },
         {
          "type": "radiogroup",
          "name": "RDS_13",
          "title": "Birth Weight Source",
          "isRequired": true,
          "Export Column Name": "Birth_Wt_Source",
          "Export Column Order": 100,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Birth Stats",
          "choices": [
           {
            "value": "1",
            "text": "Clinic"
           },
           {
            "value": "2",
            "text": "Self-Report"
           },
           {
            "value": "3",
            "text": "Other"
           }
          ]
         },
         {
          "type": "text",
          "name": "RDS_13-OTHER",
          "visibleIf": "{RDS_13} = 3",
          "title": "Other Birth Weight Source",
          "isRequired": true,
          "Export Column Name": "Birth_Wt_Source_Other",
          "Export Column Order": 105,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Birth Stats"
         },
         {
          "type": "text",
          "name": "RDS_14",
          "title": "Birth Length ",
          "isRequired": true,
          "Export Column Name": "Birth_Lgth_cm",
          "Export Column Order": 110,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Birth Stats",
          "inputType": "number",
          "min": "0"
         },
         {
          "type": "html",
          "name": "RDS_14_text",
          "startWithNewLine": false,
          "html": "<br><br><div>centimeters</div>"
         },
         {
          "type": "text",
          "name": "RDS_15",
          "title": "Birth Length, Date Measurement Obtained ",
          "isRequired": true,
          "Export Column Name": "Birth_Lgth_Date",
          "Export Column Order": 115,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Birth Stats",
          "inputType": "date"
         },
         {
          "type": "radiogroup",
          "name": "RDS_16",
          "title": "Birth Length Source",
          "isRequired": true,
          "Export Column Name": "Birth_Lgth_Source",
          "Export Column Order": 120,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Birth Stats",
          "choices": [
           {
            "value": "1",
            "text": "Clinic"
           },
           {
            "value": "2",
            "text": "Self-Report"
           },
           {
            "value": "3",
            "text": "Other"
           }
          ]
         },
         {
          "type": "text",
          "name": "RDS_16_OTHER",
          "visibleIf": "{RDS_16} = 3",
          "title": "Other Birth Length Source",
          "isRequired": true,
          "Export Column Name": "Birth_Lgth_Source_Other",
          "Export Column Order": 125,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Birth Stats"
         },
         {
          "type": "text",
          "name": "RDS_17",
          "title": "Birth Head Circumference",
          "isRequired": true,
          "Export Column Name": "Birth_Head_Circum_cm",
          "Export Column Order": 130,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Birth Stats",
          "inputType": "number",
          "min": "0"
         },
         {
          "type": "html",
          "name": "RDS_17_text",
          "startWithNewLine": false,
          "html": "<br><br><div>centimeters</div>"
         },
         {
          "type": "text",
          "name": "RDS_18",
          "title": "Birth Head Circumference, Date Measurement Obtained ",
          "isRequired": true,
          "Export Column Name": "Birth_Head_Circum_Date",
          "Export Column Order": 135,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Birth Stats",
          "inputType": "date"
         },
         {
          "type": "radiogroup",
          "name": "RDS_19",
          "title": "Birth Head Circumference Source",
          "isRequired": true,
          "Export Column Name": "Birth_Head_Circum_Source",
          "Export Column Order": 140,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Birth Stats",
          "choices": [
           {
            "value": "1",
            "text": "Clinic"
           },
           {
            "value": "2",
            "text": "Self-Report"
           },
           {
            "value": "3",
            "text": "Other"
           }
          ]
         },
         {
          "type": "text",
          "name": "RDS_19_OTHER",
          "visibleIf": "{RDS_19} = 3",
          "title": "Other Birth Head Circumference Source",
          "isRequired": true,
          "Export Column Name": "Birth_Head_Circum_Source_Other",
          "Export Column Order": 145,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Birth Stats"
         }
        ],
        "title": "Measurements at Birth"
       }
      ]
     },
     {
      "name": "page3",
      "elements": [
       {
        "type": "panel",
        "name": "Most_Recent_Growth_Parameters_Panel",
        "elements": [
         {
          "type": "text",
          "name": "RDS_20",
          "title": "Most Recent Weight",
          "isRequired": true,
          "Export Column Name": "Most_Recent_Wt_kg",
          "Export Column Order": 150,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Most Recent Stats",
          "inputType": "number",
          "min": "0"
         },
         {
          "type": "html",
          "name": "RDS_20_text",
          "startWithNewLine": false,
          "html": "<br><br><div>kilograms</div>"
         },
         {
          "type": "text",
          "name": "RDS_21",
          "title": "Most Recent Weight Standard Deviation",
          "isRequired": true,
          "Export Column Name": "Most_Recent_Wt_Std_Dev",
          "Export Column Order": 155,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Most Recent Stats"
         },
         {
          "type": "text",
          "name": "RDS_22",
          "title": "Most Recent Weight, Date Measurement Obtained",
          "isRequired": true,
          "Export Column Name": "Most_Recent_Wt_Date",
          "Export Column Order": 160,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Most Recent Stats",
          "inputType": "date"
         },
         {
          "type": "radiogroup",
          "name": "RDS_23",
          "title": "Most Recent Weight Source",
          "isRequired": true,
          "Export Column Name": "Most_Recent_Wt_Source",
          "Export Column Order": 165,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Most Recent Stats",
          "choices": [
           {
            "value": "1",
            "text": "Clinic"
           },
           {
            "value": "2",
            "text": "Self-Report"
           },
           {
            "value": "3",
            "text": "Other"
           }
          ]
         },
         {
          "type": "text",
          "name": "RDS_23_OTHER",
          "visibleIf": "{RDS_23} = 3",
          "title": "Other Weight Source",
          "isRequired": true,
          "Export Column Name": "Most_Recent_Wt_Source_Other",
          "Export Column Order": 170,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Most Recent Stats"
         },
         {
          "type": "text",
          "name": "RDS_24",
          "title": "Most Recent Height",
          "isRequired": true,
          "Export Column Name": "Most_Recent_Ht_cm",
          "Export Column Order": 175,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Most Recent Stats",
          "inputType": "number",
          "min": "0"
         },
         {
          "type": "html",
          "name": "RDS_24_text",
          "startWithNewLine": false,
          "html": "<br><br><div>centimeters</div>"
         },
         {
          "type": "text",
          "name": "RDS_25",
          "title": "Most Recent Height Standard Deviation",
          "isRequired": true,
          "Export Column Name": "Most_Recent_Ht_Std_Dev",
          "Export Column Order": 180,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Most Recent Stats"
         },
         {
          "type": "text",
          "name": "RDS_26",
          "title": "Most Recent Height, Date Measurement Obtained",
          "isRequired": true,
          "Export Column Name": "Most_Recent_Ht_Date",
          "Export Column Order": 185,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Most Recent Stats",
          "inputType": "date"
         },
         {
          "type": "radiogroup",
          "name": "RDS_27",
          "title": "Most Recent Height Source",
          "isRequired": true,
          "Export Column Name": "Most_Recent_Ht_Source",
          "Export Column Order": 190,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Most Recent Stats",
          "choices": [
           {
            "value": "1",
            "text": "Clinic"
           },
           {
            "value": "2",
            "text": "Self-Report"
           },
           {
            "value": "3",
            "text": "Other"
           }
          ]
         },
         {
          "type": "text",
          "name": "RDS_27_OTHER",
          "visibleIf": "{RDS_27} = 3",
          "title": "Other Height Source",
          "isRequired": true,
          "Export Column Name": "Most_Recent_Ht_Source_Other",
          "Export Column Order": 195,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Most Recent Stats"
         },
         {
          "type": "text",
          "name": "RDS_28",
          "title": "Most Recent Head Circumference",
          "isRequired": true,
          "Export Column Name": "Most_Recent_Head_Circum_cm",
          "Export Column Order": 200,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Most Recent Stats",
          "inputType": "number",
          "min": "0"
         },
         {
          "type": "html",
          "name": "RDS_28_text",
          "startWithNewLine": false,
          "html": "<br><br><div>centimeters</div>"
         },
         {
          "type": "text",
          "name": "RDS_29",
          "title": "Most Recent Head Circumference Standard Deviation",
          "isRequired": true,
          "Export Column Name": "Most_Recent_Head_Circum_Std_Dev",
          "Export Column Order": 205,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Most Recent Stats"
         },
         {
          "type": "text",
          "name": "RDS_30",
          "title": "Most Recent Head Circumference, Date Measurement Obtained",
          "isRequired": true,
          "Export Column Name": "Most_Recent_Head_Circum_Date",
          "Export Column Order": 210,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Most Recent Stats",
          "inputType": "date"
         },
         {
          "type": "radiogroup",
          "name": "RDS_31",
          "title": "Most Recent Head Circumference Source",
          "isRequired": true,
          "Export Column Name": "Most_Recent_Head_Circum_Source",
          "Export Column Order": 215,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Most Recent Stats",
          "choices": [
           {
            "value": "1",
            "text": "Clinic"
           },
           {
            "value": "2",
            "text": "Self-Report"
           },
           {
            "value": "3",
            "text": "Other"
           }
          ]
         },
         {
          "type": "text",
          "name": "RDS_31_OTHER",
          "visibleIf": "{RDS_31} = 3",
          "title": "Other Most Recent Head Circumference Source",
          "isRequired": true,
          "Export Column Name": "Most_Recent_Head_Circum_Source_Other",
          "Export Column Order": 220,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Most Recent Stats"
         }
        ],
        "title": "Most Recent Growth Parameters"
       },
       {
        "type": "panel",
        "name": "Facial_Gestalt_/_Comparison_to_Parents_Panel",
        "elements": [
         {
          "type": "checkbox",
          "name": "RDS_32",
          "title": "Which biological parents were present at appointment? ",
          "isRequired": true,
          "Export Column Name": "Bio_Parent_At_Appt",
          "Export Column Order": 225,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation",
          "choices": [
           {
            "value": "1",
            "text": "Mother",
            "enableIf": "{RDS_32} notcontains 3"
           },
           {
            "value": "2",
            "text": "Father",
            "enableIf": "{RDS_32} notcontains 3"
           },
           {
            "value": "3",
            "text": "None"
           }
          ]
         },
         {
          "type": "radiogroup",
          "name": "RDS_33",
          "title": "Does the patient appear dysmorphic or unusual compared to the biological parents?",
          "isRequired": true,
          "Export Column Name": "Dysmorphic_YN",
          "Export Column Order": 230,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation",
          "choices": [
           {
            "value": "1",
            "text": "Yes"
           },
           {
            "value": "0",
            "text": "No"
           },
           {
            "value": "999",
            "text": "Not Sure"
           },
           {
            "value": "888",
            "text": "Unable to assess"
           }
          ]
         },
         {
          "type": "radiogroup",
          "name": "RDS_34",
          "title": "Ask parent / caregiver - \"Do you think he /she has unusual facial features that are not in keeping with the family?\"",
          "isRequired": true,
          "Export Column Name": "Ununual_Facial_Features_Parent_YN",
          "Export Column Order": 235,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation",
          "choices": [
           {
            "value": "1",
            "text": "Yes"
           },
           {
            "value": "0",
            "text": "No"
           },
           {
            "value": "999",
            "text": "Not Sure"
           }
          ]
         },
         {
          "type": "comment",
          "name": "RDS_34_SPECIFY",
          "visibleIf": "{RDS_34} = 1",
          "title": "Unusual Facial Features Detail",
          "isRequired": true,
          "Export Column Name": "Unusual_Facial_Features_Detail",
          "Export Column Order": 240,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation"
         }
        ],
        "title": "Facial Gestalt / Comparison to Parents"
       }
      ]
     },
     {
      "name": "page4",
      "elements": [
       {
        "type": "panel",
        "name": "Assessments_Panel",
        "elements": [
         {
          "type": "radiogroup",
          "name": "RDS_35",
          "title": "Habitus (body build, select one)",
          "isRequired": true,
          "Export Column Name": "Habitus_YN",
          "Export Column Order": 245,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation",
          "choices": [
           {
            "value": "1",
            "text": "Normal"
           },
           {
            "value": "2",
            "text": "Obese"
           },
           {
            "value": "3",
            "text": "Slender"
           },
           {
            "value": "4",
            "text": "Other"
           },
           {
            "value": "888",
            "text": "Not Assessed"
           }
          ]
         },
         {
          "type": "comment",
          "name": "RDS_35_OTHER",
          "visibleIf": "{RDS_35} = 4",
          "title": "Other Habitus (body build) Description",
          "isRequired": true,
          "Export Column Name": "Habitus_Detail",
          "Export Column Order": 250,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation"
         },
         {
          "type": "checkbox",
          "name": "RDS_36",
          "title": "Skin (select all that apply)\n<br><br>\nAsk patient/parent - Are there any birth marks, café au lait spots, ash leaf spots, or skin lesions?  If yes, photograph if needed.",
          "description": "<br>Example: Hyperpigmented spot (café au lait spot)<br><br>\n",
          "isRequired": true,
          "Export Column Name": "Skin",
          "Export Column Order": 255,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation",
          "choices": [
           {
            "value": "1",
            "text": "Normal (absent of any lesions, marks, spots, etc.)",
            "enableIf": "{RDS_36} notcontains 888"
           },
           {
            "value": "2",
            "text": "HYPERpigmented Spot",
            "enableIf": "{RDS_36} notcontains 1 and {RDS_36} notcontains 888"
           },
           {
            "value": "3",
            "text": "HYPOpigmented Patch",
            "enableIf": "{RDS_36} notcontains 1 and {RDS_36} notcontains 888"
           },
           {
            "value": "4",
            "text": "Other",
            "enableIf": "{RDS_36} notcontains 1 and {RDS_36} notcontains 888"
           },
           {
            "value": "888",
            "text": "Not Assessed",
            "enableIf": "{RDS_36} notcontains 1"
           }
          ]
         },
         {
          "type": "comment",
          "name": "RDS_36_OTHER",
          "visibleIf": "{RDS_36} contains 4",
          "title": "Other Skin Description",
          "isRequired": true,
          "Export Column Name": "Skin_Detail",
          "Export Column Order": 260,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation"
         },
         {
          "type": "checkbox",
          "name": "RDS_37",
          "title": "Cranium (select all that apply)",
          "description": "<img src=\"/assets/survey-images/CB_Cranium_Brachy_and_Dolicho.png\">",
          "isRequired": true,
          "Export Column Name": "Cranium",
          "Export Column Order": 265,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation",
          "choices": [
           {
            "value": "1",
            "text": "Normal Shape",
            "enableIf": "{RDS_37} notcontains 888"
           },
           {
            "value": "2",
            "text": "Brachycephaly (AP dimension /length compared to width appears shortened; head shape looks flattened)",
            "enableIf": "{RDS_37} notcontains 1 and {RDS_37} notcontains 888"
           },
           {
            "value": "3",
            "text": "Dolichocephaly (AP length of head compared to width appears increased; head shape looks long)",
            "enableIf": "{RDS_37} notcontains 1 and {RDS_37} notcontains 888"
           },
           {
            "value": "4",
            "text": "Other",
            "enableIf": "{RDS_37} notcontains 1 and {RDS_37} notcontains 888"
           },
           {
            "value": "888",
            "text": "Not Assessed",
            "enableIf": "{RDS_37} notcontains 1"
           }
          ]
         },
         {
          "type": "comment",
          "name": "RDS_37_OTHER",
          "visibleIf": "{RDS_37} contains 4",
          "title": "Other Cranium Description",
          "isRequired": true,
          "Export Column Name": "Cranium_Detail",
          "Export Column Order": 270,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation"
         },
         {
          "type": "checkbox",
          "name": "RDS_38",
          "title": "Scalp Hair/Hairline (select all that apply)",
          "description": "<br>Example: Double hair whorl<br><br>",
          "isRequired": true,
          "Export Column Name": "Scalp",
          "Export Column Order": 275,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation",
          "choices": [
           {
            "value": "1",
            "text": "Normal Scalp, Hair, and Hairline",
            "enableIf": "{RDS_38} notcontains 888"
           },
           {
            "value": "2",
            "text": "High Anterior Hairline",
            "enableIf": "{RDS_38} notcontains 1 and {RDS_38} notcontains 888"
           },
           {
            "value": "3",
            "text": "Abnormal Hair Whorl (the hair whorl is the single point on the scalp, normally in the midline and close to the vertex, where hair growth arises)",
            "enableIf": "{RDS_38} notcontains 1 and {RDS_38} notcontains 888"
           },
           {
            "value": "4",
            "text": "Other",
            "enableIf": "{RDS_38} notcontains 1 and {RDS_38} notcontains 888"
           },
           {
            "value": "888",
            "text": "Not Assessed",
            "enableIf": "{RDS_38} notcontains 1"
           }
          ]
         },
         {
          "type": "comment",
          "name": "RDS_38_OTHER",
          "visibleIf": "{RDS_38} contains 4",
          "title": "Other Scalp Hair/Hairline Description",
          "isRequired": true,
          "Export Column Name": "Scalp_Detail",
          "Export Column Order": 280,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation"
         },
         {
          "type": "checkbox",
          "name": "RDS_39",
          "title": "Eyes and Periorbital Region (select all that apply)",
          "description": "<br>Example: Epicanthic Eye Fold<br><br>",
          "isRequired": true,
          "Export Column Name": "Eyes",
          "Export Column Order": 285,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation",
          "choices": [
           {
            "value": "1",
            "text": "Normal Form and Position",
            "enableIf": "{RDS_39} notcontains 888"
           },
           {
            "value": "2",
            "text": "Deep-set Eyes (in profile: eyes that are more deeply recessed into the plane of the face than is typical)",
            "enableIf": "{RDS_39} notcontains 1 and {RDS_39} notcontains 888"
           },
           {
            "value": "3",
            "text": "Hypertelorism (eyes that appear widely spaced)",
            "enableIf": "{RDS_39} notcontains 1 and {RDS_39} notcontains 888"
           },
           {
            "value": "4",
            "text": "Epicanthic Eye Folds",
            "enableIf": "{RDS_39} notcontains 1 and {RDS_39} notcontains 888"
           },
           {
            "value": "5",
            "text": "Synophrys (meeting of the medial eyebrows in the midline)",
            "enableIf": "{RDS_39} notcontains 1 and {RDS_39} notcontains 888"
           },
           {
            "value": "6",
            "text": "Other",
            "enableIf": "{RDS_39} notcontains 1 and {RDS_39} notcontains 888"
           },
           {
            "value": "888",
            "text": "Not Assessed",
            "enableIf": "{RDS_39} notcontains 1"
           }
          ]
         },
         {
          "type": "comment",
          "name": "RDS_39_OTHER",
          "visibleIf": "{RDS_39} contains 6",
          "title": "Other Eyes and Periorbital Region Description",
          "isRequired": true,
          "Export Column Name": "Eyes_Detail",
          "Export Column Order": 290,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation"
         },
         {
          "type": "checkbox",
          "name": "RDS_40",
          "title": "Ears (select all that apply)\n",
          "description": "<br>Examples: Abnormal form (Stahl's ear, pointed), Abnormal form (cleft lobe), Abnormal form (attached lobe)<br><br>",
          "isRequired": true,
          "Export Column Name": "Ears",
          "Export Column Order": 295,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation",
          "choices": [
           {
            "value": "1",
            "text": "Normal Size, Form and Position",
            "enableIf": "{RDS_40} notcontains 888"
           },
           {
            "value": "2",
            "text": "Abnormal Location/Position (for example, ears appear low set)",
            "enableIf": "{RDS_40} notcontains 1 and {RDS_40} notcontains 888"
           },
           {
            "value": "3",
            "text": "Abnormal Form",
            "enableIf": "{RDS_40} notcontains 1 and {RDS_40} notcontains 888"
           },
           {
            "value": "4",
            "text": "Small Ears",
            "enableIf": "{RDS_40} notcontains 1 and {RDS_40} notcontains 888"
           },
           {
            "value": "5",
            "text": "Other",
            "enableIf": "{RDS_40} notcontains 1 and {RDS_40} notcontains 888"
           },
           {
            "value": "888",
            "text": "Not Assessed",
            "enableIf": "{RDS_40} notcontains 1"
           }
          ]
         },
         {
          "type": "comment",
          "name": "RDS_40_OTHER",
          "visibleIf": "{RDS_40} contains 5",
          "title": "Other Ears Description",
          "isRequired": true,
          "Export Column Name": "Ears_Detail",
          "Export Column Order": 300,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation"
         },
         {
          "type": "checkbox",
          "name": "RDS_41",
          "title": "Nose and Philtrum (select all that apply)",
          "description": "<br>Examples: Long Philtrum, Short,  Abnormal nasal bridge (depressed)<br><br>",
          "isRequired": true,
          "Export Column Name": "Nose_Philtrum",
          "Export Column Order": 305,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation",
          "choices": [
           {
            "value": "1",
            "text": "Normal Nose and Philtrum",
            "enableIf": "{RDS_41} notcontains 888"
           },
           {
            "value": "2",
            "text": "Abnormal Nasal Bridge",
            "enableIf": "{RDS_41} notcontains 1 and {RDS_41} notcontains 888"
           },
           {
            "value": "3",
            "text": "Long Nose",
            "enableIf": "{RDS_41} notcontains 1 and {RDS_41} notcontains 888"
           },
           {
            "value": "4",
            "text": "Short Nose",
            "enableIf": "{RDS_41} notcontains 1 and {RDS_41} notcontains 888"
           },
           {
            "value": "5",
            "text": "Long Philtrum",
            "enableIf": "{RDS_41} notcontains 1 and {RDS_41} notcontains 888"
           },
           {
            "value": "6",
            "text": "Short Philtrum",
            "enableIf": "{RDS_41} notcontains 1 and {RDS_41} notcontains 888"
           },
           {
            "value": "7",
            "text": "Other",
            "enableIf": "{RDS_41} notcontains 1 and {RDS_41} notcontains 888"
           },
           {
            "value": "888",
            "text": "Not Assessed",
            "enableIf": "{RDS_41} notcontains 1"
           }
          ]
         },
         {
          "type": "comment",
          "name": "RDS_41_OTHER",
          "visibleIf": "{RDS_41} contains 7",
          "title": "Other Nose and Philtrum Description",
          "isRequired": true,
          "Export Column Name": "Nose_Philtrum_Detail",
          "Export Column Order": 310,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation"
         },
         {
          "type": "checkbox",
          "name": "RDS_42",
          "title": "Lips/Mouth/Teeth (select all that apply)",
          "description": "<br>Example: Thin lips<br><br>",
          "isRequired": true,
          "Export Column Name": "Lips_Mouth_Teeth",
          "Export Column Order": 315,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation",
          "choices": [
           {
            "value": "1",
            "text": "Normal Lips, Mouth, and Teeth",
            "enableIf": "{RDS_42} notcontains 888"
           },
           {
            "value": "2",
            "text": "Abnormal Lips",
            "enableIf": "{RDS_42} notcontains 1 and {RDS_42} notcontains 888"
           },
           {
            "value": "3",
            "text": "Abnormal Mouth (oral cavity including hard and soft palate, and the tongue)",
            "enableIf": "{RDS_42} notcontains 1 and {RDS_42} notcontains 888"
           },
           {
            "value": "4",
            "text": "Abnormal Teeth",
            "enableIf": "{RDS_42} notcontains 1 and {RDS_42} notcontains 888"
           },
           {
            "value": "5",
            "text": "Thin Lips",
            "enableIf": "{RDS_42} notcontains 1 and {RDS_42} notcontains 888"
           },
           {
            "value": "6",
            "text": "Other",
            "enableIf": "{RDS_42} notcontains 1 and {RDS_42} notcontains 888"
           },
           {
            "value": "888",
            "text": "Not Assessed",
            "enableIf": "{RDS_42} notcontains 1"
           }
          ]
         },
         {
          "type": "comment",
          "name": "RDS_42_OTHER",
          "visibleIf": "{RDS_42} contains 6",
          "title": "Other Lips/Mouth/Teeth Description",
          "isRequired": true,
          "Export Column Name": "Lips_Mouth_Teeth_Detail",
          "Export Column Order": 320,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation"
         },
         {
          "type": "checkbox",
          "name": "RDS_43",
          "title": "Hands/Fingers/Nails (select all that apply)",
          "description": "<br>Examples: Tapered Fingers, Abnormal palmer crease (deep), Abnormal palmar crease (single transverse crease)<br><br>",
          "isRequired": true,
          "Export Column Name": "Hands_Fingers_Nails",
          "Export Column Order": 325,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation",
          "choices": [
           {
            "value": "1",
            "text": "Normal Hands, Fingers, and Nails",
            "enableIf": "{RDS_43} notcontains 888"
           },
           {
            "value": "2",
            "text": "Abnormal Palmar Creases",
            "enableIf": "{RDS_43} notcontains 1 and {RDS_43} notcontains 888"
           },
           {
            "value": "3",
            "text": "Clinodactyly (curving of the finger)",
            "enableIf": "{RDS_43} notcontains 1 and {RDS_43} notcontains 888"
           },
           {
            "value": "4",
            "text": "Tapering Fingers",
            "enableIf": "{RDS_43} notcontains 1 and {RDS_43} notcontains 888"
           },
           {
            "value": "5",
            "text": "Abnormal Fingernails",
            "enableIf": "{RDS_43} notcontains 1 and {RDS_43} notcontains 888"
           },
           {
            "value": "6",
            "text": "Other",
            "enableIf": "{RDS_43} notcontains 1 and {RDS_43} notcontains 888"
           },
           {
            "value": "888",
            "text": "Not Assessed",
            "enableIf": "{RDS_43} notcontains 1"
           }
          ]
         },
         {
          "type": "comment",
          "name": "RDS_43_OTHER",
          "visibleIf": "{RDS_43} contains 6",
          "title": "Other Hands/Fingers/Nails Description",
          "isRequired": true,
          "Export Column Name": "Hands_Fingers_Nails_Detail",
          "Export Column Order": 330,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation"
         },
         {
          "type": "checkbox",
          "name": "RDS_44",
          "title": "Feet/Toes/Toenails (select all that apply)",
          "description": "<br>Example: Overriding Toes<br><br>",
          "isRequired": true,
          "Export Column Name": "Feet_Toes_Toenails",
          "Export Column Order": 335,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation",
          "choices": [
           {
            "value": "1",
            "text": "Normal Feet, Toes, and Toenails",
            "enableIf": "{RDS_44} notcontains 888"
           },
           {
            "value": "2",
            "text": "Over-riding Toes",
            "enableIf": "{RDS_44} notcontains 1 and {RDS_44} notcontains 888"
           },
           {
            "value": "3",
            "text": "Abnormal Toenails",
            "enableIf": "{RDS_44} notcontains 1 and {RDS_44} notcontains 888"
           },
           {
            "value": "4",
            "text": "Other",
            "enableIf": "{RDS_44} notcontains 1 and {RDS_44} notcontains 888"
           },
           {
            "value": "888",
            "text": "Not Assessed",
            "enableIf": "{RDS_44} notcontains 1"
           }
          ]
         },
         {
          "type": "comment",
          "name": "RDS_44_OTHER",
          "visibleIf": "{RDS_44} contains 4",
          "title": "Other Feet/Toes/Toenails Description",
          "isRequired": true,
          "Export Column Name": "Feet_Toes_Toenails_Detail",
          "Export Column Order": 340,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation"
         },
         {
          "type": "comment",
          "name": "RDS_COMMENTS",
          "title": "Comments (please, no PHI)",
          "Export Column Name": "Comments",
          "Export Column Order": 345,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Evaluation"
         }
        ],
        "title": "Assessments"
       }
      ]
     }
    ],
    "triggers": [
     {
      "type": "setvalue",
      "expression": "{RDS_32} contains 3",
      "setToName": "RDS_32",
      "setValue": [
       "3"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{RDS_36} contains 1",
      "setToName": "RDS_36",
      "setValue": [
       "1"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{RDS_36} contains 888",
      "setToName": "RDS_36",
      "setValue": [
       "888"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{RDS_37} contains 1",
      "setToName": "RDS_37",
      "setValue": [
       "1"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{RDS_37} contains 888",
      "setToName": "RDS_37",
      "setValue": [
       "888"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{RDS_38} contains 1",
      "setToName": "RDS_38",
      "setValue": [
       "1"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{RDS_38} contains 888",
      "setToName": "RDS_38",
      "setValue": [
       "888"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{RDS_39} contains 1",
      "setToName": "RDS_39",
      "setValue": [
       "1"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{RDS_39} contains 888",
      "setToName": "RDS_39",
      "setValue": [
       "888"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{RDS_40} contains 1",
      "setToName": "RDS_40",
      "setValue": [
       "1"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{RDS_40} contains 888",
      "setToName": "RDS_40",
      "setValue": [
       "888"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{RDS_41} contains 1",
      "setToName": "RDS_41",
      "setValue": [
       "1"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{RDS_41} contains 888",
      "setToName": "RDS_41",
      "setValue": [
       "888"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{RDS_42} contains 1",
      "setToName": "RDS_42",
      "setValue": [
       "1"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{RDS_42} contains 888",
      "setToName": "RDS_42",
      "setValue": [
       "888"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{RDS_43} contains 1",
      "setToName": "RDS_43",
      "setValue": [
       "1"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{RDS_43} contains 888",
      "setToName": "RDS_43",
      "setValue": [
       "888"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{RDS_44} contains 1",
      "setToName": "RDS_44",
      "setValue": [
       "1"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{RDS_44} contains 888",
      "setToName": "RDS_44",
      "setValue": [
       "888"
      ]
     }
    ],
    "showQuestionNumbers": "off",
    "clearInvisibleValues": "onHidden"
   }
'''

# List of words to find
word_list = ["Study_ID","RDS_Compl_Date","Examiner_Name","Invalid_YN","Invalid_Reason","Invalid_Reason_Other","Fam_Hx_Dev_Disab_YN","Fam_Hx_Dev_Disab_Detail","Fam_Hx_Structure_Abn_YN","Fam_Hx_Structure_Abn_Detail","Bio_Parents_Related_YN","Bio_Parents_Related_Detail","Gestation_at_Birth_wks","Gestation_Msmt_Date","Gestation_Source","Gestation_Source_Other","Birth_Wt_kg","Birth_Wt_Date","Birth_Wt_Source","Birth_Wt_Source_Other","Birth_Lgth_cm","Birth_Lgth_Date","Birth_Lgth_Source","Birth_Lgth_Source_Other","Birth_Head_Circum_cm","Birth_Head_Circum_Date","Birth_Head_Circum_Source","Birth_Head_Circum_Source_Other","Most_Recent_Wt_kg","Most_Recent_Wt_Std_Dev","Most_Recent_Wt_Date","Most_Recent_Wt_Source","Most_Recent_Wt_Source_Other","Most_Recent_Ht_cm","Most_Recent_Ht_Std_Dev","Most_Recent_Ht_Date","Most_Recent_Ht_Source","Most_Recent_Ht_Source_Other","Most_Recent_Head_Circum_cm","Most_Recent_Head_Circum_Std_Dev","Most_Recent_Head_Circum_Date","Most_Recent_Head_Circum_Source","Most_Recent_Head_Circum_Source_Other","Bio_Parent_At_Appt","Dysmorphic_YN","Ununual_Facial_Features_Parent_YN","Unusual_Facial_Features_Detail","Habitus_YN","Habitus_Detail","Skin","Skin_Detail","Cranium","Cranium_Detail","Scalp","Scalp_Detail","Eyes","Eyes_Detail","Ears","Ears_Detail","Nose_Philtrum","Nose_Philtrum_Detail","Lips_Mouth_Teeth","Lips_Mouth_Teeth_Detail","Hands_Fingers_Nails","Hands_Fingers_Nails_Detail","Feet_Toes_Toenails","Feet_Toes_Toenails_Detail","Comments"]

# Find words in the string
found_words = find_words_in_string(input_string, word_list)

# Print the result
print("Words found in the string:", found_words)