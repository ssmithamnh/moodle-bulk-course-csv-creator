import streamlit as st
import pandas as pd
from datetime import datetime

def main():
    st.title("Moodle Course Bulk Upload")

    # Prompt user for a number
    number = st.number_input("Enter Cohort Number:", min_value=0, step=1)
    prior_cohort_number = number - 1
    # Get current and next year
    current_year = datetime.now().year
    next_year = current_year + 1
    last_two_digits = str(current_year)[-2:]
    last_two_digits_minus_1 = str(current_year - 1)[-2:]
    
    # Load DataFrame
    df = pd.read_csv("data/template.csv")

    # Replace placeholders
    def replace_placeholders(x):
        if isinstance(x, str):
            x = x.replace("YEAR_1", str(next_year))
            x = x.replace("YEAR", str(current_year))
            x = x.replace("NUM", str(int(number)))
            x = x.replace("LAST_TWO_DIGITS", last_two_digits)
            x = x.replace("PRIOR", str(prior_cohort_number))
            x = x.replace("CURRENT", str(last_two_digits_minus_1))
        return x

    # Apply the function to the DataFrame
    revised_df = df.applymap(replace_placeholders)

    st.subheader(f"C{number} Courses CSV to be Uploaded")
    st.dataframe(revised_df)

if __name__ == "__main__":
    main()