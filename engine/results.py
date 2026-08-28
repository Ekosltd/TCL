"""
Impact Dashboard calculations
"""

from calculations import (
    transport_emissions_valuation, embodied_carbon, environmental_quality,
    health_wellbeing, civic_engagement, travel_time_and_costs, cost_of_crime,
    economic_activity, construction_activity, fiscal, land_values,
    public_infrastructure, commercial_floorspace_indicator, pbsa_indicator,
    population_by_typology, demographic_employment_outputs,
)


def get_discount_factors(assumptions: dict) -> dict:
    
    discounting = assumptions["discounting"]
    discounting_controls = assumptions["discounting_controls"]

    social_rate = float(discounting.loc["Discount rate - social", "Value"])
    central_rate = float(discounting.loc["Discount rate - central", "Value"])
    years = float(discounting_controls.loc["Years", "Value"])

    def npv_factor(rate):
        return (1 - (1 + rate) ** -years) / rate

    return {
        "social_rate": social_rate,
        "central_rate": central_rate,
        "years": years,
        "social_npv_factor": npv_factor(social_rate),
        "central_npv_factor": npv_factor(central_rate),
    }


def build_dashboard(development_mix, place_scenario_controls, place_scenario_user_inputs,
                     crime_inputs, land_infra_inputs, commercial_floorspace_inputs, pbsa_inputs,
                     additionality_questions, assumptions) -> dict:

    factors = get_discount_factors(assumptions)
    social_f = factors["social_npv_factor"]
    central_f = factors["central_npv_factor"]

    # --- Run every indicator once ---
    transport = transport_emissions_valuation(place_scenario_controls, development_mix, additionality_questions, assumptions)
    carbon = embodied_carbon(development_mix, place_scenario_controls, additionality_questions, assumptions)
    env_quality = environmental_quality(place_scenario_controls, place_scenario_user_inputs, additionality_questions, assumptions)
    health = health_wellbeing(place_scenario_controls, development_mix, additionality_questions, assumptions)
    civic = civic_engagement(place_scenario_controls, development_mix, additionality_questions, assumptions)
    travel = travel_time_and_costs(place_scenario_controls, place_scenario_user_inputs, development_mix, additionality_questions, assumptions)
    crime = cost_of_crime(crime_inputs, additionality_questions, assumptions)
    econ = economic_activity(place_scenario_controls, development_mix, additionality_questions, assumptions)
    con = construction_activity(place_scenario_user_inputs, additionality_questions, assumptions)
    fis = fiscal(development_mix, additionality_questions, assumptions)
    land = land_values(land_infra_inputs, place_scenario_user_inputs, additionality_questions, assumptions)
    infra = public_infrastructure(development_mix, assumptions)
    commercial = commercial_floorspace_indicator(commercial_floorspace_inputs, additionality_questions, assumptions)
    pbsa = pbsa_indicator(pbsa_inputs, additionality_questions, assumptions)
    population = population_by_typology(development_mix, assumptions)
    demographics = demographic_employment_outputs(development_mix, assumptions)

    # --- Net additional values, per impact area ---
    env_q_net = env_quality["Net additional annual wellbeing value"]
    health_net = health["Net additional annual health value"]
    civic_net = civic["Net additional annual wellbeing value"]
    transport_net = transport["Net additional £ value"]
    travel_net = travel["Net additional annual value"]
    crime_net = crime["Total"]["Net value"]
    carbon_net = carbon["Net additional £ value"]  # one-off, not annuitised

    # =============================================================
    # SOCIAL VALUE — Annual + 10-Year NPV
    # =============================================================
    annual_social_value = round(env_q_net + health_net + civic_net + transport_net + travel_net + crime_net, -3)
    npv_social_value = round(
        (env_q_net + health_net + civic_net) * social_f
        + (transport_net + travel_net + crime_net) * central_f
        + carbon_net,
        -3
    )

    total_units = sum(v["Private Homes"] + v["Social/Affordable Homes"] for v in development_mix.values())
    social_value_per_home = round(npv_social_value / total_units, -3) if total_units > 0 else 0

    social_value = {
        "Annual": annual_social_value,
        "10-Year NPV": npv_social_value,
        "Social value per home (10yr NPV)": social_value_per_home,
    }

    # --- Sensitivity ±10% ---
    social_value_sensitivity = {
        "-10%": {"Annual social value": round(annual_social_value * 0.9, -3), "10yr Social value NPV": round(npv_social_value * 0.9, -3)},
        "Central": {"Annual social value": round(annual_social_value * 1.0, -3), "10yr Social value NPV": round(npv_social_value * 1.0, -3)},
        "+10%": {"Annual social value": round(annual_social_value * 1.1, -3), "10yr Social value NPV": round(npv_social_value * 1.1, -3)},
    }

    # =============================================================
    # SOCIAL VALUE COMPOSITION
    # =============================================================
    def safe_pct(x):
        return (x / annual_social_value) if annual_social_value else 0

    composition_annual = {
        "Environmental Quality": {"Annual": round(env_q_net, -3), "% of annual total": safe_pct(env_q_net)},
        "Health and Wellbeing": {"Annual": round(health_net, -3), "% of annual total": safe_pct(health_net)},
        "Civic / Belonging": {"Annual": round(civic_net, -3), "% of annual total": safe_pct(civic_net)},
        "Travel Time & Cost": {"Annual": round(travel_net, -3), "% of annual total": safe_pct(travel_net)},
        "Crime Reduction": {"Annual": round(crime_net, -3), "% of annual total": safe_pct(crime_net)},
        "Transport emissions": {"Annual": round(transport_net, -3), "% of annual total": safe_pct(transport_net)},
    }

    # NOTE: matches the original's exact (slightly misleadingly-labelled)
    # formula — this "Embodied carbon" one-off line actually combines
    # Transport Emissions net value + Embodied Carbon net value together.
    composition_oneoff = {
        "Embodied carbon": round(transport_net + carbon_net, -3),
    }

    # =============================================================
    # CORE DEVELOPMENT OUTPUTS
    # =============================================================
    core_outputs = {
        "Total Units": round(total_units),
        "Total Residents": round(population["Total"]["Total residents"]),
        "Working-age Adults": demographics["Working-age adults"],
        "Employed Adults": demographics["Employed adults"],
        "FTE jobs": round(econ["Total"]["Net FTE jobs"] + pbsa["Net total FTE jobs"], 2),
    }

    # =============================================================
    # ECONOMIC AND FISCAL VALUE — reported separately
    # =============================================================
    tc_spend_annual = round(econ["Total"]["Net TC spend"] + pbsa["Net total spend"], -3)
    gva_annual = round(econ["Total"]["Net GVA"] + pbsa["Net total GVA"], -3)
    fiscal_annual = round(fis["Net additional fiscal value"], -3)

    tc_spend_npv = round(tc_spend_annual * central_f, -3)
    gva_npv = round(gva_annual * central_f, -3)
    fiscal_npv = round(fiscal_annual * central_f, -3)

    land_oneoff = land["Net additional land value uplift"]
    infra_oneoff = round(infra["Net infrastructure savings"], -3)

    # --- Public Infrastructure annual revenue saving stream, discounted like the other annual values ---
    infra_revenue_annual = infra["Net annual revenue saving"]
    infra_revenue_npv = round(infra_revenue_annual * central_f, -3)

    econ_fiscal = {
        "Town Centre Spend": {"Annual": tc_spend_annual, "10-Year NPV": tc_spend_npv},
        "GVA": {"Annual": gva_annual, "10-Year NPV": gva_npv},
        "Fiscal": {"Annual": fiscal_annual, "10-Year NPV": fiscal_npv},
        "Land value uplift (one off)": land_oneoff,
        "Public infrastructure (one off)": infra_oneoff,
        "Public infrastructure revenue savings": {"Annual": infra_revenue_annual, "10-Year NPV": infra_revenue_npv},
    }

    def sens(x, round_to=-3):
        if not isinstance(x, (int, float)):
            return {"-10%": x, "Central": x, "+10%": x}
        return {"-10%": round(x * 0.9, round_to), "Central": round(x * 1.0, round_to), "+10%": round(x * 1.1, round_to)}

    econ_fiscal_sensitivity = {
        "Town Centre spend -  Annual value": sens(tc_spend_annual),
        "Town Centre spend - 10yr NPV": sens(tc_spend_npv),
        "GVA - Annual value": sens(gva_annual),
        "GVA - 10yr NPV": sens(gva_npv),
        "Fiscal - Annual value": sens(fiscal_annual),
        "Fiscal - 10yr NPV": sens(fiscal_npv),
        "Land value uplift - 10yr NPV": sens(land_oneoff),
        "Public infrastructure - 10yr NPV": sens(infra_oneoff),
        "Public infrastructure revenue savings - Annual value": sens(infra_revenue_annual),
        "Public infrastructure revenue savings - 10yr NPV": sens(infra_revenue_npv),
    }

    # =============================================================
    # ONE-OFF CONSTRUCTION IMPACTS
    # =============================================================
    construction_oneoff = {
        "Net additional GVA": con["Net additional GVA"],
        "Net additional PYE jobs": con["Net additional PYE jobs"],
    }

    # =============================================================
    # COMMERCIAL FLOORSPACE (supplementary) — sensitivity
    # =============================================================
    cf_gva_annual = commercial["Total"]["Net GVA"]
    cf_gva_npv = round(cf_gva_annual * central_f, -3)
    cf_fte_annual = commercial["Total"]["Net FTE jobs"]

    commercial_floorspace_sensitivity = {
        "Net additional GVA - Annual value": sens(cf_gva_annual),
        "Net additional GVA -  10yr NPV": sens(cf_gva_npv),
        "Net additional FTE jobs - Annual value": sens(cf_fte_annual, round_to=1),
    }

    return {
        "discount_factors": factors,
        "social_value": social_value,
        "social_value_sensitivity": social_value_sensitivity,
        "composition_annual": composition_annual,
        "composition_oneoff": composition_oneoff,
        "core_outputs": core_outputs,
        "econ_fiscal": econ_fiscal,
        "econ_fiscal_sensitivity": econ_fiscal_sensitivity,
        "construction_oneoff": construction_oneoff,
        "commercial_floorspace_sensitivity": commercial_floorspace_sensitivity,
    }