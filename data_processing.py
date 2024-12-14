import pandas as pd

def load_data():
    
    students_df = pd.read_csv("students.csv")
    fees_df = pd.read_csv("fees.csv")
    return students_df, fees_df

def process_data(students_df, fees_df):
    
    relevant_dates = []

    for _, student_row in students_df.iterrows():
        student_id = student_row["student_id"]

        # Filter fees_df for the current student_id
        student_fees = fees_df[fees_df["student_id"] == student_id]

        # Append fee submission dates to the list
        relevant_dates.extend(student_fees["fee_submission_date"].tolist())
    
    return relevant_dates
def find_most_common_date(fees_df):
    from collections import Counter

    # Extract fee submission dates
    relevant_dates = fees_df["fee_submission_date"].tolist()

    # Calculate the frequency of each date
    date_frequency = Counter(relevant_dates)

    # Get the most common date
    most_common_date, frequency = date_frequency.most_common(1)[0]
    return most_common_date, frequency
