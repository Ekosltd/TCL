"""
Explanatory Notes
"""

################################################################################

# From Input Sheet 

#################################################################################

PLACE_SCENARIO_NOTES = {
    "By comparison to other town centres across Scotland, please rate the existing level of active travel /public transport accessibility and infrastructure in the vicinity of the proposed site":
        "You may wish to consider proximity to (and quality of) walking, wheeling, and cycling routes, bus services, and rail station(s)",
    "How would you rate the level of poverty and deprivation in your town centre compared to the national average":
        "If appropriate, please refer to the SIMD for guidance (https://simd.scot/)",
    "Within the town centre, is there access to good quality 'social infrastructure' and open green/blue spaces for residents to interact":
        "Also consider if the proposed development will include civic and/or other space (e.g. greenspace)",
    "To what extent is there good quality and accessible opportunities for local people to spend money in the town centre consider ":
        "Consider food and drink, retail, entertainment, and leisure, etc",
    "Please estimate the likely level of embodied carbon savings to be targeted within the proposed development":
        "Low = Proposals seek to achieve Net Zero Carbon Building Standard. "
        "Medium = Average carbon savings employed." 
        "High = Minimal carbon savings employed."
}

PLACE_SCENARIO_USER_INPUT_NOTES = {
    "How many people live within 250m - 500m of the proposed development":
        "Not including the new residents of the homes, how many people who reside in close "
        "proximity are likely to experience a benefit from enhancing the environmental quality "
        "of the town centre",
    "Estimate the capital costs of the town centre living development":
        "Consider the construction, professional and associated fees of completing the proposed "
        "town centre development"
}

CRIME_NOTES = {
    "Recorded Incidents":
        "Data is also available from Police Scotland: "
        "https://www.scotland.police.uk/about-us/how-we-do-it/crime-data/",
    "Town Centre Population":
        "If recorded incidents is unknown, enter the town centre population instead and "
        "national average incidents per capita will be used",
    "Violence": "Uses Police Scotland Category (1): Non-sexual crimes of violence",
    "Theft": "Uses Police Scotland Category (3): Crimes of Dishonesty",
    "Criminal damage": "Uses Police Scotland Category (4): Damage and Reckless Behaviour",
    "ASB": "Uses Police Scotland Categories (6 & 7): Anti-Social Behaviour & Miscellaneous Offences"
}

LAND_INFRA_NOTES = {
    "Are you able to provide details on the GDV and existing land value":
        "Land value uplift calculations require GDV, development cost and baseline land value. "
        "If incomplete data is provided the indicator will not calculate.",
    "Total Gross Development Value (GDV) £":
        "For private sector homes: number of units by typology multiplied by market value (open "
        "market sale price). For social/affordable homes, use the RSL transfer value, or use the "
        "private calculation and discount the market value: Social rent 50%, MMR/other affordable 75%.",
    "Existing use / baseline land value (£)":
        "Refer to local plans and the District Valuer for guidance if necessary"
}

################################################################################

# From Additionality Questions Sheet

#################################################################################



ADDITIONALITY_NOTES = {
    "Construction_Deadweight":
        "If the TCL development is funded entirely by the private sector, select "
        "'No activity would occur'"
}
