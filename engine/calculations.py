"""
Formulas for calculations used in the dashboard. These are used to calculate the outputs based on the inputs and assumptions provided by the user.
"""

from additionality import additionality_questions

from inputs import development_mix, get_floorspace, place_scenario_controls, place_scenario_user_inputs, crime_inputs, land_infra_inputs, get_incidents_used, commercial_floorspace_inputs

from load_assumptions import load_assumptions 

#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

#################################################################################################################################################################################################################
### ADDITIONALITY SUMMARY
#################################################################################################################################################################################################################


def additionality_environmental(additionality_questions: dict) -> dict:

    # --- Deadweight ---
    deadweight_answer = additionality_questions["Environmental"]["Deadweight"]["answer"]
    # convert that answer text into its numeric value
    deadweight_values = {"High likelihood": 0.5, "Moderate likelihood": 0.3, "Low likelihood": 0.1}
    deadweight = deadweight_values[deadweight_answer]

    # --- Displacement ---
    displacement_answer = additionality_questions["Environmental"]["Displacement"]["answer"]
    displacement_values = {"Yes – notably": 0.15, "Yes – slightly": 0.075, "No / negligible": 0.025}
    displacement = displacement_values[displacement_answer]

    # --- Leakage ---
    leakage_answer = additionality_questions["Environmental"]["Leakage"]["answer"]
    leakage_values = {"Mostly local": 0.025, "Mixed": 0.075, "Mostly external": 0.15}
    leakage = leakage_values[leakage_answer]

    # --- Multiplier ---
    #fixed at 1
    multiplier = 1.0

    return {
        "Deadweight": deadweight,
        "Displacement": displacement,
        "Leakage": leakage,
        "Multiplier": multiplier,
    }

def additionality_social(additionality_questions: dict) -> dict:

    # --- Deadweight ---
    deadweight_answer = additionality_questions["Social"]["Deadweight"]["answer"]
    # convert that answer text into its numeric value
    deadweight_values = {"Already occurring": 0.5, "Some improvement expected": 0.3,  "Little/no improvement without project": 0.1}
    deadweight = deadweight_values[deadweight_answer]

    # --- Displacement ---
    displacement_answer = additionality_questions["Social"]["Displacement"]["answer"]
    displacement_values = {"Yes – notably": 0.15, "Yes – slightly": 0.075, "No/unlikely to have any notable effect": 0.025}
    displacement = displacement_values[displacement_answer]

    # --- Leakage ---
    leakage_answer = additionality_questions["Social"]["Leakage"]["answer"]
    leakage_values = {"Mostly local": 0.025, "Mixed": 0.075, "Mostly external": 0.15}
    leakage = leakage_values[leakage_answer]

    # --- Multiplier ---
    #fixed at 1
    multiplier = 1.0

    return {
        "Deadweight": deadweight,
        "Displacement": displacement,
        "Leakage": leakage,
        "Multiplier": multiplier,
    }

def additionality_crime(additionality_questions: dict) -> dict:

    # --- Deadweight ---
    deadweight_answer = additionality_questions["Crime"]["Deadweight"]["answer"]
    # convert that answer text into its numeric value
    deadweight_values = {"Already occurring": 0.5, "Some reductions occurring": 0.3, "Little/no change": 0.1}
    deadweight = deadweight_values[deadweight_answer]

    # --- Displacement ---
    displacement_answer = additionality_questions["Crime"]["Displacement"]["answer"]
    displacement_values = {"Yes – notably": 0.15, "Yes – slightly": 0.075, "No/unlikely to have any notable effect": 0.025}
    displacement = displacement_values[displacement_answer]

    # --- Leakage ---
    leakage_answer = additionality_questions["Crime"]["Leakage"]["answer"]
    leakage_values = {"Mostly local": 0.025, "Mixed": 0.075, "Mostly external": 0.15}
    leakage = leakage_values[leakage_answer]

    # --- Multiplier ---
    #fixed at 1
    multiplier = 1.0

    return {
        "Deadweight": deadweight,
        "Displacement": displacement,
        "Leakage": leakage,
        "Multiplier": multiplier,
    }

def additionality_economic(additionality_questions: dict, assumptions: dict) -> dict:

    # --- Deadweight ---
    deadweight_answer = additionality_questions["Economic"]["Deadweight"]["answer"]
    # convert that answer text into its numeric value
    deadweight_values = {"Yes, most of it": 0.6,  "Yes, some of it": 0.4, "No, limited spend would occur": 0.15}
    deadweight = deadweight_values[deadweight_answer]

    # --- Displacement ---
    displacement_answer = additionality_questions["Economic"]["Displacement"]["answer"]
    displacement_values = {"Yes – notably": 0.55, "Yes – slightly": 0.3, "No/unlikely to have any notable effect": 0.1}
    displacement = displacement_values[displacement_answer]

    # --- Multiplier ---
    #from assumptions
    multiplier = float(assumptions["land_infra_mult"].loc["Economic impacts multiplier", "Value"])

    return {
        "Deadweight": deadweight,
        "Displacement": displacement,
        "Multiplier": multiplier,
    }

def additionality_construction (additionality_questions: dict, assumptions: dict) -> dict:

    # --- Deadweight ---
    deadweight_answer = additionality_questions["Construction"]["Deadweight"]["answer"]
    # convert that answer text into its numeric value
    deadweight_values = {"Yes, most of it": 0.6,  "Yes, some of it": 0.4, "No, limited activity would occur": 0.15, "No activity would occur": 0.0}
    deadweight = deadweight_values[deadweight_answer]

    # --- Displacement ---
    displacement_answer = additionality_questions["Construction"]["Displacement"]["answer"]
    displacement_values = {"Yes – notably": 0.4, "Yes – slightly": 0.25, "No/unlikely to have any notable effect": 0.1}
    displacement = displacement_values[displacement_answer]

    # --- Leakage ---
    leakage_answer = additionality_questions["Construction"]["Leakage"]["answer"]
    leakage_values = {"Mostly local": 0.15, "Mixed": 0.4, "Mostly external": 0.6}
    leakage = leakage_values[leakage_answer]
    
    # --- Multiplier ---
    #from assumptions
    multiplier = float(assumptions["land_infra_mult"].loc["Construction impacts multiplier", "Value"])

    return {
        "Deadweight": deadweight,
        "Displacement": displacement,
        "Leakage": leakage,
        "Multiplier": multiplier,
    }

