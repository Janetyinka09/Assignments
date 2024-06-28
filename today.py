users_year = int(input("please enter your year of birth")) 
preferred_year_of_birth = int(2024 - users_year)
if users_year == 1999:
    print("You've been granted access to enter this website")  
elif users_year < 1998:
    print("Oops, seems like you're older than the required age...Try going back in time and try this again to work")
else:
    print("Sorry, you're not allowed to enter this website") 





