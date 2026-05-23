import pandas as pd
import streamlit as st

def charge():
    dg = pd.read_csv("dg.csv")
    DF = pd.read_csv("DF.csv", compression="gzip")
    df_concat = pd.read_csv("df_concat.csv")

    return dg, DF, df_concat