def additionality_fiscal (additionality_questions: dict) -> dict:

    # --- Deadweight ---
    deadweight_answer = additionality_questions["Fiscal"]["Deadweight"]["answer"]
    # convert that answer text into its numeric value
    deadweight_values = {"Yes, most of it": 0.625,  "Yes, some of it": 0.4, "No, limited activity would occur": 0.15, "No activity would occur": 0.0}
    deadweight = deadweight_values[deadweight_answer]

    # --- Displacement ---
    displacement_answer = additionality_questions["Fiscal"]["Displacement"]["answer"]
    displacement_values = {"Most residents would otherwise locate within the same authority area": 0.55, "Some in-migration, but also relocation within the authority": 0.3, "Majority of residents are additional to the area": 0.1}
    displacement = displacement_values[displacement_answer]
    
    # --- Multiplier ---
    #fixed at 1
    multiplier = 1.0

    return {
        "Deadweight": deadweight,
        "Displacement": displacement,
        "Multiplier": multiplier,
    }

def additionality_land(additionality_questions: dict) -> dict:

    # --- Deadweight ---
    deadweight_answer = additionality_questions["Land"]["Deadweight"]["answer"]
    # convert that answer text into its numeric value
    deadweight_values = {"Yes, most of it": 0.6,  "Yes, some of it": 0.4, "No, limited activity would occur": 0.15, "No activity would occur": 0.0}
    deadweight = deadweight_values[deadweight_answer]

    # --- Displacement ---
    displacement_answer = additionality_questions["Land"]["Displacement"]["answer"]
    displacement_values = {"Yes – notably": 0.4, "Yes – slightly": 0.25, "No/unlikely to have any notable effect": 0.1}
    displacement = displacement_values[displacement_answer]
    
    # --- Multiplier ---
    #fixed at 1
    multiplier = 1.0

    return {
        "Deadweight": deadweight,
        "Displacement": displacement,
        "Multiplier": multiplier,
    }

def additionality_commercial(additionality_questions: dict, assumptions: dict) -> dict:

    # --- Deadweight ---
    deadweight_answer = additionality_questions["Commercial"]["Deadweight"]["answer"]
    deadweight_values = {
        "The floorspace would be unlikely to be developed/brought back into productive use without the intervention": 0.15,
        "Development/use may have occurred, but at a substantially smaller scale or after a significant delay": 0.25,
        "A significant proportion of the development/use would probably have occurred anyway": 0.4,
    }
    deadweight = deadweight_values[deadweight_answer]

    # --- Displacement ---
    displacement_answer = additionality_questions["Commercial"]["Displacement"]["answer"]
    displacement_values = {
        "Limited local competition / predominantly new activity or activity serving new or unmet demand": 0.1,
        "Some competition with existing businesses, but a substantial proportion of activity is expected to be additional": 0.2,
        "Significant competition with existing local businesses or potential relocation from elsewhere within the area": 0.35,
    }
    displacement = displacement_values[displacement_answer]

    # --- Multiplier ---
    # Reuses the same fixed Economic impacts multiplier (matches Excel: Assumptions!E157 = $B$130)
    multiplier = float(assumptions["land_infra_mult"].loc["Economic impacts multiplier", "Value"])

    return {
        "Deadweight": deadweight,
        "Displacement": displacement,
        "Multiplier": multiplier,
    }

#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################


#################################################################################################################################################################################################################
### 4. RESIDENT POPULATION
#################################################################################################################################################################################################################

def population_by_typology(development_mix: dict, assumptions: dict) -> dict:
    result = {}
    total_private = 0.0
    total_social = 0.0

    for typology, values in development_mix.items():
        private_homes = values["Private Homes"]
        social_homes = values["Social/Affordable Homes"]

        private_persons_per_dwelling = float(assumptions["dwellingbytypology"].loc[typology, "Persons Per Dwelling - Private"])
        social_persons_per_dwelling = float(assumptions["dwellingbytypology"].loc[typology, "Persons Per Dwelling - Social/affordable"])

        private_residents = private_homes * private_persons_per_dwelling
        social_residents = social_homes * social_persons_per_dwelling

        result[typology] = {
            "Private residents": private_residents,
            "Social residents": social_residents,
            "Total residents": private_residents + social_residents,
        }

        total_private += private_residents
        total_social += social_residents

    result["Total"] = {
        "Private residents": total_private,
        "Social residents": total_social,
        "Total residents": round(total_private + total_social),
    }

    return result


def demographic_employment_outputs(development_mix: dict, assumptions: dict) -> dict:
    population = population_by_typology(development_mix, assumptions)
    pop_employ = assumptions["pop_employ"]

    older_typology = "Older Persons / Specialist"
    total_older = population[older_typology]["Total residents"]

    # Everyone NOT in the Older Persons typology still uses Private/Social split
    total_private_other = sum(
        values["Private residents"] for typology, values in population.items()
        if typology not in ("Total", older_typology)
    )
    total_social_other = sum(
        values["Social residents"] for typology, values in population.items()
        if typology not in ("Total", older_typology)
    )

    children = round(
        total_private_other * pop_employ.loc["Children share", "Private"]
        + total_social_other * pop_employ.loc["Children share", "Social/affordable"]
        + total_older * pop_employ.loc["Children share", "Older person"]
    )

    working_age_other = (
        total_private_other * pop_employ.loc["Working age share", "Private"]
        + total_social_other * pop_employ.loc["Working age share", "Social/affordable"]
    )
    working_age_older = total_older * pop_employ.loc["Working age share", "Older person"]
    working_age = round(working_age_other + working_age_older)

    older_adults = round(
        total_private_other * pop_employ.loc["65+ share", "Private"]
        + total_social_other * pop_employ.loc["65+ share", "Social/affordable"]
        + total_older * pop_employ.loc["65+ share", "Older person"]
    )

    # Uses the AVERAGE of private/social employment rates for everyone else (matches original B17),
    # but the Older person rate for the Older Persons typology
    employed_adults = round(
        working_age_other * (
            (pop_employ.loc["Employment rate", "Private"] + pop_employ.loc["Employment rate", "Social/affordable"])
            / 2
        )
        + working_age_older * pop_employ.loc["Employment rate", "Older person"]
    )

    return {
        "Children": children,
        "Working-age adults": working_age,
        "Older adults": older_adults,
        "Employed adults": employed_adults,
    }
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

#################################################################################################################################################################################################################
### 1. TRANSPORT EMISSIONS
#################################################################################################################################################################################################################

