"""
This is a program that will take a list formatted like so:
	Individual vs. Individual: Deponent Name ##/##/##, 
and return a CSV list with the following headers:
Case Name | Deponent Name | Date of Deposition
"""

def line_read(file):
	# a method for reading each line in the file and returning a tuple of case name, :, deponent and date
	sep_list = []
	with(open(file)) as input:
		for line in input:
			sep_list.append(line.partition(":"))
			# sep_list is now a list of tuples with the following structure:
			# (case name, ":", Name and date of deposition)
	return sep_list
	
	
	
def date_separate(string_with_date):
	# takes a string with a date ##/##/## OR #/#/## and returns only that date as a string
	date_character_list = []
	month = []
	day = []
	year = []
	slash_number = 0
	for char in string_with_date:
		if char == "/":
			slash_number += 1
		elif slash_number == 0 and char.isdigit() == True:
			month.append(char)
		elif slash_number == 1 and char.isdigit() == True:
			day.append(char)
		elif slash_number == 2 and char.isdigit() == True:
			year.append(char)
	# year string fix
	year = year[:2] 
	# truncate year to only two digits
	month_str = ''.join(month)
	day_str = ''.join(day)
	year_str = ''.join(year)
	if month_str and day_str and year_str is not True:
		return month_str + "/" + day_str + "/" + year_str
	# returns the date as MM/DD/YY
	else:
		return "##/##/##"
	# returns an "empty date" -- ##/##/## if no date is found (you can quickly check the CSV for missing dates this way)

def get_sep_list(file):	
	sep_list = []
	with(open(file)) as input:
		for line in input:
			sep_list.append(line.partition(":"))
			# sep_list is now a list of tuples with the following structure:
			# (case name, ":", Name and date of deposition)
	return sep_list
	
def write_row(file):
	for line in get_sep_list(file):
		(case_name, semicolon, name_depodate) = line
		# call get_sep_list on the file, and take each line from that file (a tuple)
		# create three variables, "case name" and "name_depodate" are the two important ones
		names_split = [x for x in name_depodate.split(",")]
		# in the third item of each tuple ("names_split") we split into a list of strings "firstname lastname ##/##/##"
		for name in names_split:
		# for each name in the list "names_split"
			date = date_separate(name)
			# get the date
			name = name.split()
			# list of all characters in name
			name_char_list = []
			for char in name:
				if char is not "/" and char.isdigit() == False and char is not "\n":
					name_char_list.append(char)
			
			# there are problems with this code, I'm not sure what.
			'''
			if name_char_list[0] == " ":
				del name_char_list[0]
			# remove the first char in the list (if a space)
			'''
			
			if len(name_char_list) > 1:
				if name_char_list[len(name_char_list) - 1] == " ":
					del name_char_list[len(name_char_list) - 1]
			# remove last char in the list (if a space)
			
			name = ''.join(name_char_list)
			
			
			print case_name + "," + name + "," + date + "\n"
