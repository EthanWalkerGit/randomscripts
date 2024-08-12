requiredCourses = [
    # Two other Computer Science courses (excluding COMP-XXX7)
    "COMP-1000", "COMP-1400", "COMP-1410", "COMP-2120", "COMP-2540", "COMP-2560", 
    "COMP-2650", "COMP-2660", "COMP-3150", "COMP-3220", "COMP-3300", "COMP-3340", 
    "COMP-3400", "COMP-3670", "COMP-4990", "COMP-4150", "COMP-4200", "COMP-4220", 
    "COMP-4250"
]

requiredMath = [
    "MATH-1260", "MATH-1760", "STAT-2910"
]

requiredElectives = [
    # As well as thirteen other courses from any area of study
    "SOSC-1XXX", "SPAN-1020"
]

requiredTaken = [
    "COMP-1000", "COMP-1400", "COMP-1410", "COMP-2120", "COMP-2540", "COMP-2560", 
    "COMP-2650", "COMP-3300", "COMP-3670"
]

electivesTaken = [
    "SPAN-1020", "SOSC-1XXX", "COMP-1047", "COMP-2057", "COMP-2707", "COMP-2750", "COMP-3057"
]

mathTaken = [
    "MATH-1260"
]

def match_courses(required, taken):
    matched = [course for course in required if course in taken]
    missing = [course for course in required if course not in taken]
    return matched, missing

# Match required courses
matched_required, missing_required = match_courses(requiredCourses, requiredTaken)

# Match required math courses
matched_math, missing_math = match_courses(requiredMath, mathTaken)

# Match required electives
matched_electives, missing_electives = match_courses(requiredElectives, electivesTaken)

print("Matched Required Courses:", matched_required)
print("Missing Required Courses:", missing_required)
print(" ")
print("Matched Math Courses:", matched_math)
print("Missing Math Courses:", missing_math)

#print("Matched Elective Courses:", matched_electives)
#print("Missing Elective Courses:", missing_electives)