def transport_emissions_mode_calculations(place_scenario_controls: dict, development_mix: dict, assumptions: dict) -> dict:
    transport = assumptions["transport_modal"]
    general = assumptions["general_parameters"]

    accessibility_answer = place_scenario_controls["By comparison to other town centres across Scotland, please rate the existing level of active travel /public transport accessibility and infrastructure in the vicinity of the proposed site"]

    journey_distance_reduction = general.loc["Journey distance reduction", "Value"]
    trips_per_person_per_day = general.loc["Trips per person per day", "Value"]

    population = population_by_typology(development_mix, assumptions)
    total_residents = population["Total"]["Total residents"]

    modes = {}
    gross_savings = 0.0

    for mode in transport.index:
        baseline_share = float(transport.loc[mode, "Baseline share"])
        baseline_km = float(transport.loc[mode, "Baseline km"])
        emission_factor = float(transport.loc[mode, "Emission factor kgCO2e/pkm"])

        if accessibility_answer == "Good":
            tcl_share = float(transport.loc[mode, "TCL Good"])
        elif accessibility_answer == "Average":
            tcl_share = float(transport.loc[mode, "TCL Average"])
        else:
            tcl_share = float(transport.loc[mode, "TCL Limited"])

        tcl_km = baseline_km * (1 - journey_distance_reduction)

        baseline_tco2e = total_residents * trips_per_person_per_day * baseline_share * baseline_km * emission_factor * 365 / 1000
        tcl_tco2e = total_residents * trips_per_person_per_day * tcl_share * tcl_km * emission_factor * 365 / 1000
        savings_tco2e = baseline_tco2e - tcl_tco2e

        modes[mode] = {
            "Baseline share": baseline_share,
            "TCL share": tcl_share,
            "Baseline km": baseline_km,
            "TCL km": tcl_km,
            "Emission factor": emission_factor,
            "Baseline tCO2e": baseline_tco2e,
            "TCL tCO2e": tcl_tco2e,
            "Savings tCO2e": savings_tco2e,
        }

        gross_savings += savings_tco2e

    return {
        "modes": modes,
        "Gross savings": gross_savings,
    }


def transport_emissions_valuation(place_scenario_controls: dict, development_mix: dict, additionality_questions: dict, assumptions: dict) -> dict:
    mode_calcs = transport_emissions_mode_calculations(place_scenario_controls, development_mix, assumptions)
    gross_tco2e = mode_calcs["Gross savings"]

    carbon_value = 100  # £/t- hardcoded in original model
    gross_value = round(gross_tco2e * carbon_value, -3)

    additionality = additionality_environmental(additionality_questions)
    deadweight = additionality["Deadweight"]
    displacement = additionality["Displacement"]
    leakage = additionality["Leakage"]

    net_factor = (1 - deadweight) * (1 - displacement) * (1 - leakage)
    net_tco2e = gross_tco2e * net_factor
    net_value = round(gross_value * net_factor, -3)

    return {
        "Gross tCO2e saved": gross_tco2e,
        "Carbon value (£/t)": carbon_value,
        "Gross £ value": gross_value,
        "Deadweight": deadweight,
        "Displacement": displacement,
        "Leakage": leakage,
        "Net factor": net_factor,
        "Net additional tCO2e saved": net_tco2e,
        "Net additional £ value": net_value,
    }

#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

#################################################################################################################################################################################################################
### 2. EMBODIED CARBON
#################################################################################################################################################################################################################

def get_total_gia(development_mix: dict, assumptions: dict) -> dict:
    total_private_gia = 0.0
    total_social_gia = 0.0

    for typology, values in development_mix.items():
        private_homes = values["Private Homes"]
        social_homes = values["Social/Affordable Homes"]

        private_floorspace = get_floorspace(typology, "private", development_mix, assumptions)
        social_floorspace = get_floorspace(typology, "social", development_mix, assumptions)

        total_private_gia += private_homes * private_floorspace
        total_social_gia += social_homes * social_floorspace

    return {
        "Total private GIA": total_private_gia,
        "Total social GIA": total_social_gia,
        "Total GIA": total_private_gia + total_social_gia,
    }


def embodied_carbon(development_mix: dict, place_scenario_controls: dict, additionality_questions: dict, assumptions: dict) -> dict:
    carbon = assumptions["carbon"]

    embodied_target = place_scenario_controls["Please estimate the likely level of embodied carbon savings to be targeted within the proposed development"]
    development_type = place_scenario_controls["Please select the type of development being proposed - retrofit or new build"]

    gia = get_total_gia(development_mix, assumptions)
    total_gia = gia["Total GIA"]

    # --- Proposed carbon factor: column depends on target (Low/Medium/High), row depends on development type ---
    target_column_map = {"Low": "Low upfront", "Medium": "Medium upfront", "High": "High upfront"}
    proposed_carbon_factor = float(carbon.loc[development_type, target_column_map[embodied_target]])

    # --- Comparator (baseline) carbon factor, from the same development-type row ---
    comparator_carbon_factor = float(carbon.loc[development_type, "Baseline comparator"])

    # --- End of life factor (same for every development type in this sheet) ---
    end_of_life_factor = float(carbon.loc[development_type, "End of life factor"])

    # --- Gross impact ---
    upfront_tco2e = total_gia * (comparator_carbon_factor - proposed_carbon_factor) / 1000
    end_of_life_tco2e = upfront_tco2e * end_of_life_factor
    gross_tco2e = round(upfront_tco2e + end_of_life_tco2e, -2)

    carbon_value = 100  # £/t — hardcoded in original model, same as Transport Emissions
    gross_value = round(gross_tco2e * carbon_value, -3)

    # --- Net additional impact: uses Environmental additionality, same as Transport Emissions ---
    additionality = additionality_environmental(additionality_questions)
    deadweight = additionality["Deadweight"]
    displacement = additionality["Displacement"]
    leakage = additionality["Leakage"]

    net_factor = (1 - deadweight) * (1 - displacement) * (1 - leakage)
    net_tco2e = round(gross_tco2e * net_factor, -2)
    net_value = round(gross_value * net_factor, -3)

    return {
        "Total private GIA": gia["Total private GIA"],
        "Total social GIA": gia["Total social GIA"],
        "Total GIA": total_gia,
        "Proposed carbon factor": proposed_carbon_factor,
        "Comparator carbon factor": comparator_carbon_factor,
        "End of life factor": end_of_life_factor,
        "Upfront tCO2e saved": upfront_tco2e,
        "End of life tCO2e saved": end_of_life_tco2e,
        "Gross tCO2e saved": gross_tco2e,
        "Carbon value (£/t)": carbon_value,
        "Gross £ value": gross_value,
        "Deadweight": deadweight,
        "Displacement": displacement,
        "Leakage": leakage,
        "Net factor": net_factor,
        "Net additional tCO2e saved": net_tco2e,
        "Net additional £ value": net_value,
    }

