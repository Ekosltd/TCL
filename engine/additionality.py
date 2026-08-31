"""
Additionality Questions

"""

### ADDITIONALITY QUESTIONS###

additionality_questions = {
    "Environmental": {
        "Deadweight": {
            "question": "To what extent would reductions in emissions and improvements in environmental quality happen anyway without the proposed TCL development?",
            "options": ["High likelihood", "Moderate likelihood", "Low likelihood"],
            "answer": "Low likelihood",
        },
        "Displacement": {
            "question": "Could environmental improvements in this town centre lead to environmental problems or reduced environmental quality elsewhere?",
            "options": ["Yes – notably", "Yes – slightly", "No / negligible"],
            "answer": "No / negligible",
        },
        "Leakage": {
            "question": "Will the environmental benefits mainly benefit the local area, or will a significant proportion occur outside the local authority area?",
            "options": ["Mostly local", "Mixed", "Mostly external"],
            "answer": "Mixed",
        },
    },
    "Social": {
        "Deadweight": {
            "question": "To what extent would residents experience these wellbeing, accessibility and community benefits without the TCL development?",
            "options": ["Already occurring", "Some improvement expected", "Little/no improvement without project"],
            "answer": "Little/no improvement without project",
        },
        "Displacement": {
            "question": "Could the TCL development shift community activity, participation or local spending away from nearby areas rather than creating new benefits overall?",
            "options": ["Yes – notably", "Yes – slightly", "No/unlikely to have any notable effect"],
            "answer": "No/unlikely to have any notable effect",
        },
        "Leakage": {
            "question": "Will the social and wellbeing benefits mainly benefit local residents, or will a significant proportion benefit people outside the area?",
            "options": ["Mostly local", "Mixed", "Mostly external"],
            "answer": "Mostly local",
        },
    },
    "Crime": {
        "Deadweight": {
            "question": "Are reductions already occurring due to wider trends or policing?",
            "options": ["Already occurring", "Some reductions occurring", "Little/no change"],
            "answer": "Little/no change",
        },
        "Displacement": {
            "question": "Could reductions in crime in town centre lead to crime being displaced to nearby areas rather than reduced overal",
            "options": ["Yes – notably", "Yes – slightly", "No/unlikely to have any notable effect"],
            "answer": "Yes – slightly",
        },
        "Leakage": {
            "question": "Will the benefits from reduced crime mainly be experienced locally, or more widely across surrounding areas?",
            "options": ["Mostly local", "Mixed", "Mostly external"],
            "answer": "Mixed",
        },
    },
    "Economic": {
        "Deadweight": {
            "question": "To what extent would this town centre spending happen anyway without the TCL development?",
            "options": ["Yes, most of it", "Yes, some of it", "No, limited spend would occur"],
            "answer": "Yes, most of it",
        },
        "Displacement": {
            "question": "To what extent could increased spending in this town centre reduce spending in nearby centres or retail locations?",
            "options": ["Yes – notably", "Yes – slightly", "No/unlikely to have any notable effect"],
            "answer": "Yes – slightly",
        },
    },
    "Construction": {
        "Deadweight": {
            "question": "Would the development proceed without public sector support or intervention?",
            "options": ["Yes, most of it", "Yes, some of it", "No, limited activity would occur", "No activity would occur"],
            "answer": "No activity would occur",
        },
        "Displacement": {
            "question": "Will this draw construction labour / resources from other local projects?",
            "options": ["Yes – notably", "Yes – slightly", "No/unlikely to have any notable effect"],
            "answer": "No/unlikely to have any notable effect",
        },
        "Leakage": {
            "question": "How much of the construction spend is likely to be captured locally rather than outside the local authority?",
            "options": ["Mostly local", "Mixed", "Mostly external"],
            "answer": "Mixed",
        },
    },
    "Fiscal": {
        "Deadweight": {
            "question": "Would this development, and the associated public revenues (Council Tax and/or rental returns), occur elsewhere within the local authority area?",
            "options": ["Yes, most of it", "Yes, some of it", "No, limited activity would occur", "No activity would occur"],
            "answer": "Yes, some of it",
        },
        "Displacement": {
            "question": "From where do you anticipate that the residents that occupy the new homes will come from? ",
            "options": ["Most residents would otherwise locate within the same authority area", "Some in-migration, but also relocation within the authority", "Majority of residents are additional to the area"],
            "answer": "Some in-migration, but also relocation within the authority",
        },
    },
    "Land": {
        "Deadweight": {
            "question": "To what extent would increases in land and property values happen anyway without the TCL development?",
            "options": ["Yes, most of it", "Yes, some of it", "No, limited activity would occur", "No activity would occur"],
            "answer": "No, limited activity would occur",
        },
        "Displacement": {
            "question": "Does the development shift land value uplift from other sites or locations?",
            "options": ["Yes – notably", "Yes – slightly", "No/unlikely to have any notable effect"],
            "answer": "No/unlikely to have any notable effect",
        },
    },
    "Commercial":{
        "Deadweight":{
            "question": "What is most likely to have happened to the proposed commercial floorspace in the absence of the Town Centre Living intervention?",
            "options":[
                "The floorspace would be unlikely to be developed/brought back into productive use without the intervention",
                "Development/use may have occurred, but at a substantially smaller scale or after a significant delay",
                "A significant proportion of the development/use would probably have occurred anyway"
            ],
            "answer":"The floorspace would be unlikely to be developed/brought back into productive use without the intervention"
        },
        "Displacement":{
            "question":"To what extent is the commercial activity expected to occupy the floorspace likely to relocate from, or compete directly with, existing businesses elsewhere within the town centre?",
            "options":[
                "Significant competition with existing local businesses or potential relocation from elsewhere within the area",
                "Some competition with existing businesses, but a substantial proportion of activity is expected to be additional",
                "Limited local competition / predominantly new activity or activity serving new or unmet demand"
            ],
            "answer":"Limited local competition / predominantly new activity or activity serving new or unmet demand"
        },
    }
}
