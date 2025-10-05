# Dictionary of country codes
country_code = {
    'India': '0091'
    'Australia': '0025'
    'Nepal': '00977'
}
# Taking input from the user
country = input("Enter your country name: ")
# Checking if the country exists in dictionary
if country in country_code:
    print(f"The country code for {country} is {country_code[country]}")
else:
    print("Sorry,country not found in list")
    