#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

#################################################################################################################################################################################################################
### 3. ENVIRONMENTAL QUALITY 
#################################################################################################################################################################################################################

def environmental_quality(place_scenario_controls: dict, place_scenario_user_inputs: dict, additionality_questions: dict, assumptions: dict) -> dict:
    general = assumptions["general_parameters"]
    wellbeing = assumptions["environ_wellbeing"]

    population_500m = place_scenario_user_inputs["How many people live within 250m - 500m of the proposed development"]

    # --- Brownfield / gap site impact ---
    brownfield_answer = place_scenario_controls["Will the town centre living development remove or address Brownfield or gap site(s)"]
    if brownfield_answer == "No change / no impact":
        brownfield_impact = 0.0
    elif brownfield_answer == "Minor/localised":
        brownfield_impact = float(wellbeing.loc["Brownfield / gap site LS", "Lower scale impact"])
    elif brownfield_answer == "Moderate/visible":
        brownfield_impact = float(wellbeing.loc["Brownfield / gap site LS", "Central impact"])
    else:  # Major/prominent
        brownfield_impact = float(wellbeing.loc["Brownfield / gap site LS", "Higher scale impact"])

    # --- Vacant units impact ---
    vacant_answer = place_scenario_controls["Will the town centre living development remove or address vacant unit(s)"]
    if vacant_answer == "No change / no impact":
        vacant_impact = 0.0
    elif vacant_answer == "Isolated vacancy addressed":
        vacant_impact = float(wellbeing.loc["Vacant units LS", "Lower scale impact"])
    elif vacant_answer == "Multiple units/frontage restored":
        vacant_impact = float(wellbeing.loc["Vacant units LS", "Central impact"])
    else:  # Major block/cluster reactivated
        vacant_impact = float(wellbeing.loc["Vacant units LS", "Higher scale impact"])

    # --- Heritage impact ---
    heritage_answer = place_scenario_controls["Does the town centre living development include proposals to restore building(s) or a site with heritage designation or significance?"]
    if heritage_answer == "No heritage designation/significance":
        heritage_impact = 0.0
    elif heritage_answer == "Locally significant asset / conservation-area contribution":
        heritage_impact = float(wellbeing.loc["Heritage asset LS", "Lower scale impact"])
    elif heritage_answer == "Listed building / significant conservation asset":
        heritage_impact = float(wellbeing.loc["Heritage asset LS", "Central impact"])
    else:  # Significant town-centre landmark / regionally/nationally significant heritage asset
        heritage_impact = float(wellbeing.loc["Heritage asset LS", "Higher scale impact"])

    life_satisfaction_value = float(general.loc["Life satisfaction value", "Value"])

    # --- Gross impact ---
    gross_annual_value = round(population_500m * (brownfield_impact + vacant_impact + heritage_impact) * life_satisfaction_value, -3)

    # --- Net additional impact: Environmental additionality again ---
    additionality = additionality_environmental(additionality_questions)
    deadweight = additionality["Deadweight"]
    displacement = additionality["Displacement"]
    leakage = additionality["Leakage"]

    net_factor = (1 - deadweight) * (1 - displacement) * (1 - leakage)
    net_annual_value = round(gross_annual_value * net_factor, -3)

    return {
        "Population within 500m": population_500m,
        "Brownfield / gap site impact": brownfield_impact,
        "Vacant units impact": vacant_impact,
        "Heritage impact": heritage_impact,
        "Life satisfaction value": life_satisfaction_value,
        "Gross annual wellbeing value": gross_annual_value,
        "Deadweight": deadweight,
        "Displacement": displacement,
        "Leakage": leakage,
        "Net factor": net_factor,
        "Net additional annual wellbeing value": net_annual_value,
    }
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

#################################################################################################################################################################################################################
### 5. HEALTH & WELLBEING (Physical and Mental Wellbeing)
#################################################################################################################################################################################################################

def health_wellbeing(place_scenario_controls: dict, development_mix: dict, additionality_questions: dict, assumptions: dict) -> dict:
    active_travel = assumptions["active_travel"]
    general = assumptions["general_parameters"]
    wellbeing = assumptions["environ_wellbeing"]

    demographics = demographic_employment_outputs(development_mix, assumptions)
    # Weighted "total residents" specific to this indicator: children 25%, working-age 90%, older adults 75%
    total_residents_weighted = (
        demographics["Children"] * 0.25
        + demographics["Working-age adults"] * 0.9
        + demographics["Older adults"] * 0.75
    )

    accessibility_answer = place_scenario_controls["By comparison to other town centres across Scotland, please rate the existing level of active travel /public transport accessibility and infrastructure in the vicinity of the proposed site"]
    minutes_uplift = float(active_travel.loc[accessibility_answer if accessibility_answer != "Limited / Poor" else "Limited / poor", "Minutes uplift"])

    deprivation_answer = place_scenario_controls["How would you rate the level of poverty and deprivation in your town centre compared to the national average"]
    if deprivation_answer == "Much higher":
        baseline_threshold = float(active_travel.loc["Good", "Baseline meeting 150 mins (high deprivation)"])
    elif deprivation_answer in ("Slightly higher", "About the same"):
        baseline_threshold = float(active_travel.loc["Good", "Baseline meeting 150 mins (average deprivation)"])
    else:  # Slightly lower, Much lower
        baseline_threshold = float(active_travel.loc["Good", "Baseline meeting 150 mins (low deprivation)"])

    share_newly_meeting = min(0.15, (minutes_uplift / 150) * (1 - baseline_threshold))
    residents_newly_meeting = total_residents_weighted * share_newly_meeting
    residents_already_active = total_residents_weighted * baseline_threshold

    qaly_value = float(general.loc["QALY value", "Value"])
    qaly_uplift_newly_active = float(wellbeing.loc["QALY uplift - newly active", "Lower scale impact"])
    qaly_uplift_already_active = float(wellbeing.loc["QALY uplift - already active", "Lower scale impact"])

    gross_annual_value = round(
        residents_newly_meeting * qaly_uplift_newly_active * qaly_value
        + residents_already_active * qaly_uplift_already_active * qaly_value,
        -3
    )


    additionality = additionality_social(additionality_questions)
    deadweight = additionality["Deadweight"]
    displacement = additionality["Displacement"]
    leakage = additionality["Leakage"]

    net_factor = (1 - deadweight) * (1 - displacement) * (1 - leakage)
    net_annual_value = round(gross_annual_value * net_factor, -3)

    return {
        "Total residents (weighted)": total_residents_weighted,
        "Minutes uplift per person/week": minutes_uplift,
        "Baseline already meeting threshold": baseline_threshold,
        "Share newly meeting threshold": share_newly_meeting,
        "Residents newly meeting threshold": residents_newly_meeting,
        "Residents already active": residents_already_active,
        "Gross annual health value": gross_annual_value,
        "Deadweight": deadweight,
        "Displacement": displacement,
        "Leakage": leakage,
        "Net factor": net_factor,
        "Net additional annual health value": net_annual_value,
    }

