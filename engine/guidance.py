"""
Guidance content shown to the user before they start entering inputs.
"""

GUIDANCE_TITLE = "How the Model Works"

GUIDANCE_INTRO = """
This tool estimates the social, economic, environmental and fiscal impact of a proposed Town Centre Living (TCL) development. You'll work through six input sections, then the model calculates a full Impact Dashboard plus more detailed results of the 14 indicators.
"""

INPUT_SECTIONS = [
    {
        "title": "1. Development Mix",
        "what_you_need": [
            "Number of private and social/affordable homes, by typology:\n"
            "  - Detached (3–5 bed)\n"
            "  - Semi-detached / Terrace\n"
            "  - Low-rise flats (2–4 storey)\n"
            "  - Higher density flats (5 plus storeys)\n"
            "  - Older Persons / Specialist",
            "Optional: floor area per unit (private and social) for each typology. "
            "Leave at 0 to use the assumptions default.",
        ],
        "why": "This is the foundation for: resident population, "
               "total floorspace (GIA), embodied carbon, and most economic and fiscal indicators ",
    },
    {
        "title": "2. Place & Scenario",
        "what_you_need": [
            "Multiple choice site-level questions: active travel/public transport "
            "accessibility, deprivation level, access to social infrastructure and green/blue space, "
            "local spending offer, embodied carbon target, retrofit vs new build, and whether the "
            "development addresses brownfield/gap sites or vacant units.",
            "Numerical inputs include: how many people live within 250–500m of the proposed site and "
            "the estimated total capital cost of the development.",
            "Optional: % of households with 1+ car, leave blank to estimate from the development mix.",
        ],
        "why": "These answers drive transport "
               "emissions, health & wellbeing, civic engagement, environmental quality, and "
               "construction activity.",
    },
    {
        "title": "3. Crime",
        "what_you_need": [
            "Recorded incidents for Violence, Theft, Criminal Damage and ASB, if known.",
            "Otherwise: the town centre population, which is used to estimate incidents from national rates.",
        ],
        "why": "Feeds the Cost of Crime indicator.",
    },
    {
        "title": "4. Land & Infrastructure",
        "what_you_need": [
            "Whether you're able to provide Gross Development Value (GDV) and existing/baseline land value.",
            "If yes: the GDV and the existing use / baseline land value, in £.",
        ],
        "why": "Optional. Feeds the Land Values indicator only. If you answer 'No', or leave the "
               "figures blank, that indicator will show as 'N/A' rather than being estimated.",
    },
    {
        "title": "5. Commercial Floorspace",
        "what_you_need": [
            "Any planned non-residential floorspace, in m², by use type: Retail and Town Centre "
            "Services, Food and Beverage/Hospitality, Office/Workspace, Community and Civic Uses, "
            "Leisure/Culture/Visitor Economy.",
        ],
        "why": "Optional. Feeds the Commercial Floorspace indicator.",
    },
    {
        "title": "6. Additionality Questions",
        "what_you_need": [
            "Multiple choice questions across seven impact areas: Environmental, Social, Crime, "
            "Economic, Construction, Fiscal, Land. The answers are used to work out deadweight, "
            "displacement and leakage.",
        ],
        "extra": {
            "heading": "What are additionality factors?",
            "items": [
                "Deadweight: how much would happen anyway without the project?",
                "Displacement: does the project move activity or benefits from somewhere else?",
                "Leakage: do benefits flow outside the local area?",
                "Multiplier: wider supply chain and spending effects that create additional "
                "economic activity. These are calculated automatically, no input needed.",
            ],
        },
        "why": "This works out how much of the modelled impact is genuinely additional, meaning it "
               "wouldn't have happened anyway. This is the final section: once you've answered "
               "these, the Show Results button appears.",
    },
]


GUIDANCE_NOTE = """
<b>Please work through the sections in order, 1 to 6.</b> The <b>Show Results</b> button only appears once you reach the final section, 
Additionality Questions.
"""

GUIDANCE_RESULTS_INTRO = """
Once you've completed all six sections, the model produces an **Impact Dashboard** which is a summary of 
the overall value, followed by 14 **detailed indicator impacts**.
"""

RESULTS_SECTIONS = [
    {
        "title": "Net Additional Social Value",
        "description": "The headline social value: annual, 10-year NPV, and value per home. "
                        "Includes a ±10% sensitivity range and a breakdown of which impact areas "
                        "(health, environment, civic engagement, etc.) make up the annual total.",
    },
    {
        "title": "Core Development Outputs",
        "description": "The underlying numbers everything else is built from: total units, total "
                        "residents, working-age adults, employed adults, and FTE jobs.",
    },
    {
        "title": "Net Additional Economic and Fiscal Value",
        "description": "Economic and fiscal value: spend, jobs, GVA, council tax and rental "
                        "returns. Annually and as a 10-year NPV, with the same ±10% sensitivity range.",
    },
    {
        "title": "One-off Construction Impacts",
        "description": "Construction-phase jobs and GVA, shown separately as they're one-off "
                        "rather than recurring annual value.",
    },
    {
        "title": "Commercial Floorspace Impacts",
        "description": "If you entered commercial floorspace, its jobs and GVA impact",
    },
    {
        "title": "Detailed Impacts",
        "description": "All 14 indicators, each in its own expandable section, showing the gross value, the deadweight/displacement/leakage factors "
                        "applied, and the resulting net additional value.",
        "extra": {
            "heading": "Every indicator follows the same pattern",
            "items": [
                "Gross value: the impact before adjusting for additionality",
                "Deadweight, Displacement, Leakage (and Multiplier, where relevant): the "
                "additionality factors applied",
                "Net additional value: the final, additionality-adjusted figure which is what "
                "feeds into the dashboard totals above",
            ],
        },
    },
]