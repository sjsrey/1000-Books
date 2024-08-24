"""One thousand books project"""

import pandas as pd
import bibtexparser

def read_bibtex_to_dataframe(bibtex_file):
    """
    Reads a BibTeX file and converts it into a pandas DataFrame.

    Parameters:
    bibtex_file (str): Path to the BibTeX file.

    Returns:
    pandas.DataFrame: DataFrame containing the BibTeX entries.
    """
    with open(bibtex_file) as bibtex_file:
        bibtex_str = bibtex_file.read()

    bib_database = bibtexparser.loads(bibtex_str)
    df = pd.DataFrame(bib_database.entries)
    return df

def monthly(bibtex_file):
    df = read_bibtex_to_dataframe(bibtex_file)
    df["date"] = pd.to_datetime(df["annotation"], errors="coerce")
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["pages"] = df["pagetotal"].astype(float).fillna(0).astype(int)
    monthly_df = df.groupby(["year", "month"])["pages"].sum()
    return monthly_df
