import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    def get_city():
        """ Ask for city from the list to start analyze """
        cities_list = ["chicago", "new york", "washington"]
        city = input("Would you like to see data for Chicago, New York, or Washington?\n").strip().lower()
        while city not in cities_list :
            city = input ("Please enter a valid city: ").strip().lower()
        return city    
    
    city = get_city()

    Time_frame = ["month", "day", "not at all"]
    Day_or_Month = input("Would you like to filter the data by month, day, or not at all?\n").strip().lower()
    while Day_or_Month not in Time_frame:
        Day_or_Month = input("Please enter a valid Time_frame: ").strip().lower()
           
    # get user input for month (all, january, february, ... , june)
    
    
    def get_month():
        """ Ask for month to filter by, first six months only """
        if Day_or_Month == "month":
            months_list = ["january", "february", "march", "april", "may", "june"]
            month = input("(if they choose month) Which month- January, February, March, April, May, or June?\n").strip().lower()
            while month not in months_list :
                month = input("Please enter a valid month: ").strip().lower()
        elif Day_or_Month != "month":
            month = "all"    
        return month 

    month = get_month()   

    # get user input for day of week (all, monday, tuesday, ... sunday)

    def get_day():
        """ Ask for day to filter by """
        if Day_or_Month == "day":
            days_list = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
            day = input("(if they choose day) Which day- Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, or Friday?\n").strip().lower()
            while day not in days_list :
                day = input("Please enter a valid day: ").strip().lower()
        elif Day_or_Month != "day":
            day = "all"
        return day
    day = get_day() 

    
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month =  df['month'].mode()[0]
    month_count = df['month'].count()
    print("\nThe most common month is {} count: {}".format(common_month, month_count))
    

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    day_count = df['day_of_week'].value_counts()[0]
    print("\nThe most common day is {} count: {}".format(common_day, day_count))

    # display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    hour_count = df['hour'].value_counts()[0]

    print('\nThe most common Start Hour is {} count: {}'.format(common_hour, hour_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
     

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    count1 = df['Start Station'].value_counts()[0]
    print("\nThe most common start station is {} count: {}".format(common_start_station, count1))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    count2 = df['End Station'].value_counts()[0]
    print("\nThe most common end station is {} count: {}".format(common_end_station, count2))

    # display most frequent combination of start station and end station trip
    df['Start to End'] = df['Start Station'] + " to " + df['End Station']
    common_trip = df['Start to End'].mode()[0]
    count3 = df['Start to End'].value_counts()[0]
    print("\nThe most common trip is {} count: {}".format(common_trip, count3))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = float(df['Trip Duration'].sum())
    count1 = df['Trip Duration'].count()
    print("\nTotal travel time is {} count: {}".format(total_travel_time, count1))

    # display mean travel time
    average_travel_time = float(df['Trip Duration'].mean())
    count2 = df['Trip Duration'].count()
    print("\nAverage travel time is {} count: {}".format(average_travel_time, count2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)  

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print(user_type)

    # Display counts of gender
    if "Gender" in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print("earliest year is: {} ,recent year is: {} ,most common year is: {}".format(earliest_year, recent_year, most_common_year))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)      


def display_raw_data(df):
    """Display random of raw data if asked"""

    print('\nDisplaying random raw data...\n')
    start_time = time.time()

    response_list = ['yes', 'no']
    response = input("\nDo you want to see raw data?\n").strip().lower()
    while response not in response_list:
        response = input("\nPlease answer yes or no\n").strip().lower()
    while response == "yes":
        raw_data = print(df.sample(5))
        response = input("\nDo you want to see more of raw data?\n").strip().lower()
        while response not in response_list:
            response = input("\nPlease answer yes or no\n").strip().lower()
        if response == "no":
           break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()




 

