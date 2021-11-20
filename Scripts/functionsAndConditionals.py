def mean(value):
    if type(value) == dict:
        theMean = sum(value.values())/len(value)
    else:
        theMean = sum(value) / len(value)
    return theMean

mondayTemperatures = [8.8,9.1,9.9]
studentGrades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
print(mean(studentGrades))
print(mean(mondayTemperatures))



##Exercise - Password controller##
def password(pass1):
    if len(pass1) >= 8:
        return True
    else:
        return False
##Exercise - Password controller##


##Exercise - Temperature controller##
def temperatureCalculate(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"
##Exercise - Temperature controller##


##Exercise Elif - Temperature controller##
def temperatureCalc(temperature):
    if temperature > 25:
        return "Hot"
    elif temperature >= 15 and temperature <= 25:
        return "Warm"
    else:
        return "Cold"
##Exercise Elif - Temperature controller##


## User Input ##
user_input = float(input("Enter the temperature:"))
print (temperatureCalc(user_input))
## User Input ##



## String formating ##
name = input("Enter your name: ")
surname = input("Enter your surname: ")
message = "Hello %s %s" % (name, surname)
print(message)
message = f"Hello {name} {surname}"
print(message)
## String formating ##