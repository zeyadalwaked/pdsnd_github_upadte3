import time
import pandas as pd
import numpy as np

# Mapping of city names to their respective CSV file names.
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks the user to specify a city, month, and day to analyze.

    Returns:
        city (str): Name of the city to analyze.
        month (str): Name of the month to filter by, or "all" to apply no month filter.
        day (str): Name of the day of week to filter by, or "all" to apply no day filter.
    """
    print("Hello! Let's explore some US bikeshare data!")

    # Validate city input
    valid_cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input("Please enter the city (Chicago, New York City, Washington): ").strip().lower()
        if city in valid_cities:
            break
        print("Invalid city. Please choose from Chicago, New York City, or Washington.")

    # Validate month input
    valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Please enter the month (January, February, March, April, May, June) or 'all': ").strip().lower()
        if month in valid_months:
            break
        print("Invalid month. Please enter a valid month or 'all'.")

    # Validate day input
    valid_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Please enter the day of week (e.g., Monday, Tuesday, ...) or 'all': ").strip().lower()
        if day in valid_days:
            break
        print("Invalid day. Please enter a valid day of the week or 'all'.")

    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and applies filters by month and day if applicable.

    Args:
        city (str): Name of the city.
        month (str): Name of the month or "all".
        day (str): Name of the day of week or "all".

    Returns:
        df (DataFrame): Pandas DataFrame containing the filtered city data.
    """
    # Load data file into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' to datetime and create new columns for month and day of week.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_index = months.index(month) + 1  # January is 1, February is 2, etc.
        df = df[df['month'] == month_index]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day]

    # Refactoring Change 1 : Added a function to rename columns for consistency
    df.rename(columns=lambda x: x.strip().lower().replace(' ', '_'), inplace=True)

    return df

def display_data(df):
    """Displays raw data upon user request."""
    view_data = input('\nWould you like to view the first 5 rows of data? Enter yes or no: ').lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input('\nWould you like to view the next 5 rows of data? Enter yes or no: ').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)

        # Refactoring Change  2: Simplified restart logic
        if input('\nWould you like to restart? Enter yes or no: ').strip().lower() != 'yes':
            break

if __name__ == "__main__":
    main()
