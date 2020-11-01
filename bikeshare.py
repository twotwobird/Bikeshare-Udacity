import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all', 'january', 'february', 'march', 'april', 'may' , 'june']

days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input("Select from the following cities: Chicago, New York City, or Washington: ")
    while True:
        if city.lower() in CITY_DATA.keys():
            city = city.lower()
            break
        else:
            city = input("Please select ONLY from the following cities: Chicago, New York City, or Washington: ")

    # TO DO: get user input for month (all, january, february, ... , june)
    
    month = input("Select a month to analyze from January through June. For no month filter, select 'all': ")
    
    while True:
        if month.lower() in months:
            month = month.lower()
            break
        else:
            month = input("Please select ONLY from the months of January through June: ")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = input("Select a day of the week to analyze. For no day filter, select 'all': ")
    while True:
        if day.lower() in days:
            day = day.lower()
            break
        else:
            day = input("Please check if you selected a proper day of the week: ")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    
    if month != 'all':
        month = month.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    common_month = df['month'].mode()[0]
    
    print("Most common month: " + str(common_month))
    
    # TO DO: display the most common day of week

    common_day = df['day'].mode()[0]
    
    print("Most common day: " + str(common_day))

    # TO DO: display the most common start hour
    
    common_hour = df['hour'].mode()[0]
    
    print("Most common hour: " + str(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start = str(df['Start Station'].mode()[0])
    
    print("Most commonly used start station: " + common_start)
    
    # TO DO: display most commonly used end station
    
    common_end = str(df['End Station'].mode()[0])
    
    print("Most commonly used end station: " + common_end)


    # TO DO: display most frequent combination of start station and end station trip
    
    df['combination'] = (df['Start Station'] + ' - ' + df['End Station'])
    common_combination = str(df['combination'].mode()[0])
    print("Most frequent combination of start station and end station trip is: " + common_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is: {} minutes".format(total_travel_time/60))


    # TO DO: display mean travel time
    
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time is: {} minutes".format(mean_travel_time/60))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print("Number of user types: " + str(user_types))

    
    # TO DO: Display counts of gender
    
    try:
        gender_count = df['Gender'].value_counts()
        print("Counts of gender: " + str(gender_count))
    except:
        print("There's no gender data for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    
    try:
        earliest_year = str(int(df['Birth Year'].min()))
        recent_year = str(int(df['Birth Year'].max()))
        common_year = str(int(df['Birth Year'].mode()[0]))
    
        print("Earliest birth year: " + earliest_year)
        print("Most recent birth year: " + recent_year)
        print("Most common birth year: " + common_year)
    except:
        print("There's no birth year data for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """Asks user if they would like to see five rows of data."""
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no.\n')
    
    start_loc = 0
    while view_data.lower() == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
