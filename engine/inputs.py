"""
Model Inputs

"""

from load_assumptions import load_assumptions 

#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

###  DEVELOPMENT MIX - entry are typology  ###

development_mix = {
    "Detached (3–5 bed)": {
        "Private Homes": 0,
        "Social/Affordable Homes": 0,
        "Private Floor Area per unit (m2)": 0,
        "Social Floor Area per unit (m2)": 0
    },
    "Semi-detached / Terrace": {
        "Private Homes": 0,
        "Social/Affordable Homes": 0,
        "Private Floor Area per unit (m2)": 0,
        "Social Floor Area per unit (m2)": 0
    },
    "Low-rise flats (2–4 storey)": {
        "Private Homes": 0,
        "Social/Affordable Homes": 0,
        "Private Floor Area per unit (m2)": 0,
        "Social Floor Area per unit (m2)": 0
    },
    "Higher density flats (5 plus storeys)": {
        "Private Homes": 0,
        "Social/Affordable Homes": 0,
        "Private Floor Area per unit (m2)": 0,
        "Social Floor Area per unit (m2)": 0
    },
    "Older Persons / Specialist": {
        "Private Homes": 0,
        "Social/Affordable Homes": 0,
        "Private Floor Area per unit (m2)": 0,
        "Social Floor Area per unit (m2)": 0
    }
}

### none values are derived from assumptions

def get_floorspace(typology: str, tenure: str, development_mix: dict, assumptions: dict) -> float:
    override_key = f"{tenure.capitalize()} Floor Area per unit (m2)"
    override = development_mix[typology][override_key]

    if override is not None and override > 0:
        return override

    # Falls back to the assumptions default --> looked up by typology NAME
    return assumptions["dwellingbytypology"].loc[typology, "Floorspace m2"]


#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

### PLACE AND SCENARIO CONTROLS

### PLACE AND SCENARIO CONTROLS - dropdown selections in streamlit so we have the options and then the controls the selection  ###

place_scenario_options = {
    "By comparison to other town centres across Scotland, please rate the existing level of active travel /public transport accessibility and infrastructure in the vicinity of the proposed site": ["Good", "Average", "Limited / Poor"],
    "How would you rate the level of poverty and deprivation in your town centre compared to the national average": ["Much higher", "Slightly higher", "About the same", "Slightly lower", "Much lower"],
    "Within the town centre, is there access to good quality 'social infrastructure' and open green/blue spaces for residents to interact": ["Yes - good access", "Some access", "Limited access"],
    "To what extent is there good quality and accessible opportunities for local people to spend money in the town centre consider ": ["Strong offer", "Some offer", "Limited offer"],
    "Please estimate the likely level of embodied carbon savings to be targeted within the proposed development": ["Low", "Medium", "High"],
    "Please select the type of development being proposed - retrofit or new build": ["Retrofit development", "New build development", "Mix of retrofit and new build "],
    "Will the town centre living development remove or address Brownfield or gap site(s)": ["Minor/localised", "Moderate/visible", "Major/prominent", "No change / no impact"],
    "Will the town centre living development remove or address vacant unit(s)": ["Isolated vacancy addressed", "Multiple units/frontage restored", "Major block/cluster reactivated", "No change / no impact"],
}

place_scenario_controls = {
    "By comparison to other town centres across Scotland, please rate the existing level of active travel /public transport accessibility and infrastructure in the vicinity of the proposed site": "Average",
    "How would you rate the level of poverty and deprivation in your town centre compared to the national average": "About the same",
    "Within the town centre, is there access to good quality 'social infrastructure' and open green/blue spaces for residents to interact": "Some access",
    "To what extent is there good quality and accessible opportunities for local people to spend money in the town centre consider ": "Some offer",
    "Please estimate the likely level of embodied carbon savings to be targeted within the proposed development": "Medium",
    "Please select the type of development being proposed - retrofit or new build": "Mix of retrofit and new build ",
    "Will the town centre living development remove or address Brownfield or gap site(s)": "Moderate/visible",
    "Will the town centre living development remove or address vacant unit(s)": "No change / no impact",
}

### NMUMERICAL INPUTS 

place_scenario_user_inputs = {
    "How many people live within 250m - 500m of the proposed development": 0,
    "Estimate the capital costs of the town centre living development": 0,
    "% of households in new TCL development with 1+ car": None
}


#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

### CRIME INPUTS    

crime_inputs = {
    "Town Centre Population": None, 
    "Violence": {"Recorded Incidents": None},
    "Theft": {"Recorded Incidents": None},
    "Criminal damage": {"Recorded Incidents": None},
    "ASB": {"Recorded Incidents": None}
}

#for yes or no column
def use_incidents_if_provided(recorded_incidents) -> str:
    if recorded_incidents is not None and recorded_incidents > 0:
        return "Yes"
    return "No"

#to use the town centre population instead of the recorded incidents if the recorded incidents are not provided
def get_incidents_used(category: str, crime_inputs: dict, assumptions: dict) -> float:
    recorded = crime_inputs[category]["Recorded Incidents"]

    if recorded is not None and recorded > 0:
        return recorded

    population = crime_inputs["Town Centre Population"]
    if population is None:
        return 0.0

    rate_per_1000 = assumptions["crime"].loc[category, "Rate per 1,000"]
    return (population / 1000) * rate_per_1000


#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

### LAND AND INFRASTRUCTURE INPUTS


land_infra_options = {
    "Are you able to provide details on the GDV and existing land value": ["Yes", "No "],
}

land_infra_inputs = {
    "Are you able to provide details on the GDV and existing land value": "No ",
    "Total Gross Development Value (GDV) £": None,
    "Existing use / baseline land value (£)": None
}

#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

### COMMERCIAL FLOORSPACE INPUTS 

commercial_floorspace_inputs = {
    "Retail and Town Centre Services":0,
    "Food and Beverage / Hospitality":0,
    "Office / Workspace": 0,
    "Community and Civic Uses": 0,
    "Leisure, Culture and Visitor Economy": 0
}