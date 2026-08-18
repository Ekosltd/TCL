"""
Demo/sample data for presentations. Local-only — never merged into main.
Inputs and additionality answers based on the Ayr scenario workbook.
"""

DEMO_DEVELOPMENT_MIX = {
    "Detached (3–5 bed)": {
        "Private Homes": 10, "Social/Affordable Homes": 5,
        "Private Floor Area per unit (m2)": 0, "Social Floor Area per unit (m2)": 0,
    },
    "Semi-detached / Terrace": {
        "Private Homes": 15, "Social/Affordable Homes": 10,
        "Private Floor Area per unit (m2)": 0, "Social Floor Area per unit (m2)": 0,
    },
    "Low-rise flats (2–4 storey)": {
        "Private Homes": 30, "Social/Affordable Homes": 20,
        "Private Floor Area per unit (m2)": 0, "Social Floor Area per unit (m2)": 0,
    },
    "Higher density flats (5 plus storeys)": {
        "Private Homes": 30, "Social/Affordable Homes": 20,
        "Private Floor Area per unit (m2)": 0, "Social Floor Area per unit (m2)": 0,
    },
    "Older Persons / Specialist": {
        "Private Homes": 10, "Social/Affordable Homes": 5,
        "Private Floor Area per unit (m2)": 0, "Social Floor Area per unit (m2)": 0,
    },
}

DEMO_PLACE_SCENARIO_CONTROLS = {
    "By comparison to other town centres across Scotland, please rate the existing level of active travel /public transport accessibility and infrastructure in the vicinity of the proposed site": "Average",
    "How would you rate the level of poverty and deprivation in your town centre compared to the national average": "Slightly higher",
    "Within the town centre, is there access to good quality 'social infrastructure' and open green/blue spaces for residents to interact": "Some access",
    "To what extent is there good quality and accessible opportunities for local people to spend money in the town centre consider ": "Some offer",
    "Please estimate the likely level of embodied carbon savings to be targeted within the proposed development": "Medium",
    "Please select the type of development being proposed - retrofit or new build": "Mix of retrofit and new build ",
    "Will the town centre living development remove or address Brownfield or gap site(s)": "Moderate/visible",
    "Will the town centre living development remove or address vacant unit(s)": "Multiple units/frontage restored",
}

DEMO_PLACE_SCENARIO_USER_INPUTS = {
    "How many people live within 250m - 500m of the proposed development": 1200,
    "Estimate the capital costs of the town centre living development": 15000000,
    "% of households in new TCL development with 1+ car": 0.55,
}

DEMO_CRIME_INPUTS = {
    "Town Centre Population": 3000,
    "Violence": {"Recorded Incidents": None},
    "Theft": {"Recorded Incidents": None},
    "Criminal damage": {"Recorded Incidents": None},
    "ASB": {"Recorded Incidents": None},
}

DEMO_LAND_INFRA_INPUTS = {
    "Are you able to provide details on the GDV and existing land value": "Yes",
    "Total Gross Development Value (GDV) £": 22000000,
    "Existing use / baseline land value (£)": 2500000,
}

DEMO_COMMERCIAL_FLOORSPACE_INPUTS = {
    "Retail and Town Centre Services": 800,
    "Food and Beverage / Hospitality": 400,
    "Office / Workspace": 600,
    "Community and Civic Uses": 300,
    "Leisure, Culture and Visitor Economy": 200,
}

DEMO_ADDITIONALITY_QUESTIONS = {
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
}