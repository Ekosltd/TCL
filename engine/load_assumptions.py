"""
Loads every sheet from data/assumptions.xlsx into a dictionary of pandas DataFrames, one per sheet. Place where engine gets assumptions from. 

"""

from pathlib import Path
import pandas as pd

# path to the assumptions file
ASSUMPTIONS_PATH = Path(__file__).resolve().parent.parent / "data" / "assumptions.xlsx"

#load assumptions from the assumptions file into a dictionary of pandas DataFrames
def load_assumptions(path: Path = ASSUMPTIONS_PATH) -> dict[str, pd.DataFrame]:
    sheets = pd.read_excel(path, sheet_name=None, header=0, index_col=0)
    return sheets

#print the first few rows of every sheet
def preview(sheets: dict[str, pd.DataFrame]) -> None:
    for name, df in sheets.items():
        print(f"\n=== {name} — shape: {df.shape} ===")
        print(df.head())


if __name__ == "__main__":
    assumptions = load_assumptions()
    preview(assumptions)