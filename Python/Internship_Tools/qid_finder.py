def find_words_in_string(input_string, word_list):
    found_words = [word for word in word_list if word in input_string]
    return found_words

# Example usage
input_string = '''
{
    "title": "RA - Neurological Exam",
    "description": "IDDRC-CTSA National Brain Gene Registry ",
    "pages": [
     {
      "name": "page1",
      "elements": [
       {
        "type": "text",
        "name": "NEURO_1",
        "title": "NEURO Study ID",
        "description": "<br>(site ID 1xx, family ID xxx, sub ID 101, 130, 140)<br><br>",
        "isRequired": true,
        "Export Column Name": "Study_ID",
        "Export Column Order": 5,
        "Pii flag": true,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Administration"
       },
       {
        "type": "text",
        "name": "NEURO_2",
        "title": "Date of completing the NEURO",
        "isRequired": true,
        "Export Column Name": "NEURO_Compl_Date",
        "Export Column Order": 10,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Administration",
        "inputType": "date"
       },
       {
        "type": "text",
        "name": "NEURO_3",
        "title": "Name of the Examiner",
        "isRequired": true,
        "Export Column Name": "Examiner_Name",
        "Export Column Order": 15,
        "Pii flag": true,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Administration"
       },
       {
        "type": "checkbox",
        "name": "NEURO_4",
        "title": "Please indicate here if assessment is considered valid.",
        "titleLocation": "hidden",
        "Export Column Name": "Asses_Invalid_YN",
        "Export Column Order": 20,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Administration",
        "choices": [
         {
          "value": "1",
          "text": "Please indicate here if assessment is considered invalid."
         }
        ]
       },
       {
        "type": "checkbox",
        "name": "NEURO_5",
        "visibleIf": "{NEURO_4} = [1]",
        "title": "If assessment is invalid, please indicate the reason(s):",
        "isRequired": true,
        "Export Column Name": "Assess_Invalid_Reason",
        "Export Column Order": 25,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Administration",
        "choices": [
         {
          "value": "1",
          "text": "Child behavioral issues (e.g. difficulty with cooperation, etc.) impacted assessment"
         },
         {
          "value": "2",
          "text": "Other"
         }
        ]
       },
       {
        "type": "comment",
        "name": "NEURO_6",
        "visibleIf": "{NEURO_5} contains 2",
        "title": "Specify other reason",
        "isRequired": true,
        "Export Column Name": "Assess_Invalid_Reason_Other",
        "Export Column Order": 30,
        "Pii flag": true,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Administration"
       },
       {
        "type": "comment",
        "name": "NEURO_7",
        "title": "Any comments",
        "Export Column Name": "Comments",
        "Export Column Order": 35,
        "Pii flag": true,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Administration"
       },
       {
        "type": "radiogroup",
        "name": "question8",
        "title": "Child's/Individual's Age",
        "isRequired": true,
        "Export Column Name": "Age",
        "Export Column Order": 40,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Administration",
        "choices": [
         {
          "value": "1",
          "text": "< 12 months"
         },
         {
          "value": "2",
          "text": "12-36 months"
         },
         {
          "value": "3",
          "text": "3+ years"
         },
         {
          "value": "4",
          "text": "37 months - 15 years, 11 months"
         },
         {
          "value": "5",
          "text": "16 years and older"
         }
        ]
       }
      ]
     },
     {
      "name": "page2",
      "elements": [
       {
        "type": "panel",
        "name": "Page2Panel",
        "elements": [
         {
          "type": "radiogroup",
          "name": "NEURO_9",
          "title": "Is the child / individual awake and alert?",
          "isRequired": true,
          "Export Column Name": "Awake_Alert_YN",
          "Export Column Order": 45,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Alert and Interactive",
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
            "text": "Unknown"
           }
          ]
         },
         {
          "type": "comment",
          "name": "NEURO_10_SPECIFY",
          "visibleIf": "{NEURO_9} = 0",
          "title": "If No, please specify as needed",
          "Export Column Name": "Awake_Alert_No_Specify",
          "Export Column Order": 50,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Alert and Interactive"
         },
         {
          "type": "radiogroup",
          "name": "NEURO_11",
          "title": "Is the child / individual appropriately interactive\nwith the environment/caregiver?",
          "description": "<br>[For children under 16]: Observe the interaction of the child with the caregiver. Have the caregiver smile, make funny faces, and play peek-a-boo with the child. \n<br><br>\n[For children 16 and older]: Observe the interactions of the individual throughout the visit with the examiner and/or any other individuals if present. Pay attention when first greeting the individual to see if they respond to your smile, respond to your social initiations (conversation, chit-chat), etc. Are their thoughts coherent, etc.?<br><br>",
          "isRequired": true,
          "Export Column Name": "Interactive_YN",
          "Export Column Order": 55,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Alert and Interactive",
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
            "text": "Unknown"
           }
          ]
         },
         {
          "type": "comment",
          "name": "NEURO_11_SPECIFY",
          "visibleIf": "{NEURO_11} = 0",
          "title": "If No, please specify as needed",
          "Export Column Name": "Interactive_No_Specify",
          "Export Column Order": 60,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Alert and Interactive"
         },
         {
          "type": "radiogroup",
          "name": "NEURO_12",
          "title": "Does the child track appropriately? ",
          "description": "<br>Observe the parent moving a visually interesting toy (which does not make sounds) in all directions (left, right, up, and down). Note that the ability to visually track horizontally and vertically develops by age 2 months, and the ability to visually follow in a 360 degree circle develops by age 3 months.<br><br>",
          "isRequired": true,
          "Export Column Name": "Track_Appropriately_YN",
          "Export Column Order": 65,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Vision",
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
            "text": "Unknown"
           }
          ]
         },
         {
          "type": "comment",
          "name": "NEURO_12_SPECIFY",
          "visibleIf": "{NEURO_12} = 0",
          "title": "If No, please specify as needed",
          "Export Column Name": "Track_Appropriately_No_Specify",
          "Export Column Order": 70,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Vision"
         },
         {
          "type": "radiogroup",
          "name": "NEURO_13",
          "title": "Does the individual wear glasses/contacts or report any vision deficits? ",
          "isRequired": true,
          "Export Column Name": "Glasses_Contacts_YN",
          "Export Column Order": 75,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Vision",
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
            "text": "Unknown"
           }
          ]
         },
         {
          "type": "comment",
          "name": "NEURO_13_SPECIFY",
          "visibleIf": "{NEURO_13} = 1",
          "title": "If Yes, please specify as needed ",
          "Export Column Name": "Glasses_Contacts_Yes_Specify",
          "Export Column Order": 80,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Vision"
         },
         {
          "type": "radiogroup",
          "name": "NEURO_14",
          "title": "Are extraocular movements intact? ",
          "description": "<br>[For children under 16]: Observe the parent moving a visually interesting toy (which does not make sounds) in all directions (left, right, up, and down). \n<br><br>\n[For 16 and older]: Ask the individual to follow your finger with their eyes, then present your finger in the center of the camera screen and move it in all directions (left, right, up, and down).<br><br>",
          "isRequired": true,
          "Export Column Name": "Extraocular_Mvmt_Intact_YN",
          "Export Column Order": 85,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Vision",
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
            "text": "Unknown"
           }
          ]
         },
         {
          "type": "comment",
          "name": "NEURO_14_SPECIFY",
          "visibleIf": "{NEURO_14} = 0",
          "title": "If No, please specify as needed",
          "Export Column Name": "Extraocular_Mvmt_Intact_No_Specify",
          "Export Column Order": 90,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Vision"
         },
         {
          "type": "radiogroup",
          "name": "NEURO_15",
          "title": "Are the eye movements conjugate? ",
          "isRequired": true,
          "Export Column Name": "Eye_Mvmt_Conjugate_YN",
          "Export Column Order": 95,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Vision",
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
            "text": "Unknown"
           }
          ]
         },
         {
          "type": "comment",
          "name": "NEURO_15_SPECIFY",
          "visibleIf": "{NEURO_15} = 0",
          "title": "If No, please specify as needed",
          "Export Column Name": "Eye_Mvmt_Conjugate_No_Specify",
          "Export Column Order": 100,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Vision"
         },
         {
          "type": "radiogroup",
          "name": "NEURO_16",
          "title": "Is there evidence of nystagmus? ",
          "isRequired": true,
          "Export Column Name": "Nystagmus_YN",
          "Export Column Order": 105,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Vision",
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
            "text": "Unknown"
           }
          ]
         },
         {
          "type": "comment",
          "name": "NEURO_16_SPECIFY",
          "visibleIf": "{NEURO_16} = 1",
          "title": "If Yes, please specify as needed ",
          "Export Column Name": "Nystagmus_No_Specify",
          "Export Column Order": 110,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Vision"
         },
         {
          "type": "radiogroup",
          "name": "NEURO_17",
          "title": "Are the facial movements symmetric? ",
          "description": "<br>[For children under 16]: Observe the child's facial expression in neutral affect and while smiling/laughing/crying. \n<br><br>\n[For 16 and older] Ask individual to raise eyebrows, puff out cheeks and smile. Alternatively, observe facial expression throughout the visit, paying attention to symmetry during neutral affect and while smiling/laughing/crying (if crying happens naturally)<br><br>",
          "isRequired": true,
          "Export Column Name": "Facial_Mvmt_Symmetric_YN",
          "Export Column Order": 115,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Facial",
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
            "text": "Unknown"
           }
          ]
         },
         {
          "type": "comment",
          "name": "NEURO_17_SPECIFY",
          "visibleIf": "{NEURO_17} = 0",
          "title": "If No, please specify as needed",
          "Export Column Name": "Facial_Mvmt_Symmetric_No_Specify",
          "Export Column Order": 120,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Facial"
         },
         {
          "type": "radiogroup",
          "name": "NEURO_18",
          "title": "Are tongue protrusions normal? ",
          "description": "<br>Have the child / individual mimic the examiner's own tongue movements.<br><br>",
          "isRequired": true,
          "Export Column Name": "Tongue_Protru_Normal_YN",
          "Export Column Order": 125,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Facial",
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
            "text": "Unknown"
           }
          ]
         },
         {
          "type": "comment",
          "name": "NEURO_18_SPECIFY",
          "visibleIf": "{NEURO_18} = 0",
          "title": "If No, please specify as needed",
          "Export Column Name": "Tongue_Protru_Normal_No_Specify",
          "Export Column Order": 130,
          "Pii flag": true,
          "IsNotAnalyze-Able?": true,
          "IsNotPull-ForwardEligible": true,
          "Analyze Question Group/Name": "Facial"
         }
        ],
        "title": "*Caution: Be sure to ask about any issues with balance or falling prior to asking individual to do certain activities (getting up from the floor or a seated position, walking, etc.). If individual is alone during telehealth and is at risk for falls, then obtain information through interview (ask individual if they have difficulty in those areas) verses having them demonstrate those activities. "
       }
      ]
     },
     {
      "name": "page3",
      "elements": [
       {
        "type": "radiogroup",
        "name": "NEURO_19_PAR",
        "title": "Is hearing normal based on parental report?",
        "isRequired": true,
        "Export Column Name": "Hearing_Normal_Parent_YN",
        "Export Column Order": 135,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Hearing",
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
          "text": "Unknown"
         }
        ]
       },
       {
        "type": "radiogroup",
        "name": "NEURO_19_INDIV",
        "title": "Is hearing normal based on individual report? ",
        "description": "<br>Ask individual, or their caregiver, if they have any hearing issues and/or if other's report issues with individual's hearing.<br><br>",
        "Export Column Name": "Hearing_Normal_Indiv_YN",
        "Export Column Order": 140,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Hearing",
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
          "text": "Unknown"
         }
        ]
       },
       {
        "type": "comment",
        "name": "NEURO_19_SPECIFY",
        "visibleIf": "{NEURO_19_PAR} = 0 or {NEURO_19_INDIV} = 0",
        "title": "If No, please specify as needed",
        "Export Column Name": "Hearing_Normal_No_Specify",
        "Export Column Order": 145,
        "Pii flag": true,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Hearing"
       },
       {
        "type": "radiogroup",
        "name": "NEURO_20",
        "title": "Is there evidence of hypotonia? ",
        "description": "<br>[For < 12mos]: Observe the child in supine position. Are legs in a frog-legged position suggesting hypotonia? Observe child in prone to see if child can support chin off table in prone (1 month age equivalent ability), support chest off table in prone (2 month age equivalent ability), support on forearms in prone (3 month age equivalent ability), or support on wrists in prone (4 month age equivalent ability). Decreased ability to perform these milestones based on age could suggest axial hypotonia (with the caveat that it could also reflect decreased visual motor developmental quotient).  \n<br><br>\n[For children between 12m and 16 years]: Observe the child in sitting position. Is there decreased head control suggestive of axial hypotonia? \n<br><br>\n[For 16 and older]: This can be assessed by asking if a service provider has ever said they have low muscle tone or hypotonia.<br><br>",
        "isRequired": true,
        "Export Column Name": "Hypotonia_YN",
        "Export Column Order": 150,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Tone",
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
          "text": "Unknown"
         }
        ]
       },
       {
        "type": "checkbox",
        "name": "NEURO_20_SPECIFY",
        "visibleIf": "{NEURO_20} = 1",
        "title": "If Yes, please specify (multiple choices allowed)",
        "isRequired": true,
        "Export Column Name": "Hypotonia_Yes_Specify",
        "Export Column Order": 155,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Tone",
        "choices": [
         {
          "value": "1",
          "text": "Appendicular hypotonia",
          "enableIf": "{NEURO_20_SPECIFY} <> [999] and {NEURO_20_SPECIFY} <> [999, 1] and {NEURO_20_SPECIFY} <> [999, 2] and {NEURO_20_SPECIFY} <> [1, 2, 999]"
         },
         {
          "value": "2",
          "text": "Axial hypotonia",
          "enableIf": "{NEURO_20_SPECIFY} <> [999] and {NEURO_20_SPECIFY} <> [999, 1] and {NEURO_20_SPECIFY} <> [999, 2] and {NEURO_20_SPECIFY} <> [1, 2, 999]"
         },
         {
          "value": "999",
          "text": "Unknown"
         }
        ]
       },
       {
        "type": "radiogroup",
        "name": "NEURO_21",
        "title": "Is there evidence of hypertonia? ",
        "description": "<br>[For children under 16]: Observe the child in supine position. Do legs remain hyperextended (inappropriate for age/state) that could suggest hypertonia? \n<br><br>\n[For 16 and older]:  This can be assessed by asking if a service provider has ever said they have increased muscle tone or hypertonia.<br><br>",
        "isRequired": true,
        "Export Column Name": "Hypertonia_YN",
        "Export Column Order": 160,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Tone",
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
          "text": "Unknown"
         }
        ]
       },
       {
        "type": "checkbox",
        "name": "NEURO_21_SPECIFY",
        "visibleIf": "{NEURO_21} = 1",
        "title": "If Yes, please specify (multiple choices allowed) ",
        "isRequired": true,
        "Export Column Name": "Hypertonia_Yes_Specify",
        "Export Column Order": 165,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Tone",
        "choices": [
         {
          "value": "1",
          "text": "Axial hypertonia",
          "enableIf": "{NEURO_21_SPECIFY} notcontains 999"
         },
         {
          "value": "2",
          "text": "Spasticity",
          "enableIf": "{NEURO_21_SPECIFY} notcontains 999"
         },
         {
          "value": "3",
          "text": "Rigidity",
          "enableIf": "{NEURO_21_SPECIFY} notcontains 999"
         },
         {
          "value": "4",
          "text": "Other",
          "enableIf": "{NEURO_21_SPECIFY} notcontains 999"
         },
         {
          "value": "999",
          "text": "Unknown"
         }
        ]
       },
       {
        "type": "comment",
        "name": "NEURO_21_OTHER",
        "visibleIf": "{NEURO_21_SPECIFY} contains 4",
        "title": "Other hypertonia features",
        "Export Column Name": "Hypertonia_Yes_Other",
        "Export Column Order": 170,
        "Pii flag": true,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Tone"
       },
       {
        "type": "radiogroup",
        "name": "NEURO_22",
        "title": "Is there dystonia? ",
        "description": "<br>[For children under 16]: Observe for involuntary twisting/abnormal postures in the child's upper extremities, lower extremities, and trunk. \n<br><br>\n[For 16 and older]: Observe for involuntary twisting/abnormal postures in the individual's upper extremities, lower extremities, and trunk. This can be assessed when asking individual to stand and walk (see gait below).<br><br>",
        "isRequired": true,
        "Export Column Name": "Dystonia_YN",
        "Export Column Order": 175,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Tone",
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
          "text": "Unknown"
         }
        ]
       },
       {
        "type": "comment",
        "name": "NEURO_22_SPECIFY",
        "visibleIf": "{NEURO_22} = 1",
        "title": "If Yes, please specify as needed",
        "Export Column Name": "Dystonia_Yes_Specify",
        "Export Column Order": 180,
        "Pii flag": true,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Tone"
       },
       {
        "type": "radiogroup",
        "name": "NEURO_23",
        "title": "Are upper and lower extremity movements symmetric? ",
        "description": "<br>[For children under 16]: Observe the child's natural\nmovements at rest and with play. \n<br><br>\n[For 16 and older] : Observe natural movements at rest and while using any objects (picking up phone, adjusting position of device). Ask if one side of their body is noticeably weaker than the other.<br><br>",
        "isRequired": true,
        "Export Column Name": "Extremity_Mvmt_Symmetric_YN",
        "Export Column Order": 185,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Movements",
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
          "text": "Unknown"
         }
        ]
       },
       {
        "type": "comment",
        "name": "NEURO_23_SPECIFY",
        "visibleIf": "{NEURO_23} = 0",
        "title": "If No, please specify as needed",
        "Export Column Name": "Extremity_Mvmt_Symmetric_No_Specify",
        "Export Column Order": 190,
        "Pii flag": true,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Movements"
       },
       {
        "type": "radiogroup",
        "name": "NEURO_24",
        "title": "Is there evidence of weakness? ",
        "description": "<br>[For children under 16]: Have the child sit on the ground and then get up to get keys from the parent (watch for Gower). \n<br><br>\n[For 16 and older]: Ask individual to put out their hands (toward camera) with palms up, fingers spread, and close eyes (this can be done while seated). Observe for signs of weakness such as, one arm drifting downward and/or a palm turns toward the floor. Ask if one side of their body is noticeably weaker than the other.<br><br>",
        "isRequired": true,
        "Export Column Name": "Weakness_YN",
        "Export Column Order": 195,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Movements",
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
          "text": "Unknown"
         }
        ]
       },
       {
        "type": "checkbox",
        "name": "NEURO_24_SPECIFY",
        "visibleIf": "{NEURO_24} = 1",
        "title": "If Yes, please specify (multiple choices allowed) ",
        "isRequired": true,
        "Export Column Name": "Weakness_Yes_Specify",
        "Export Column Order": 200,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Movements",
        "choices": [
         {
          "value": "1",
          "text": "Weakness in right arm",
          "enableIf": "{NEURO_24_SPECIFY} notcontains 999"
         },
         {
          "value": "2",
          "text": "Weakness in right leg",
          "enableIf": "{NEURO_24_SPECIFY} notcontains 999"
         },
         {
          "value": "3",
          "text": "Weakness in left arm",
          "enableIf": "{NEURO_24_SPECIFY} notcontains 999"
         },
         {
          "value": "4",
          "text": "Weakness in left leg",
          "enableIf": "{NEURO_24_SPECIFY} notcontains 999"
         },
         {
          "value": "5",
          "text": "Other",
          "enableIf": "{NEURO_24_SPECIFY} notcontains 999"
         },
         {
          "value": "999",
          "text": "Unknown"
         }
        ]
       },
       {
        "type": "comment",
        "name": "NEURO_24_OTHER",
        "visibleIf": "{NEURO_24_SPECIFY} contains 5",
        "title": "Other Weakness",
        "Export Column Name": "Weakness_Yes_Other",
        "Export Column Order": 205,
        "Pii flag": true,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Movements"
       },
       {
        "type": "radiogroup",
        "name": "NEURO_25",
        "title": "Is there evidence of tremor?",
        "description": "<br>[For children under 16]: Observe the child's ability to reach for a toy with both hands. \n<br><br>\n[For 16 and older]: Ask individual to extend their arms with fingers pointed in the direction of the camera to observe for tremor. If unable to assess this way, ask individual or their caregiver if they've noticed any tremor in their hands.<br><br>",
        "isRequired": true,
        "Export Column Name": "Tremor_YN",
        "Export Column Order": 210,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Movements",
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
          "text": "Unknown"
         }
        ]
       },
       {
        "type": "comment",
        "name": "NEURO_25_SPECIFY",
        "visibleIf": "{NEURO_25} = 1",
        "title": "If Yes, please specify as needed ",
        "Export Column Name": "Tremor_Yes_Specify",
        "Export Column Order": 215,
        "Pii flag": true,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Movements"
       },
       {
        "type": "radiogroup",
        "name": "NEURO_26",
        "title": "Is there dysmetria? ",
        "description": "<br>[For children under 16]: Observe the child's ability to reach for a toy with both hands. \n<br><br>\n[For 16 and older] : Observe individual's ability to reach for an object (phone, pen, book) with both hands. Have individual place a pen down on a surface in front of them and ask them to pick it up with each hand.<br><br>",
        "isRequired": true,
        "Export Column Name": "Dysmetria_YN",
        "Export Column Order": 220,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Movements",
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
          "text": "Unknown"
         }
        ]
       },
       {
        "type": "comment",
        "name": "NEURO_26_SPECIFY",
        "visibleIf": "{NEURO_26} = 1",
        "title": "If Yes, please specify as needed ",
        "Export Column Name": "Dysmetria_Yes_Specify",
        "Export Column Order": 225,
        "Pii flag": true,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Movements"
       },
       {
        "type": "radiogroup",
        "name": "NEURO_27",
        "title": "Can the child / individual walk independently? ",
        "description": "<br>[For 16 and older]: *Ask individual to walk in a straight line away from camera, towards camera.<br><br>",
        "isRequired": true,
        "Export Column Name": "Walk_Indep_YN",
        "Export Column Order": 230,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Walking",
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
          "text": "Unknown"
         }
        ]
       },
       {
        "type": "comment",
        "name": "NEURO_27_SPECIFY",
        "visibleIf": "{NEURO_27} = 0",
        "title": "If No, please specify as needed",
        "Export Column Name": "Walk_Indep_No_Specify",
        "Export Column Order": 235,
        "Pii flag": true,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Walking"
       },
       {
        "type": "radiogroup",
        "name": "NEURO_28",
        "title": "Is there evidence of abnormal gait? ",
        "isRequired": true,
        "Export Column Name": "Abn_Gait_YN",
        "Export Column Order": 240,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Walking",
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
          "text": "Unknown"
         }
        ]
       },
       {
        "type": "checkbox",
        "name": "NEURO_28_SPECIFY",
        "visibleIf": "{NEURO_28} = 1",
        "title": "If Yes, please specify (multiple choices allowed) ",
        "isRequired": true,
        "Export Column Name": "Abn_Gait_Yes_Specify",
        "Export Column Order": 245,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Walking",
        "choices": [
         {
          "value": "1",
          "text": "Ataxic gait",
          "enableIf": "{NEURO_28_SPECIFY} notcontains 999"
         },
         {
          "value": "2",
          "text": "Hypotonic gait",
          "enableIf": "{NEURO_28_SPECIFY} notcontains 999"
         },
         {
          "value": "3",
          "text": "Hemiparetic gait",
          "enableIf": "{NEURO_28_SPECIFY} notcontains 999"
         },
         {
          "value": "4",
          "text": "Spastic gait",
          "enableIf": "{NEURO_28_SPECIFY} notcontains 999"
         },
         {
          "value": "5",
          "text": "Other",
          "enableIf": "{NEURO_28_SPECIFY} notcontains 999"
         },
         {
          "value": "999",
          "text": "Unknown"
         }
        ]
       },
       {
        "type": "comment",
        "name": "NEURO_28_OTHER",
        "visibleIf": "{NEURO_28_SPECIFY} contains 5",
        "title": "Other abnormal gait",
        "Export Column Name": "Abn_Gait_Yes_Other",
        "Export Column Order": 250,
        "Pii flag": true,
        "IsNotAnalyze-Able?": true,
        "IsNotPull-ForwardEligible": true,
        "Analyze Question Group/Name": "Walking"
       }
      ]
     }
    ],
    "triggers": [
     {
      "type": "setvalue",
      "expression": "{NEURO_20_SPECIFY} contains 999",
      "setToName": "NEURO_20_SPECIFY",
      "setValue": [
       "999"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{NEURO_21_SPECIFY} contains 999",
      "setToName": "NEURO_21_SPECIFY",
      "setValue": [
       "999"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{NEURO_24_SPECIFY} contains 999",
      "setToName": "NEURO_24_SPECIFY",
      "setValue": [
       "999"
      ]
     },
     {
      "type": "setvalue",
      "expression": "{NEURO_28_SPECIFY} contains 999",
      "setToName": "NEURO_28_SPECIFY",
      "setValue": [
       "999"
      ]
     }
    ],
    "showQuestionNumbers": "off",
    "clearInvisibleValues": "onHidden"
   }
'''

