import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#months = {'all':0, 'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6}
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

days = {'all':0, 'monday':1, 'tuesday':2, 'wednesday':3, 'thursday':4, 'friday':5, 'saturday':6, 'sunday':7}


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
    city = ''
    while city not in CITY_DATA.keys():
        print("Please choose one of the following: Chicago, New York City and Washington: ")
        city = input('Enter city: ').lower()
    
      
    
    # TO DO: get user input for month (all, january, february, ... , june)
   
    month = ''
    while month not in months:
        print("\nPlease enter month between January and June: ")
        month = input("Enter month: ").lower()
    


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = ''
    while day not in days.keys():
        print('\nPlease enter a day of the week: ')
        day = input('Enter day: ').lower()


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


    return df

                

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\ndef time_stats(df): most Frequent Times of Travel...\n')
    start_time = time.time()
    #months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all':7}
    # TO DO: display the most common month
    most_common_month = months[df['month'].mode()[0]]
    
  
   # most_common_month = months[most_common_month]
    
    #most_common_month = df[df['month'] == months.value()]
    print('The most common month is {}'.format(most_common_month).title())


    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]
    print('The most common day is {}'.format(most_common_day))

    # TO DO: display the most common start hour
    # extract hour from Start Time
    df['Start Hour'] = df['Start Time'].dt.hour
    print('The most common start hour is {}'.format(df['Start Hour'].mode()[0]))
          
    print("\nThis took %s seconds.".format(time.time() - start_time))
    print('-'*40)  
        
   
   #most_common_start_hour = df['hour'].mode()[0]
   #print('The most common start hour is {}'.format(most_common_start_hour))
  
   
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is {}'.format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most common end station is {}'.format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    #df['start_end'] = df['Start Station'] + '-' + df['End Station']
    df['start_end_station'] = df['Start Station'] + ' - ' + df['End Station']
    most_common_start_end_station = df['start_end_station'].mode()[0]
    print('The most common start and end station combination is {}'.format(most_common_start_end_station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time =  sum(df['Trip Duration'])
    print('The total travel time is {}seconds.'.format(total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is {}seconds.'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types: \n',user_types)

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('\nCounts of gender: \n', gender_count)
    except:
        print('\nGender type: No data available')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
       most_earliest_year = df['Birth Year'].min()   
       print('\nThe earliest year of bith: {}'.format(most_earliest_year))
    except:
       print('\nMost earliest Birth Year: No data available for this city')
    
    try:
        most_recent_year = df['Birth Year'].max()
        print('The most recent year of bith: {}'.format(most_recent_year))
    except:
        print('Most recent Birth Year: No data available for this city')
    
    try:
        most_common_year = df['Birth Year'].mode()[0]
        print('The most common year of bith: {}'.format(most_common_year))
    except:
        print('Most common Birth Year: No data available for this city')
        
        
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
        
        raw_data = input('\nWould you like to view the raw data? Enter yes or no.\n').lower()
        more_data = True
        more_rows = 0
        while (more_data):
            print(df[more_rows:more_rows + 5])
            more_rows += 5
            ask_for_more = input('Do you want to see more rows of data? Enter yes or no ')
            if ask_for_more == 'no'.lower():
                more_data = False
           
        
                    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