#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

#################################################################################################################################################################################################################
### 6. CIVIC ENGAGEMENT, PARTICIPATION AND BELONGING
#################################################################################################################################################################################################################

def civic_engagement(place_scenario_controls: dict, development_mix: dict, additionality_questions: dict, assumptions: dict) -> dict:
    general = assumptions["general_parameters"]
    belonging = assumptions["civic_eng_belong"]

    population = population_by_typology(development_mix, assumptions)
    total_residents = population["Total"]["Total residents"]

    deprivation_answer = place_scenario_controls["How would you rate the level of poverty and deprivation in your town centre compared to the national average"]
    deprivation_uplift_map = {
        "Much higher": 0.0125,
        "Slightly higher": 0.025,
        "About the same": 0.025,
        "Slightly lower": 0.025,
        "Much lower": 0.035,
    }
    deprivation_uplift = deprivation_uplift_map[deprivation_answer]

    social_infra_answer = place_scenario_controls["Within the town centre, is there access to good quality 'social infrastructure' and open green/blue spaces for residents to interact"]
    if social_infra_answer == "Yes - good access":
        social_infra_uplift = 0.025
    elif social_infra_answer == "Some access":
        social_infra_uplift = 0.0125
    else:  # Limited access
        social_infra_uplift = 0.00625

    life_satisfaction_value = float(general.loc["Life satisfaction value", "Value"])

    full_impact_share = float(belonging.loc["Belonging - full impact share", "Value"])
    partial_impact_share = float(belonging.loc["Belonging - partial impact share", "Value"])
    partial_impact_weighting = float(belonging.loc["Belonging - partial impact weighting", "Value"])

    effective_beneficiary_weighting = full_impact_share + (partial_impact_share * partial_impact_weighting)

    gross_annual_value = round(
        total_residents * effective_beneficiary_weighting * (deprivation_uplift + social_infra_uplift) * life_satisfaction_value,
        -3
    )

    additionality = additionality_social(additionality_questions)
    deadweight = additionality["Deadweight"]
    displacement = additionality["Displacement"]
    leakage = additionality["Leakage"]

    net_factor = (1 - deadweight) * (1 - displacement) * (1 - leakage)
    net_annual_value = round(gross_annual_value * net_factor, -3)

    return {
        "Total residents": total_residents,
        "Deprivation uplift": deprivation_uplift,
        "Social infrastructure uplift": social_infra_uplift,
        "Effective beneficiary weighting": effective_beneficiary_weighting,
        "Gross annual wellbeing value": gross_annual_value,
        "Deadweight": deadweight,
        "Displacement": displacement,
        "Leakage": leakage,
        "Net factor": net_factor,
        "Net additional annual wellbeing value": net_annual_value,
    }
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

#################################################################################################################################################################################################################
### 7. TRAVEL TIME AND COSTS
#################################################################################################################################################################################################################

def travel_time_and_costs(place_scenario_controls: dict, place_scenario_user_inputs: dict, development_mix: dict, additionality_questions: dict, assumptions: dict) -> dict:
    general = assumptions["general_parameters"]
    pop_employ = assumptions["pop_employ"]

    demographics = demographic_employment_outputs(development_mix, assumptions)
    total_residents_weighted = (
        demographics["Children"] * 0.25
        + demographics["Working-age adults"] * 0.9
        + demographics["Older adults"] * 0.75
    )

    total_private_homes = sum(v["Private Homes"] for v in development_mix.values())
    total_social_homes = sum(v["Social/Affordable Homes"] for v in development_mix.values())
    total_households = total_private_homes + total_social_homes

    annual_km_reduction_per_person = 229  # hardcoded in original model
    operating_cost_per_km = float(general.loc["Car operating cost", "Value"])
    value_of_time = float(general.loc["Value of time", "Value"])
    annual_minutes_saved_per_person = 752  # hardcoded in original model

    # --- Households with 1+ car: override, or weighted fallback (private/social homes x their car ownership rates) ---
    car_override = place_scenario_user_inputs["% of households in new TCL development with 1+ car"]
    if car_override is not None:
        households_with_1plus_car = total_households * car_override
    else:
        private_car_rate = float(pop_employ.loc["Households with 1+ car", "Private"])
        social_car_rate = float(pop_employ.loc["Households with 1+ car", "Social/affordable"])
        households_with_1plus_car = (total_private_homes * private_car_rate) + (total_social_homes * social_car_rate)

    car_ownership_reduction = float(general.loc["Car ownership reduction", "Value"])
    full_annual_car_ownership_cost = 3420  # hardcoded in original model

    gross_travel_cost_savings = total_residents_weighted * annual_km_reduction_per_person * operating_cost_per_km
    gross_time_savings = total_residents_weighted * (annual_minutes_saved_per_person / 60) * value_of_time
    gross_reduced_car_ownership_savings = households_with_1plus_car * car_ownership_reduction * full_annual_car_ownership_cost

    gross_annual_value = round(gross_travel_cost_savings + gross_time_savings + gross_reduced_car_ownership_savings, -3)

    # Uses SOCIAL additionality (matches Assumptions!B145)
    additionality = additionality_social(additionality_questions)
    deadweight = additionality["Deadweight"]
    displacement = additionality["Displacement"]
    leakage = additionality["Leakage"]

    net_factor = (1 - deadweight) * (1 - displacement) * (1 - leakage)
    net_annual_value = round(gross_annual_value * net_factor, -3)

    return {
        "Total residents (weighted)": total_residents_weighted,
        "Total households": total_households,
        "Households with 1+ car": households_with_1plus_car,
        "Gross travel cost savings": gross_travel_cost_savings,
        "Gross time savings": gross_time_savings,
        "Gross reduced car ownership savings": gross_reduced_car_ownership_savings,
        "Gross annual value": gross_annual_value,
        "Deadweight": deadweight,
        "Displacement": displacement,
        "Leakage": leakage,
        "Net factor": net_factor,
        "Net additional annual value": net_annual_value,
    }

