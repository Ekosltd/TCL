"""
Based on the SFT Brand Guidelines
"""

import base64
from pathlib import Path
import pandas as pd
import streamlit as st

# Primary colours
SFT_DARK_GREY = "#434343"
SFT_BLUE = "#0071ba"
SFT_NAVY = "#0c2d56"
SFT_MID_BLUE = "#0c528c"
SFT_HEADER_BLUE = "#0C528C"
SFT_TEAL_GREEN = "#008172"
SFT_TEAL = "#47e0d4"
SFT_GREEN = "#389d6a"
SFT_BLUE_GREY = "#657e9d"
SFT_LIGHT_GREY = "#e3dfdc"
SFT_PALE_TEAL = "#eaf6f4"
SFT_CREAM = "#F2EEEA"

WHITE_LOGO_PATH = Path(__file__).resolve().parent / "logo.png"

BRAND_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
}}

.stApp {{
    background-color: {SFT_CREAM};
}}

h1, h2, h3 {{
    color: {SFT_NAVY};
    font-weight: 700;
}}

h2 {{
    border-left: 4px solid {SFT_BLUE};
    padding-left: 0.6rem;
    margin-top: 1.8rem;
}}

h3 {{
    color: {SFT_MID_BLUE};
    font-weight: 600;
    margin-top: 1.2rem;
    border-bottom: 1px solid {SFT_LIGHT_GREY};
    padding-bottom: 0.2rem;
}}

[data-testid="stCaptionContainer"] {{
    color: {SFT_BLUE_GREY};
}}

hr {{
    border-top: 1px solid {SFT_LIGHT_GREY};
}}

.stButton > button[kind="primary"] {{
    background-color: {SFT_BLUE};
    border-color: {SFT_BLUE};
    font-weight: 600;
}}
.stButton > button[kind="primary"]:hover {{
    background-color: {SFT_NAVY};
    border-color: {SFT_NAVY};
}}

button[data-baseweb="tab"] {{
    font-weight: 600;
    color: {SFT_DARK_GREY};
}}
button[data-baseweb="tab"][aria-selected="true"] {{
    color: {SFT_BLUE};
}}
div[data-baseweb="tab-highlight"] {{
    background-color: {SFT_BLUE} !important;
}}

[data-testid="stMetric"] {{
    background-color: #ffffff;
    border: 1px solid {SFT_LIGHT_GREY};
    border-radius: 6px;
    padding: 0.6rem 0.8rem;
}}
[data-testid="stMetricValue"] {{
    color: {SFT_NAVY};
}}
[data-testid="stMetricLabel"] {{
    color: {SFT_DARK_GREY};
}}

[data-testid="stExpander"] summary {{
    font-weight: 600;
    color: {SFT_NAVY};
}}
[data-testid="stExpander"] {{
    border: 1px solid {SFT_LIGHT_GREY};
    border-radius: 6px;
    background-color: #ffffff;
}}

.sft-callout {{
    background-color: {SFT_PALE_TEAL};
    border-left: 4px solid {SFT_TEAL_GREEN};
    border-radius: 4px;
    padding: 0.9rem 1.1rem;
    margin: 0.8rem 0 1.2rem 0;
    color: {SFT_DARK_GREY};
}}

.sft-table {{
    width: 100%;
    border-collapse: collapse;
    font-family: 'Inter', sans-serif;
    margin-bottom: 1rem;
    background-color: #ffffff;
}}
.sft-table th {{
    background-color: {SFT_NAVY};
    color: white;
    text-align: left;
    padding: 0.5rem 0.75rem;
    font-weight: 600;
}}
.sft-table td {{
    padding: 0.5rem 0.75rem;
    border-bottom: 1px solid {SFT_LIGHT_GREY};
    color: {SFT_DARK_GREY};
}}
.sft-table tr:nth-child(even) td {{
    background-color: #f7f6f5;
}}

.sft-header {{
    background-color: {SFT_HEADER_BLUE};
    border-radius: 8px;
    padding: 1.2rem 2rem;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 1.5rem;
}}
.sft-header img {{
    height: 44px;
}}
.sft-header span {{
    color: white;
    font-size: 1.8rem;
    font-weight: 700;
    font-family: 'Inter', sans-serif;
}}
</style>
"""


def inject_brand_css():
    st.markdown(BRAND_CSS, unsafe_allow_html=True)


def render_header(title: str):
    """Header bar (SFT_HEADER_BLUE) with the white logo and page title, sitting inside
    the normal page width (not full-bleed, to avoid layout issues)."""
    if WHITE_LOGO_PATH.exists():
        logo_b64 = base64.b64encode(WHITE_LOGO_PATH.read_bytes()).decode()
        logo_html = f'<img src="data:image/png;base64,{logo_b64}" />'
    else:
        logo_html = ""
    st.markdown(
        f'<div class="sft-header">{logo_html}<span>{title}</span></div>',
        unsafe_allow_html=True,
    )


def render_brand_table(df: pd.DataFrame):
    """Renders a DataFrame as a branded HTML table (Inter font, SFT colours)."""
    st.markdown(df.to_html(classes="sft-table", index=False, escape=False), unsafe_allow_html=True)


def brand_callout(text: str):
    """A styled callout box (teal accent). Pass HTML, not Markdown, since this renders raw."""
    st.markdown(f'<div class="sft-callout">{text}</div>', unsafe_allow_html=True)


def render_stat_row(pairs: list[tuple[str, str]]):
    """Renders a row of label/value pairs as boxed metric cards, for standalone numbers
    that would otherwise sit unstyled (e.g. the one-off impacts breakdown)."""
    cols = st.columns(len(pairs))
    for col, (label, value) in zip(cols, pairs):
        col.metric(label, value)