# List of words to find
word_list = ["NEURO_1","NEURO_2","NEURO_3","NEURO_4","NEURO_5","NEURO_6","NEURO_7","NEURO_8","NEURO_9","NEURO_10_SPECIFY","NEURO_11","NEURO_11_SPECIFY","NEURO_12","NEURO_12_SPECIFY","NEURO_13","NEURO_13_SPECIFY","NEURO_14","NEURO_14_SPECIFY","NEURO_15","NEURO_15_SPECIFY","NEURO_16","NEURO_16_SPECIFY","NEURO_17","NEURO_17_SPECIFY","NEURO_18","NEURO_18_SPECIFY","NEURO_19_PAR","NEURO_19_INDIV","NEURO_19_SPECIFY","NEURO_20","NEURO_20_SPECIFY","NEURO_21","NEURO_21_SPECIFY","NEURO_21_OTHER","NEURO_22","NEURO_22_SPECIFY","NEURO_23","NEURO_23_SPECIFY","NEURO_24","NEURO_24_SPECIFY","NEURO_24_OTHER","NEURO_25","NEURO_25_SPECIFY","NEURO_26","NEURO_26_SPECIFY","NEURO_27","NEURO_27_SPECIFY","NEURO_28","NEURO_28_SPECIFY","NEURO_28_OTHER"]

# Find words in the string
found_words = find_words_in_string(input_string, word_list)
found_count = len(found_words)
word_list_count = len(word_list)

# Print the result
print(f"Words found in the JSON data: {found_count}/{word_list_count} in \n\n {found_words}\n\n{word_list}")