#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

#################################################################################################################################################################################################################
### 8. COST OF CRIME
#################################################################################################################################################################################################################

def cost_of_crime(crime_inputs: dict, additionality_questions: dict, assumptions: dict) -> dict:
    crime = assumptions["crime"]
    categories = ["Violence", "Theft", "Criminal damage", "ASB"]

    additionality = additionality_crime(additionality_questions)
    deadweight = additionality["Deadweight"]
    displacement = additionality["Displacement"]
    leakage = additionality["Leakage"]
    net_factor = (1 - deadweight) * (1 - displacement) * (1 - leakage)

    results = {}
    gross_total = 0.0
    net_total = 0.0

    for category in categories:
        incidents_used = get_incidents_used(category, crime_inputs, assumptions)
        reduction_rate = float(crime.loc[category, "Reduction rate"])
        cost_per_incident = float(crime.loc[category, "Cost per incident"])

        gross_value = incidents_used * reduction_rate * cost_per_incident
        net_value = gross_value * net_factor

        results[category] = {
            "Incidents used": incidents_used,
            "Reduction rate": reduction_rate,
            "Cost per incident": cost_per_incident,
            "Gross value": gross_value,
            "Net value": net_value,
        }

        gross_total += gross_value
        net_total += net_value

    results["Total"] = {
        "Gross value": round(gross_total, -3),
        "Net value": round(net_total, -3),
    }
    results["Net factor"] = net_factor

    return results


#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

#################################################################################################################################################################################################################
### 9. ECONOMIC ACTIVITY
#################################################################################################################################################################################################################

def economic_activity(place_scenario_controls: dict, development_mix: dict, additionality_questions: dict, assumptions: dict) -> dict:
    household_spend = assumptions["household_spend"]
    economic_coeff = assumptions["economic_coeff"]

    spend_answer = place_scenario_controls["To what extent is there good quality and accessible opportunities for local people to spend money in the town centre consider "]
    offer_column_map = {"Strong offer": "Upper", "Some offer": "Central", "Limited offer": "Lower"}
    offer_column = offer_column_map[spend_answer]

    turnover_per_job = float(economic_coeff.loc["Average turnover per job", "Value"])
    gva_to_turnover_ratio = float(economic_coeff.loc["GVA to turnover ratio", "Value"])

    additionality = additionality_economic(additionality_questions, assumptions)
    deadweight = additionality["Deadweight"]
    displacement = additionality["Displacement"]
    multiplier = additionality["Multiplier"]
    net_factor = (1 - deadweight) * (1 - displacement) * multiplier

    # Maps household_spend row names to (typology, tenure key) in development_mix
    row_mapping = [
        ("Private detached", "Detached (3–5 bed)", "Private Homes"),
        ("Private semi/terrace", "Semi-detached / Terrace", "Private Homes"),
        ("Private low-rise flat", "Low-rise flats (2–4 storey)", "Private Homes"),
        ("Private higher density flat", "Higher density flats (5 plus storeys)", "Private Homes"),
        ("Private older persons", "Older Persons / Specialist", "Private Homes"),
        ("Social detached", "Detached (3–5 bed)", "Social/Affordable Homes"),
        ("Social semi/terrace", "Semi-detached / Terrace", "Social/Affordable Homes"),
        ("Social low-rise flat", "Low-rise flats (2–4 storey)", "Social/Affordable Homes"),
        ("Social higher density flat", "Higher density flats (5 plus storeys)", "Social/Affordable Homes"),
        ("Social older persons", "Older Persons / Specialist", "Social/Affordable Homes"),
    ]

    results = {}
    totals = {"Gross TC spend": 0.0, "Gross FTE jobs": 0.0, "Gross GVA": 0.0, "Net TC spend": 0.0, "Net FTE jobs": 0.0, "Net GVA": 0.0}

    for spend_row, typology, tenure_key in row_mapping:
        households = development_mix[typology][tenure_key]
        spend_per_household = float(household_spend.loc[spend_row, offer_column])

        gross_spend = households * spend_per_household
        gross_fte_jobs = gross_spend / turnover_per_job
        gross_gva = gross_spend * gva_to_turnover_ratio

        net_spend = gross_spend * net_factor
        net_fte_jobs = gross_fte_jobs * net_factor
        net_gva = gross_gva * net_factor

        results[spend_row] = {
            "Households": households,
            "Spend/household": spend_per_household,
            "Gross TC spend": gross_spend,
            "Gross FTE jobs": gross_fte_jobs,
            "Gross GVA": gross_gva,
            "Net TC spend": net_spend,
            "Net FTE jobs": net_fte_jobs,
            "Net GVA": net_gva,
        }

        totals["Gross TC spend"] += gross_spend
        totals["Gross FTE jobs"] += gross_fte_jobs
        totals["Gross GVA"] += gross_gva
        totals["Net TC spend"] += net_spend
        totals["Net FTE jobs"] += net_fte_jobs
        totals["Net GVA"] += net_gva

    results["Total"] = {
        "Gross TC spend": round(totals["Gross TC spend"], -3),
        "Gross FTE jobs": round(totals["Gross FTE jobs"]),
        "Gross GVA": round(totals["Gross GVA"], -3),
        "Net TC spend": round(totals["Net TC spend"], -3),
        "Net FTE jobs": round(totals["Net FTE jobs"]),
        "Net GVA": round(totals["Net GVA"], -3),
    }
    results["Net factor"] = net_factor

    return results


#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

#################################################################################################################################################################################################################
### 10. ONE-OFF CONSTRUCTION ACTIVITY
#################################################################################################################################################################################################################

