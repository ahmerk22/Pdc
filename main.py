import pandas as pd
from collections import Counter
from data_processing import load_data, process_data,find_most_common_date

def main():
    # Load data from CSV files
    students_df, fees_df = load_data()

    # Process data to get relevant fee submission dates
    relevant_dates = process_data(students_df, fees_df)

    # Calculate frequency of dates using Counter
    date_frequency = Counter(relevant_dates)

    #Finding out the most common date of fees submission
    most_common_date, frequency = find_most_common_date(fees_df)

    # Display results
    print("\nRelevant Fee Submission Dates:", relevant_dates)
    print("\nFrequency of Relevant Fee Submission Dates:")
    for date, freq in date_frequency.items():
        print(f"{date}: {freq}")
     
    print(f"Most Common Fee Submission Date: {most_common_date} with {frequency} fees submissions.")


if __name__ == "__main__":
    main()
