import json
import random
from faker import Faker


countries_list = []
campuses_list = []
countries = open("countries.txt", "r")
campuses = open("campuses.txt","r")

for country in countries:
    countries_list.append(country)
for campus in campuses:
    campuses_list.append(campus)

majors = ['Sciences and Engineering', 
        'Social Sciences',
        'Arts and Humanities',
        'Natural Sciences',
        'Health Sciences',
        'Business and Economics',
        'Education and Teaching',
        'Fine and Applied Arts',
        'Communications and Media',
        'Law and Legal Studies']
education_levels = ['Freshman','Sophomore','Junior','Senior','Master\'s','PhD']
# Initialize Faker
fake = Faker()

# Helper function to create a student's details
def create_student():
    return [
        random.choice(campuses_list).strip(),
        random.choice(countries_list).strip(),
        random.choice(majors).strip(),
        random.choice(education_levels).strip()
    ]
print(create_student())

# Number of records to generate
num_students = 100  # You can change this to generate more or fewer students

# Generate student data


for _ in range(num_students):
    student_data = {}
    name = fake.name()  # Generate a random name
    student_info = create_student()  # Generate random student details
    # Store the information as a string representation of a list
    student_data[name] = json.dumps(student_info)
    print(student_data)

# Display the generated data
