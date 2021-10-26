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

