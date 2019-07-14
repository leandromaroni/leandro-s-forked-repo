
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_cities = ('chicago', 'new york city', 'washington')
    city = input('\nWould you like to see data for Chicago, New York City or Washington?\n').lower()
    
    while city not in valid_cities:
            city = input('\nWrong input!\nWould you like to see data for Chicago, New York City or Washington?\n').lower()
            
    # TO DO: get user input for month (all, january, february, ... , june)
    valid_months = ('january', 'february', 'march', 'april', 'may', 'june', 'all')
    month = input('\nWhat month would you like to explore the data from? January, February, March, April, May or June?\n Enter "all" for no month filter.\n').lower()
    
    while month not in valid_months:
            month = input('\nWrong input!\nWhat month would you like to explore the data from? January, February, March, April, May or June?\n Enter "all" for no month filter.\n').lower()
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')
    day = input('\nWhich the day of the week you want to explore data from? Enter "all" for no week day filter.\n').lower()
    while day not in valid_days:
            day = input('\nWrong input!\nWhich the day of the week you want to explore data from? Enter "all" for no week day filter.\n').lower()
    
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
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #converting start and end times to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    #getting new month, weekdays and hour columns that will help with the code building below
    df['month'] = df['Start Time'].dt.strftime("%B")
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour
    df['end_hour'] = df['End Time'].dt.hour
    
    # Display the most common month
    popular_month = df['month'].mode()[0]
    print('\nThe most common month is: ', popular_month)
    
    # TO DO: display the most common day of week
    popular_dayofweek = df['day_of_week'].mode()[0]
    print('\nThe most common day of the week is: ', popular_dayofweek)
    
    # TO DO: display the most common start hour
    popular_start_hour = df['start_hour'].mode()[0]
    print('\nThe most common hour of the day for a travel start is: ', popular_start_hour, 'hs')
    
    popular_end_hour = df['end_hour'].mode()[0]
    print('\nThe most common hour of the day for a travel end is: ', popular_end_hour, 'hs')
    
    print("\nThis calculation took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nThe most commonly used start station is: ', popular_start_station)
          
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nThe most commonly used end station is: ', popular_end_station)   
    
    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combinations'] = df['Start Station'] + ', ' + df['End Station']
    popular_station_combination = df['Station Combinations'].mode()[0]
    print('\nThe most frequent combination of start station and end station trip is: \n', popular_station_combination)
    
    print("\nThis calculation took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    
    df['Travel Duration'] = df['End Time'] - df['Start Time']
    
    start_time = time.time()
   
    # TO DO: display total travel time
    total_travel_time = df['Travel Duration'].sum()
    print('\nThe total travel time is: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Travel Duration'].mean()
    print('\nThe average travel time is: ', mean_travel_time)
    
    print("\nThis calculation took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats_1(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    user_types = user_types.to_dict()
    print('\nThe amount of users by user types are:')
    for key, value in user_types.items():
        print('{}: {}'.format(key, value))
    
    print("\nThis calculation took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats_2(df):
    """Displays statistics on bikeshare users with information that's available only in New York City and Chicago databases."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of gender
    genders = df['Gender'].value_counts()
    genders = genders.to_dict()
    print('\nThe amount of users by genders are: ')
    for key, value in genders.items():
        print('{}: {}'.format(key, value))

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth_year = df['Birth Year'].min().astype(np.int64)
    print('\nThe oldest user was born in: ', earliest_birth_year)

    most_recent_birth_year = df['Birth Year'].max().astype(np.int64)
    print('\nThe youngest user was born in: ', most_recent_birth_year)

    popular_birth_year = df['Birth Year'].mode()[0]
    popular_birth_year = popular_birth_year.astype(np.int64)
    print('\nMost users were born in: ', popular_birth_year)

    print("\nThis calculation took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        valid_input = ('yes', 'no')
        
        first = input('\nDo you wish to see data on time statistics? Enter yes or no.\n')
        while first not in valid_input:
            first = input('\nWrong input! Do you wish to see data on time statistics? Enter yes or no.\n')
        if first == 'yes':
            time_stats(df)
        
        second = input('\nDo you wish to see data on stations statistics? Enter yes or no.\n')
        while second not in valid_input:
            second = input('\nWrong input! Do you wish to see data on stations statistics? Enter yes or no.\n')
        if second == 'yes':
            station_stats(df)
        
        third = input('\nDo you wish to see data on trip duration statistics? Enter yes or no.\n')
        while third not in valid_input:
            third = input('\nWrong input! Do you wish to see data on trip duration statistics? Enter yes or no.\n')
        if third == 'yes':    
            trip_duration_stats(df)
        
        fourth = input('\nDo you wish to see data on user statistics? Enter yes or no.\n')
        while fourth not in valid_input:
            fourth = input('\nWrong input! Do you wish to see data on user statistics? Enter yes or no.\n')
        if fourth == 'yes':     
            user_stats_1(df)
            if city.lower() in ('chicago', 'new york city'):
                user_stats_2(df)    
        
        i = 0
        o = 5
        lines = input('\nWould you like to see five lines of raw data? Enter yes or no.\n')
        while lines not in valid_input:
            lines = input('\nWrong input! Would you like to see five lines of raw data? Enter yes or no.\n')
        while lines == 'yes':
            print(df.iloc[i:o])
            lines = input('\nWould you like to see five more lines of raw data? Enter yes or no.\n')
            while lines not in valid_input:
                lines = input('\nWrong input! Would you like to see five lines of raw data? Enter yes or no.\n')
            if lines == 'yes':
                i += 5
                o += 5

        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        
        while restart not in valid_input:
            restart = input('\nWrong input! Would you like to restart? Enter yes or no.\n')
            
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
