def enrollment_stats(universities):
    # Extracting the number of students and tuition fees from the list of lists
    student_enrollments = [university[1] for university in universities]
    tuition_fees = [university[2] for university in universities]
    return student_enrollments, tuition_fees

def mean(values):
    # Calculate the mean of a list of values
    return sum(values) / len(values)

def median(values):
    # Calculate the median of a list of values
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:
        return sorted_values[mid]

# List of universities with their enrollment and tuition fees
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

# Get enrollment numbers and tuition fees using the enrollment_stats function
student_enrollments, tuition_fees = enrollment_stats(universities)

# Calculate total number of students and total tuition fees
total_students = sum(student_enrollments)
total_tuition = sum(tuition_fees)

# Calculate mean and median for the number of students
mean_students = mean(student_enrollments)
median_students = median(student_enrollments)

# Calculate mean and median for tuition fees
mean_tuition = mean(tuition_fees)
median_tuition = median(tuition_fees)

# Output the results
print(f"Total number of students: {total_students}")
print(f"Total tuition fees: ${total_tuition}")
print(f"Mean number of students: {mean_students:.2f}")
print(f"Median number of students: {median_students}")
print(f"Mean tuition fees: ${mean_tuition:.2f}")
print(f"Median tuition fees: ${median_tuition:.2f}")