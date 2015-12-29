"""
The following program creates two tables in Sqlite (one containing a list of cities and states, the other
	containing weather information by city), joins them, imports them to a Python dataframe, and then prints
	the cities whose hottest months are in July.

Written by: David Lindberg
Date: December 28, 2015
"""

# Import necessary packages
import sqlite3 as lite
import pandas as pd
import sys

print('The Weather Machine - List the cities whose warmest or coldest months are a specified month \n\n')

# Store an integer 1 or 2 representing the warmest or coldest month
print('Are you interested in seeing cities for the warmest or coldest month? \n 1 for warmest \n 2 for coldest \n')
hot_cold_check = True
while hot_cold_check:
	try:
		hot_cold = int(raw_input('Type 1 or 2: '))
		if hot_cold != 1 and hot_cold != 2:
			print("\nWARNING: You must enter a 1 or a 2\n")
		else:
			hot_cold_check = False
	except ValueError:
		print("\nWARNING: You must enter a 1 or a 2\n")

print("\n")

# Store an integer between 1 and 12 representing the month
print('\nWhich month are you interested in? \n 1 for January \n 2 for February \n 3 for March \n 4 for April \n 5 for May \n 6 for June \n 7 for July \n 8 for August \n 9 for September \n 10 for October \n 11 for December \n 12 for December \n')
month_check = True
while month_check:
	try:
		month = int(raw_input('Type a integer between 1 and 12: '))
		if month < 1 or month > 12:
			print("\nWARNING: You must enter an integer between 1 and 12\n")
		else:
			month_check = False
	except ValueError:
		print("\nWARNING: You must enter an integer between 1 and 12\n")

print('\n')

# Define a tuple of tuples containing city and state information
cities = (	('New York City', 'NY'),
			('Boston', 'MA'),
			('Chicago', 'IL'),
			('Miami', 'FL'),
			('Dallas', 'TX'),
			('Seattle', 'WA'),
			('Portland', 'OR'),
			('San Francisco', 'CA'),
			('Los Angeles', 'CA'),
			('Washington', 'DC'),
			('Houston', 'TX'),
			('Las Vegas', 'NV'),
			('Atlanta', 'GA')
			)

# Define a tuple of tuples containing city weather data 
weather = (	('New York City', 2013, 'July', 'January', 62),
			('Boston', 2013, 'July', 'January', 59),
			('Chicago', 2013, 'July', 'January', 59),
			('Miami', 2013, 'August', 'January', 84),
			('Dallas', 2013, 'July', 'January', 77),
			('Seattle', 2013, 'July', 'January', 61),
			('Portland', 2013, 'July', 'December', 63),
			('San Francisco', 2013, 'September', 'December', 64),
			('Los Angeles', 2013, 'September', 'December', 75),
			('Washington', 2013, 'July', 'January', 65),
			('Houston', 2013, 'July', 'January', 80),
			('Las Vegas', 2013, 'July', 'December', 80),
			('Atlanta', 2013, 'July', 'January', 70)
			)

# Define a tuple of tuples containing the month number
month_number = ( 	('January', 1),
					('February', 2),
					('March', 3),
					('April', 4),
					('May', 5),
					('June', 6),
					('July', 7),
					('August', 8),
					('September', 9),
					('October', 10),
					('November', 11),
					('December', 12)
					)					
			

# Open a connection
con = lite.connect('getting_started.db')

# Execute Sqlite within connection
with con:    
	
	# Create a cursor
	cur = con.cursor()

	# Drop the tables if they already exist
	cur.execute("DROP TABLE IF EXISTS cities")
	cur.execute("DROP TABLE IF EXISTS weather")
	cur.execute("DROP TABLE IF EXISTS month_number")
	
	# Create the cities and weather tables
	cur.execute("CREATE TABLE cities (name text, state text)")
	cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)")
	cur.execute("CREATE TABLE month_number (month text, number integer)")
	
	# Insert tuple data into the cities and weather Sqlite tables
	cur.executemany("INSERT INTO cities VALUES(?, ?)", cities)
	cur.executemany("INSERT INTO weather VALUES(?, ?, ?, ?, ?)", weather)
	cur.executemany("INSERT INTO month_number VALUES(?, ?)", month_number)
	
	# Join the cities and weather tables together
	cur.execute("SELECT * FROM weather INNER JOIN cities ON name = city INNER JOIN month_number mn1 ON mn1.month = warm_month INNER JOIN month_number mn2 ON mn2.month = cold_month")
	
	# Get all the rows of the joined tables
	rows = cur.fetchall()	
	
	# Get the column names
	cols = [desc[0] for desc in cur.description]
	cols[7:11] = ['month1', 'month1_num', 'month2', 'month2_num']
	
	# Define a data frame in Python with the data generated from Sqlite
	df = pd.DataFrame(rows, columns = cols)
	
	# Initialize the output string based on whether warmest or coldest was selected
	if hot_cold == 1:
		city_list = "The cities that are warmest in " 
	else: 
		city_list = "The cities that are coldest in "
	
	city_list += month_number[month - 1][0] + " are: "

	# Start a count the number of cities
	city_count = 0
	
	# Iterate through all the rows of the data frame appending cities to the output string
	# For the warmest month
	if hot_cold == 1:
		
		for i in df.index:
			
			# Only append to the output string if a city matches the warmest month selected
			if df.loc[i, 'month1_num'] == month:
			
				# Append city to the output string
				city_list += df.loc[i, 'city'] + ", " + df.loc[i, 'state'] + ", "
				city_count += 1

	# For the coldest month
	else:
		for i in df.index:
			
			# Only append to the output string if a city matches the coldest month selected
			if df.loc[i, 'month2_num'] == month:
			
				# Append city to the output string
				city_list += df.loc[i, 'city'] + ", " + df.loc[i, 'state'] + ", "
				city_count += 1

# Close the connection
con.close()

# Remove ", " from the end, or specify "None" if no matches
if city_count > 0:
	city_list = city_list[:(len(city_list)-2)]
else:
	city_list += "None"

# Print to the terminal
print(city_list + "\n")
