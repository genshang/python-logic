#Logic 

#Conditional statements gives us the ability to check conditions and make decisions based on the condition.

#In this assignment, you'll be asked to create conditional statements using if, elif and else. 

# Please commit and push your code after each completed exercise.

#1. Declare a variable named weather and assign it a string value of 'rain'. Next create a conditional statement that will check the weather and print 'Bring an umbrella' if weather equals 'rain'.
weather = "rain"
if weather == "rain":
    print("Bring an umbrella")
else:
    print("Suns out guns out!")

#2 Declare a variable named score and assign it a number value of 70. Next create a conditional statement that will check the score and print 'You pass!' if the score is 70 and above and print 'Study harder!' if the score is less than 70.
score = 70
if score >= 70:
    print("You Pass!")
elif score < 70:
    print("Study Harder!")

#3. Declare a variable named download_speed and assign it a data value of 50. Next create a conditional statement that will check the download speed and print the following based on the condition:
download_speed = 50

# <= 50: 'Basic Package'
# <=100: 'Premium Package'
# >100: 'Platinum Package'
if download_speed <= 50:
    print("Basic Package")
elif download_speed <= 100:
    print("Premium Package")
elif download_speed > 100:
    print("Platinum Package")


 #4 Function - check_password
 #Create a function named check_password which takes a parameter password.

def check_password(password):
    if password == "qwerty":
        print("true")
    else:
        print("false")

password_result = check_password("qwerty")


 #The function will return true if the password passed into the function is equal to 'qwerty'. Declare a variable named password_result and print your result.

#5 Function check_login
#Create a function named check_login which takes a parameter login.

#The function will print 'Login Success' if the login passed into the function is equal to 'DevLeague' and print 'Re-enter Login' if it doesn't.
def check_login(login):
    if login == "DevLeague":
        print("Login Success")
    else:
        print("Re-enter Login")

login_result = check_login("DevLeague")


#6 Function malware_type
#Create a function named malware_type which takes a parameter malware. 

#The function will print the following based on the following conditions:
#if malware is adware: 'Low Threat'
#if malware is virus: 'Do not share files'
#default message 'I hope you backed up your data'
def malware_type(malware):
    if malware == "adware":
        print("Low Threat")
    elif malware == "virus":
        print("Do not share files")
    else:
        print("I hope you backed up your data")

malware_result = malware_type("virus")


#7 Function encryption
#Create a function named encryption which takes a parameter keys.

#The function will print 'Encryption Success' if the keys passed into function has 5 characters and print 'Encryption Fail' if it doesn't.
def encryption(keys):
    if len(keys) == 5:
        print("Encryption Success")
    else:
        print("Encryption Fail")

password = encryption("Shang")

#8 Function even_cryptography
#Create a function named even_cryptography which takes a parameter num.

#The function will print 'Decryption Success' if the number passed into the function is even and print 'Decryption Fail' if it isn't.
def even_cryptography(num):
    if num % 2 == 0:
        print("Decryption Success")
    else:
        print("Decryption Fail")

cryptography = even_cryptography(102)

#9 Function bandwidth
#Declare a variable named mbps and assign it a list of 5 number values of your choosing. 

#Next, create a function named bandwidth which takes a parameter usage.
#The function will sum up the list of numbers and print the following messages based on the condition:

#if sum <= 50: 'Light User'
#if sum <= 100: 'Moderate User'
#if sum <=150: 'Multi Media User'
#if sum >150: 'Power User'
mbps = [1, 2, 3, 4, 88]
def bandwidth(usage):
    if sum(usage) <= 50:
        print("Light User")
    elif sum(usage) <= 100:
        print("Moderate User")
    elif sum(usage) <= 150: 
        print("Multi Media User")
    elif sum(usage) > 150:
        print("Power User")

how_much = bandwidth(mbps)

#10 Function ssh_keys
#Create a function named ssh_keys which takes two parameters public and private.

#The function will return false if public and private aren't equal and return true if they are equal.

#Declare a variable named ssh_connection and print your result.
def ssh_keys(public, private):
    if public == private:
        return True
    elif public != private:
        return False

ssh_connection = ssh_keys("public", "private")
print(ssh_connection)

#11 Function largest_num
#Create a function named largest_num which takes three parameters: num_1, num_2 and num_3.

#The function will find the largest number among any three numbers that are passed into the function. Declare a variable named large_num_result and print your results.
def largest_num(num_1, num_2, num_3):
    return (max(num_1, num_2, num_3))

large_num_result = largest_num(23, 44, 99)
print(large_num_result)

#12 Function pos_neg
#Create a function named pos_neg which takes a parameter num.

#The function will print 'Positive Number' if the number passed in is positive, print 'Zero' if the number is 0 and print 'Negative Number' for a negative number.
def pos_neg(num):
    if num == 0:
        print("Zero")
    elif num % 2 == 0:
        print("Positive Number")
    else:
        print("Negative Number")

numresult = pos_neg(0)

#13 Function name_caps
#Create a function named name_caps which takes a parameter name.

#The function will check the number of characters in the name that is passed into the function and do the following:

#if characters in name <=5: capitalize the first letter in the name
#if characters in name <=10: captialize all the letters in the name
#if characters in name >10: leave the letters as is

#Print your results
def name_caps(name):
    if len(name) <= 5:
        print(name.capitalize())
    elif len(name) <= 10:
        print(name.upper())
    elif len(name) >10:
        print(name)

my_name = name_caps("shangounchained")


#14 Function leap_year

#A leap year occurs every four years. Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but are leap years if they are exactly divisible by 400.

#Create a function named leap_year which takes a parameter year.
#The function will print 'The year x is a leap year.' where x is the year value that is passed into the function and print 'The year x is not a leap year.' if it isn't a leap year.
def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("The year " + str(year) + " is a leap year")
    else:
        print("The year " + str(year) + " is not a leap year")
    
leap = leap_year(2004)