def construction_activity(place_scenario_user_inputs: dict, additionality_questions: dict, assumptions: dict) -> dict:
    economic_coeff = assumptions["economic_coeff"]

    capital_cost = place_scenario_user_inputs["Estimate the capital costs of the town centre living development"]
    capex_per_pye_job = float(economic_coeff.loc["Construction capex per PYE job", "Value"])
    construction_gva_ratio = float(economic_coeff.loc["Construction GVA to capex ratio", "Value"])

    gross_pye_jobs = round(capital_cost / capex_per_pye_job)
    gross_gva = round(capital_cost * construction_gva_ratio, -3)

    additionality = additionality_construction(additionality_questions, assumptions)
    deadweight = additionality["Deadweight"]
    displacement = additionality["Displacement"]
    leakage = additionality["Leakage"]
    multiplier = additionality["Multiplier"]

    net_factor = (1 - deadweight) * (1 - displacement) * (1 - leakage) * multiplier

    net_pye_jobs = round(gross_pye_jobs * net_factor)
    net_gva = round(gross_gva * net_factor, -3)

    return {
        "Capital cost": capital_cost,
        "Gross PYE jobs": gross_pye_jobs,
        "Gross GVA": gross_gva,
        "Deadweight": deadweight,
        "Displacement": displacement,
        "Leakage": leakage,
        "Multiplier": multiplier,
        "Net factor": net_factor,
        "Net additional PYE jobs": net_pye_jobs,
        "Net additional GVA": net_gva,
    }


#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

#################################################################################################################################################################################################################
### 11. RENTAL RETURNS AND COUNCIL TAX
#################################################################################################################################################################################################################

def fiscal(development_mix: dict, additionality_questions: dict, assumptions: dict) -> dict:
    dwellingbytypology = assumptions["dwellingbytypology"]
    additionality_mappings = assumptions["additionality_mappings"]

    gross_council_tax = 0.0
    gross_rental_returns = 0.0

    for typology, values in development_mix.items():
        private_homes = values["Private Homes"]
        social_homes = values["Social/Affordable Homes"]

        council_tax_per_unit = float(dwellingbytypology.loc[typology, "Council Tax per unit"])
        rent_per_social_unit = float(dwellingbytypology.loc[typology, "Rent per social/MMR unit"])

        # Social homes pay half council tax (matches original formula's *0.5)
        gross_council_tax += (private_homes * council_tax_per_unit) + (social_homes * council_tax_per_unit * 0.5)
        gross_rental_returns += social_homes * rent_per_social_unit

    gross_fiscal_value = round(gross_council_tax + gross_rental_returns, -3)

    additionality = additionality_fiscal(additionality_questions)
    deadweight = additionality["Deadweight"]
    displacement = additionality["Displacement"]

    # Fiscal has no real Leakage question — uses a fixed default instead
    leakage = float(additionality_mappings.loc["Fiscal default for leakage", "Leakage"])

    net_factor = (1 - deadweight) * (1 - displacement) * (1 - leakage)
    net_fiscal_value = round(gross_fiscal_value * net_factor, -3)

    return {
        "Gross council tax": gross_council_tax,
        "Gross rental returns": gross_rental_returns,
        "Gross fiscal value": gross_fiscal_value,
        "Deadweight": deadweight,
        "Displacement": displacement,
        "Leakage": leakage,
        "Net factor": net_factor,
        "Net additional fiscal value": net_fiscal_value,
    }

#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

#################################################################################################################################################################################################################
### 12. LAND VALUES
#################################################################################################################################################################################################################

def land_values(land_infra_inputs: dict, place_scenario_user_inputs: dict, additionality_questions: dict, assumptions: dict) -> dict:
    additionality_mappings = assumptions["additionality_mappings"]
    land_infra_mult = assumptions["land_infra_mult"]

    qualifier = land_infra_inputs["Are you able to provide details on the GDV and existing land value"].strip()

    if qualifier == "No":
        return {
            "Total GDV": "N/A",
            "Capital cost": "N/A",
            "Developer return": "N/A",
            "Existing use / baseline land value": "N/A",
            "Gross land value uplift": "N/A",
            "Net additional land value uplift": "N/A",
        }

    gdv = land_infra_inputs["Total Gross Development Value (GDV) £"]
    capital_cost = place_scenario_user_inputs["Estimate the capital costs of the town centre living development"]
    baseline_land_value = land_infra_inputs["Existing use / baseline land value (£)"]

    if gdv is None or baseline_land_value is None:
        return {
            "Total GDV": gdv if gdv is not None else "Insufficient Data",
            "Capital cost": capital_cost,
            "Developer return": "Insufficient Data",
            "Existing use / baseline land value": baseline_land_value if baseline_land_value is not None else "Insufficient Data",
            "Gross land value uplift": "Insufficient Data",
            "Net additional land value uplift": "Insufficient Data",
        }

    developer_return_rate = float(land_infra_mult.loc["Average developer return on cost", "Value"])
    developer_return = round(capital_cost * developer_return_rate, -3)

    gross_land_value_uplift = round(gdv - capital_cost - developer_return - baseline_land_value, -3)

    additionality = additionality_land(additionality_questions)
    deadweight = additionality["Deadweight"]
    displacement = additionality["Displacement"]

    # Land has no real Leakage question — uses a fixed default instead
    leakage = float(additionality_mappings.loc["Land value default for leakage", "Leakage"])
    multiplier = 1  # hardcoded in original model

    net_factor = (1 - deadweight) * (1 - displacement) * (1 - leakage) * multiplier
    net_land_value_uplift = round(gross_land_value_uplift * net_factor, -3)

    return {
        "Total GDV": gdv,
        "Capital cost": capital_cost,
        "Developer return": developer_return,
        "Existing use / baseline land value": baseline_land_value,
        "Gross land value uplift": gross_land_value_uplift,
        "Deadweight": deadweight,
        "Displacement": displacement,
        "Leakage": leakage,
        "Multiplier": multiplier,
        "Net factor": net_factor,
        "Net additional land value uplift": net_land_value_uplift,
    }

#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

#################################################################################################################################################################################################################
### 13. PUBLIC SECTOR INFRASTRUCTURE COSTS
#################################################################################################################################################################################################################

