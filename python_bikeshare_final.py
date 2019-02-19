import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ["chicago", "new york city", "washington"]

months = ["january", "february", "march", "april", "may", "june"]

days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

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
 
    city = input("Please enter a city of your choice: Chicago, New York City or Washington: ").lower()

    if city.lower() == "washington" or city == "chicago" or city == "new york city":
        check_city = True
    else:
        check_city = False
    
    while check_city == False:
        city = input("Please enter a city of your choice: Chicago, New York City or Washington: ")
        break
    
    print("Great! Let's get you the information you need on {}.".format(city.title()))
    
    # TO DO: get user input for month (all, january, february, ... , june)
    filter = input("Would you like to filter by day, month or all? ")
   
    if filter == "day":
        day = input("Please enter a day of the week: Monday through Sunday or all for no day filter: ").lower()
        month = "all"
    elif filter == "month":
        month = input("Please enter a month of the year, January through June: ").lower()
        day = "all"
    else:
        day = "all"
        month = "all"
  
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

    # convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns    
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name

    # filter by month if applicable
    if month != "all":
 
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df["month"] == month]

    # filter by day of week if applicable
    if day != "all":
        # filter by day of week to create the new dataframe
        df = df[df["day_of_week"] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    most_common_month = df["month"].mode()[0]
    
    if most_common_month == 1:
        most_common_month = "January"
    elif most_common_month == 2:
        most_common_month = "February"
    elif most_common_month == 3:
        most_common_month = "March"
    elif most_common_month == 4:
        most_common_month = "April"
    elif most_common_month == 5:
        most_common_month = "May"
    else:
        most_common_month = "June"
    
    print("The most common month is {}.".format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df["day_of_week"].mode()[0]
    print("The most common day of the week is {}.".format(most_common_day))
    
    # TO DO: display the most common start hour
    most_common_start_hour = df["Start Time"].dt.hour.mode()[0]
    print("The most common start hour is {}.".format(most_common_start_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df["Start Station"].mode()[0]
    print("The most common start station is {}.".format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df["End Station"].mode()[0]
    print("The most common end station is {}.".format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration = df["Trip Duration"]
    total_travel_time = trip_duration.sum()
    print("The total travel time is {}.".format(total_travel_time))

    # TO DO: display mean travel time
    average_travel_time = trip_duration.mean()
    print("The average travel time is {}.".format(average_travel_time))
    
    # Display the quickest travel time
    quickest_travel_time = trip_duration.min()
    print("The fastest time was {}.".format(quickest_travel_time))
    
    #Display the longest travel time
    longest_travel_time = trip_duration.max()
    print("The slowest time was {}.".format(longest_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("The user types include the following: {}.".format(user_types))
    
    # TO DO: Display counts of gender
    try:
        gender_types = df["Gender"].value_counts()
        earliest_birth_year = int(df["Birth Year"].min())
        most_recent_birth_year = int(df["Birth Year"].max())
        most_common_birth_year = int(df["Birth Year"].mode()[0])
        print("The gender counts include the following {}.".format(gender_types))
        print("The earliest, most recent and most common birth years are as follows: {}, {} and {}.".format(earliest_birth_year, most_recent_birth_year, most_common_birth_year))
    except:
        pass   
    # TO DO: Display earliest, most recent, and most common year of birth
 
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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
if __name__ == "__main__":
	main()