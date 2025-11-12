# DICTIONARY
# KEY : VALUE

StudentInformation = {"Name" : "Camumut, Kirk Claret S.", "Age" : 17, "Citizenship" : "Filipino", "Date Of Birth" : "November 02, 2007", "Gender" : "Female"}

print(StudentInformation)
print(StudentInformation["Age"])
print(StudentInformation["Date Of Birth"])
print(StudentInformation["Name"])

StudentInformation["Name"] = "Kirik Camutmut"
print(StudentInformation)

StudentInformation.update({"Section" : "1-4"})
print(StudentInformation)


# Nested Dictionary

MyInfo = {
    "Name" : {
        "First Name" : "Kirk Claret",
        "Middle Name" : "Sistona",
        "Last Name" : "Camumut"
    },
    "Age" : 17,
    "Gender" : "Female",
    "Hobbies": [
        "Chess",
        "Drawing",
        "Writing"
    ]
}

print(MyInfo)
print(MyInfo["Age"])
print(MyInfo["Name"]["First Name"])
print(MyInfo["Name"]["Middle Name"])
print(MyInfo["Hobbies"][2])