def public_infrastructure(development_mix: dict, assumptions: dict) -> dict:
    land_infra_mult = assumptions["land_infra_mult"]
    additionality_mappings = assumptions["additionality_mappings"]

    avoided_cost_per_unit = float(land_infra_mult.loc["Avoided capital cost per unit for public sector infrastructure", "Value"])
    annual_revenue_saving_per_unit = float(land_infra_mult.loc["Annual revenue saving per unit for public sector infrastructure", "Value"])

    total_units = sum(v["Private Homes"] + v["Social/Affordable Homes"] for v in development_mix.values())

    # Fixed default additionality — not from a user question, applies to all developments
    row = additionality_mappings.loc["Public infrastructure  - default for all "]
    deadweight = float(row["Deadweight"])
    displacement = float(row["Displacement"])
    leakage = float(row["Leakage"])
    multiplier = 1  # hardcoded in original model

    net_factor = (1 - deadweight) * (1 - displacement) * (1 - leakage) * multiplier

    # --- One-off capital saving (unchanged) ---
    gross_infrastructure_savings = round(avoided_cost_per_unit * total_units, -3)
    net_infrastructure_savings = round(gross_infrastructure_savings * net_factor, -3)

    # --- New: annual revenue saving stream ---
    gross_annual_revenue_saving = round(annual_revenue_saving_per_unit * total_units, -3)
    net_annual_revenue_saving = round(gross_annual_revenue_saving * net_factor, -3)

    return {
        "Avoided capital cost per unit": avoided_cost_per_unit,
        "Annual revenue saving per unit": annual_revenue_saving_per_unit,
        "Total residential units": total_units,
        "Deadweight": deadweight,
        "Displacement": displacement,
        "Leakage": leakage,
        "Multiplier": multiplier,
        "Gross infrastructure savings": gross_infrastructure_savings,
        "Net factor": net_factor,
        "Net infrastructure savings": net_infrastructure_savings,
        "Gross annual revenue saving": gross_annual_revenue_saving,
        "Net annual revenue saving": net_annual_revenue_saving,
    }
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

#################################################################################################################################################################################################################
### 14. COMMERCIAL FLOORSPACE 
#################################################################################################################################################################################################################

def commercial_floorspace_indicator(commercial_floorspace_inputs: dict, additionality_questions: dict, assumptions: dict) -> dict:
    commercial = assumptions["commercial_floorspace"]

    additionality = additionality_commercial(additionality_questions, assumptions)
    deadweight = additionality["Deadweight"]
    displacement = additionality["Displacement"]
    multiplier = additionality["Multiplier"]
    net_factor = (1 - deadweight) * (1 - displacement) * multiplier

    results = {}
    totals = {"Floorspace": 0.0, "Gross FTE jobs": 0.0, "Gross GVA": 0.0, "Net FTE jobs": 0.0, "Net GVA": 0.0}

    for category, floorspace in commercial_floorspace_inputs.items():
        density = float(commercial.loc[category, "Floorspace density"])
        avg_gva_per_job = float(commercial.loc[category, "Avg GVA per FTE job"])

        fte_jobs = floorspace / density if density > 0 else 0.0
        gross_gva = fte_jobs * avg_gva_per_job

        net_fte_jobs = fte_jobs * net_factor
        net_gva = gross_gva * net_factor

        results[category] = {
            "Floorspace": floorspace,
            "FTE jobs": fte_jobs,
            "Gross GVA": gross_gva,
            "Net FTE jobs": net_fte_jobs,
            "Net GVA": net_gva,
        }

        totals["Floorspace"] += floorspace
        totals["Gross FTE jobs"] += fte_jobs
        totals["Gross GVA"] += gross_gva
        totals["Net FTE jobs"] += net_fte_jobs
        totals["Net GVA"] += net_gva

    results["Total"] = {
        "Floorspace": totals["Floorspace"],
        "Gross FTE jobs": round(totals["Gross FTE jobs"]),
        "Gross GVA": round(totals["Gross GVA"], -3),
        "Net FTE jobs": round(totals["Net FTE jobs"]),
        "Net GVA": round(totals["Net GVA"], -3),
    }

    # "CK occupancy assumptions" row — applies a flat 75% occupancy adjustment to the totals
    results["Occupancy-adjusted (75%)"] = {
        "Gross FTE jobs": round(results["Total"]["Gross FTE jobs"] * 0.75),
        "Gross GVA": round(results["Total"]["Gross GVA"] * 0.75, -3),
        "Net FTE jobs": round(results["Total"]["Net FTE jobs"] * 0.75),
        "Net GVA": round(results["Total"]["Net GVA"] * 0.75, -3),
    }

    return results


#################################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################################################################################################################################################################################

#################################################################################################################################################################################################################
### 14b. PURPOSE BUILT STUDENT ACCOMMODATION (PBSA)
#################################################################################################################################################################################################################

def pbsa_indicator(pbsa_inputs: dict, additionality_questions: dict, assumptions: dict) -> dict:
    economic_coeff = assumptions["economic_coeff"]
    commercial = assumptions["commercial_floorspace"]

    rooms = pbsa_inputs["Purpose Built Student Accommodation - Number of Rooms"]

    onsite_fte_jobs = rooms / 25

    offsite_spend_per_room = 5000
    total_offsite_spend = rooms * offsite_spend_per_room

    turnover_per_job = float(economic_coeff.loc["Average turnover per job", "Value"])
    offsite_jobs = total_offsite_spend / turnover_per_job if turnover_per_job > 0 else 0.0

    # --- Convert to GVA using a blended average of Retail, F&B, and Leisure/Culture rates ---
    retail_gva_per_job = float(commercial.loc["Retail and Town Centre Services", "Avg GVA per FTE job"])
    fnb_gva_per_job = float(commercial.loc["Food and Beverage / Hospitality", "Avg GVA per FTE job"])
    leisure_gva_per_job = float(commercial.loc["Leisure, Culture and Visitor Economy", "Avg GVA per FTE job"])
    avg_gva_per_job = (retail_gva_per_job + fnb_gva_per_job + leisure_gva_per_job) / 3

    offsite_gva = offsite_jobs * avg_gva_per_job

    gross_total_fte_jobs = onsite_fte_jobs + offsite_jobs
    gross_total_gva = offsite_gva

    additionality = additionality_commercial(additionality_questions, assumptions)
    deadweight = additionality["Deadweight"]
    displacement = additionality["Displacement"]
    multiplier = additionality["Multiplier"]
    net_factor = (1 - deadweight) * (1 - displacement) * multiplier

    net_total_fte_jobs = gross_total_fte_jobs * net_factor
    net_total_gva = gross_total_gva * net_factor

    return {
        "Number of rooms": rooms,
        "On-site FTE jobs (e.g. concierge)": onsite_fte_jobs,
        "Total off-site spend": total_offsite_spend,
        "Net total spend": total_offsite_spend * net_factor,
        "Off-site FTE jobs": offsite_jobs,
        "Off-site GVA": offsite_gva,
        "Gross total FTE jobs": gross_total_fte_jobs,
        "Gross total GVA": gross_total_gva,
        "Deadweight": deadweight,
        "Displacement": displacement,
        "Multiplier": multiplier,
        "Net factor": net_factor,
        "Net total FTE jobs": net_total_fte_jobs,
        "Net total GVA": net_total_gva,
    }