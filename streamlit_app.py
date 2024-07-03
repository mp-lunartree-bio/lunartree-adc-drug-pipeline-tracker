import streamlit as st
import pandas as pd
import json

# Load JSON data
@st.cache_data
def load_data():
    with open('result.json') as f:
        data = json.load(f)
    return data

data = load_data()

# Function to create a table view with a search bar
def display_table(data, columns, key):
    search_term = st.text_input("Search", key=key)
    df = pd.DataFrame(data)
    if search_term:
        df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
    st.dataframe(df[columns])

# Create tabs
tabs = st.tabs(["Drugs", "Orgs", "Trials"])

# Display data for each tab
with tabs[0]:
    st.header("Drugs")
    # drug_columns = list(data['drugs'][0].keys())  # Customize the columns you want to display
    drug_columns = [
        'heading', 'names', 'phases', 'Max Phase', 'developers'
    ]
    display_table(data['drugs'], drug_columns, key='drugs')

with tabs[1]:
    st.header("Orgs")
    org_columns = list(data['orgs'][0].keys())  # Customize the columns you want to display
    display_table(data['orgs'], org_columns, key='orgs')

with tabs[2]:
    st.header("Trials")
    trial_columns = list(data['trials'][0].keys())  # Customize the columns you want to display
    display_table(data['trials'], trial_columns, key='trials')
