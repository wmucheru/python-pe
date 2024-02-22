import pickle

students = {
    "Student 1": {
        "Name": "Alice",
        "Age": 10,
        "Grade": 4,
    },
    "Student 2": {"Name": "Bob", "Age": 11, "Grade": 5},
    "Student 3": {"Name": "Elena", "Age": 14, "Grade": 8},
}

print(type(students))


def read_write_json():
    filename = "students.json"

    with open(filename, "w") as data:
        print("Writing data:")
        data.write(str(students))

    with open(filename, "r") as data:
        print("Reading data:")
        for student in students:
            print(student)


def read_write_pickle():
    filename = "students.pkl"

    with open(filename, "wb") as file:
        pickle.dump(students, file)

    with open(filename, "rb") as file:
        data = pickle.load(file)
        print(data)


read_write_pickle()
