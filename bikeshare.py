## packages

import time
import csv
import pandas as pd

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.
    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''

    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    if city == 'Chicago':
        return chicago
    elif city == 'New York':
        return new_york_city
    elif city == 'Washington':
        return washington
    else:
        print('!!! Try Again !!! YOU HAVE ENTERED WRONG INPUT')
        exit()

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.
    Args:
        none.
    Returns:
        (str) or (Integer) based on choice of User(Month or Day)
    '''

    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')

    if time_period == 'month':
        return get_month()
    elif time_period == 'day':
        month = get_month()
        return get_day(month)
    else:
        return 'none'

def get_month():
    '''Asks the user for a month and returns the specified month.
    Args:
        none.
    Returns:
        (str) Name of month chosen by User
    '''
    
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    return month

def get_day(month):
    '''Asks the user for a day and returns the specified day.
    Args:
        Month value.
    Returns:
        (Integer) Day chosen by user
    '''
    day = input('\nWhich day? Please type your response as an integer.\n')
    return day

def popular_month(city_file, time_period):
    '''Calculates the most popular month for start time
    Args:
        Filename for a city's bikeshare data, Starting Time.
    Returns:
        (Integer) Number of the respective Month(1-12) which is most popular. 
    '''

    print('\n#### CALCULATING MOST POPLULAR MONTH FROM YOUR DATA ####\n')
    
    df = pd.read_csv(city_file)
    
    df = df.dropna(subset=['Start Time'])
    s = df['Start Time'].value_counts().idxmax()
    
    date,time = s.split()
    year, month, day = date.split('-')

    if month == '01':
        print('Januray is the popular month')
    elif month == '02':
        print('February is the popular month')
    elif month == '03':
        print('March is the popular month')
    elif month == '04':
        print('April is the popular month')
    elif month == '05':
        print('May is the popular month')
    elif month == '06':
        print('June is the popular month')
    elif month == '07':
        print('July is the popular month')
    elif month == '08':
        print('August is the popular month')
    elif month == '09':
        print('September is the popular month')
    elif month == '10':
        print('October is the popular month')
    elif month == '11':
        print('November is the popular month')
    else:
        print('December is the popular month')

    return int(month)  

def popular_day(city_file, time_period):
    '''Calculates the most popular day for start time
    Args:
        Filename for a city's bikeshare data, Starting Time.
    Returns:
        (Integer) Number of the respective day(1-7) which is most popular.
    '''
    print('\n#### CALCULATING MOST POPLULAR DAY FROM YOUR DATA ####\n')
    
    df = pd.read_csv(city_file)
    df = df.dropna(subset=['Start Time'])
    s = df['Start Time'].value_counts().idxmax()
    
    date,time = s.split()
    year, month, day = date.split('-')
    day = int(day)
    day = day%7
    if day == '0':
        print('Sunday is the popular day')
    elif day == '1':
        print('Monday is the popular day')
    elif day == '2':
        print('Tuesday is the popular day')
    elif day == '3':
        print('Wednesday is the popular day')
    elif day == '4':
        print('Thrusday is the popular day')
    elif day == '5':
        print('Friday is the popular day')
    else:
        print('Saturday is the popular day')

    return int(day)+1

def popular_hour(city_file, time_period):
    '''Calculates the most popular hour for start time
    Args:
        Filename for a city's bikeshare data, Starting Time.
    Returns:
        (Integer) Number of the respective Hour(1-11) which is most popular.
    '''
    print('\n#### CALCULATING MOST POPLULAR HOUR OF THE DAY FROM YOUR DATA ####\n')
    
    df = pd.read_csv(city_file)
    df = df.dropna(subset=['Start Time'])
    s = df['Start Time'].value_counts().idxmax()

    date,time = s.split(' ')
    
    if city_file == chicago: 
        hour,minute = time.split(':')
    else:
        hour,minute,second = time.split(':')
    if int(hour) >= 12:
        hour = int(hour)%12
        print('Popular Hour is',hour,'PM')
    else:
        print('Popular Hour is',hour,'AM')
    
    return hour

def trip_duration(city_file, time_period):
    '''Calculates the trip duration for start time
    Args:
        Filename for a city's bikeshare data, Starting Time.
    Returns:
        (Integer) Sum of Trip Duration of the User's File.
    '''
    print('\n#### CALCULATING TRIP DURATION FROM YOUR DATA ####\n')

    df = pd.read_csv(city_file)

    sum1 = df['Trip Duration'].sum()

    print('The Total Trip Duration is', sum1)

    df = df.dropna(subset=['Start Time'])
    count1 = df.size

    print('The Mean Trip Duration is', int(sum1/count1))
    
    return sum1

def popular_stations(city_file, time_period):
    '''Calculates the most popular start and end station for start time
    Args:
        Filename for a city's bikeshare data, Starting Time.
    Returns:
        (str) Name of the End Station which is most popular.
    '''
    print('\n#### CALCULATING MOST POPLULAR STATIONS FROM YOUR DATA ####\n')

    df = pd.read_csv(city_file)
    df = df.dropna(subset=['Start Station'])
    s = df['Start Station'].value_counts().idxmax()

    print('Popular Start Station is', s)

    df = df.dropna(subset=['End Station'])
    s = df['End Station'].value_counts().idxmax()

    print('Popular End Station is', s)

    return s

def popular_trip(city_file, time_period):
    '''Calculates the most popular Trip Duration for start time
    Args:
        Filename for a city's bikeshare data, Starting Time.
    Returns:
        (Integer) Value of the Trip Duration which is most popular.
    '''

    print('\n#### CALCULATING POPLULAR TRIP FROM YOUR DATA ####\n')
    
    df = pd.read_csv(city_file)
    df = df.dropna(subset=['Trip Duration'])
    s = df['Trip Duration'].value_counts().idxmax()
    
    print('The Most Popular Trip Duration is: ', s)

    return s

def users(city_file, time_period):
    '''Calculates the count of each user for start time
    Args:
        Filename for a city's bikeshare data, Starting Time.
    Returns:
        (Integer) Count of Each User in the file.
    '''
    print('\n#### CALCULATING COUNT OF USERS FROM YOUR DATA ####\n')
    
    df = pd.read_csv(city_file)
    s = df['User Type'].value_counts().rename('Count')
    print(s)

    return s

def gender(city_file, time_period):
    '''Calculates the count of each gender for start time
    Args:
        Filename for a city's bikeshare data, Starting Time.
    Returns:
        (Integer) Count of Each Gender in the file.
    '''
    print('\n#### CALCULATING COUNTS OF GENDER FROM YOUR DATA ####\n')

    df = pd.read_csv(city_file)
    s = df['Gender'].value_counts().rename('Count')
    print(s)

    return s

def birth_years(city_file, time_period):
    '''Calculates the earliest, most recent, and most popular birth years
    Args:
        Filename for a city's bikeshare data, Starting Time.
    Returns:
        (Integer) Year Values (earliest, recent, most popular).
    '''

    print('\n#### CALCULATING BIRTH YEARS FROM YOUR DATA ####\n')
    
    df = pd.read_csv(city_file)
    
    s = df['Birth Year'].sort_values()
    print('The Earliest Birth Year is', int(s.iloc[0]))

    df = df.dropna(subset=['Birth Year'])
    s = df['Birth Year'].sort_values()
    print('The Recent Birth Year is', int(s.iloc[-1]))

    s = df['Birth Year'].value_counts().rename('Count')

    df = df.dropna(subset=['Birth Year'])
    s = df['Birth Year'].value_counts().idxmax()
    
    print('The Most Popular Year is: ',int(s))

    return s

def display_data():
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    while display == 'yes':
        if display == 'yes':
            city = get_city()
            df = pd.read_csv(city)
            print(df.head())
            display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
        else:
            break
                
    # TODO: handle raw input and complete function


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    print('\nCalculating the first statistic...')

    if time_period == 'none':
        start_time = time.time()

        popular_month(city, start_time)
        
        
        print("\nThat took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")

    if time_period == 'none' or time_period == 'month':
        start_time = time.time()

        popular_day(city, start_time)
        
        print("\nThat took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")    

    start_time = time.time()

    popular_hour(city, start_time)

    print("\nThat took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    trip_duration(city, start_time)

    print("\nThat took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    popular_stations(city, start_time)

    print("\nThat took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    popular_trip(city, start_time)

    print("\nThat took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    users(city, start_time)

    print("\nThat took %s seconds." % (time.time() - start_time))
    if city != washington:
        print("\nCalculating the next statistic...")
        start_time = time.time()
    
        gender(city, start_time)

        print("\nThat took %s seconds." % (time.time() - start_time))
    if city != washington:
        print("\nCalculating the next statistic...")
        start_time = time.time()
        birth_years(city, start_time)

        print("\nThat took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data()

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
