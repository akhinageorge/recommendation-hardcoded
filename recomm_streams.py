all_streams = [
    ('Physics', 'Chemistry', 'Biology', 'Mathematics', 'English'),
    ('Physics', 'Chemistry', 'Mathematics', 'Computer Science', 'English'),
    ('Physics', 'Chemistry', 'Mathematics', 'Physical Education', 'English'),
    ('Physics', 'Chemistry', 'Mathematics', 'Economics', 'English'),
    ('Physics', 'Chemistry', 'Mathematics', 'Informatics Practices', 'English'),
    ('Physics', 'Chemistry', 'Mathematics', 'Engineering Graphics', 'English'),
    ('Physics', 'Chemistry', 'Mathematics', 'Fine Arts', 'English'),
    ('Physics', 'Chemistry', 'Mathematics', 'Music', 'English'),
    ('Physics', 'Chemistry', 'Mathematics', 'Psychology', 'English'),
    ('Physics', 'Chemistry', 'Mathematics', 'Home Science', 'English'),
    ('Physics', 'Chemistry', 'Biology', 'Biotechnology', 'English'),
    ('Physics', 'Chemistry', 'Biology', 'Physical Education', 'English'),
    ('Physics', 'Chemistry', 'Biology', 'Physical Education', 'English'),
    ('Physics', 'Chemistry', 'Biology', 'Psychology', 'English'),
    ('Physics', 'Chemistry', 'Biology', 'Sociology', 'English'),
    ('Physics', 'Chemistry', 'Biology', 'Economics', 'English'),
    ('Physics', 'Chemistry', 'Biology', 'Informatics Practices', 'English'),
    ('Physics', 'Chemistry', 'Biology', 'Fine Arts', 'English'),
    ('Physics', 'Chemistry', 'Biology', 'Music', 'English'),
    ('Physics', 'Chemistry', 'Biology', 'Home Science', 'English'),
    ('Physics', 'Chemistry', 'Biology', 'Entrepreneurship', 'English'),
    ('Accountancy', 'Business Studies', 'Economics', 'English', 'Mathematics'),
    ('Accountancy', 'Business Studies', 'Economics', 'English', 'Informatics Practices'),
    ('Accountancy', 'Business Studies', 'Economics', 'English', 'Physical Education'),
    ('Accountancy', 'Business Studies', 'Economics', 'English', 'Entrepreneurship'),
    ('Accountancy', 'Business Studies', 'Economics', 'English', 'Computer Science'),
    ('Accountancy', 'Business Studies', 'Economics', 'English', 'Psychology'),
    ('Accountancy', 'Business Studies', 'Economics', 'English', 'Fine Arts'),
    ('Accountancy', 'Business Studies', 'Economics', 'English', 'Music'),
    ('Accountancy', 'Business Studies', 'Economics', 'English', 'Home Science'),
    ('Accountancy', 'Business Studies', 'Economics', 'English', 'Sociology'),
    ('Political Science', 'History', 'Geography', 'English', 'Sociology'),
    ('Political Science', 'History', 'Geography', 'English', 'Economics'),
    ('Political Science', 'History', 'Geography', 'English', 'Psychology'),
    ('Political Science', 'History', 'Geography', 'English', 'Fine Arts'),
    ('Political Science', 'History', 'Geography', 'English', 'Music'),
    ('Political Science', 'History', 'Geography', 'English', 'Home Science'),
    ('Political Science', 'History', 'Geography', 'English', 'Legal Studies'),
    ('Political Science', 'History', 'Geography', 'English', 'Mathematics'),
    ('Political Science', 'History', 'Geography', 'English', 'Physical Education'),
    ('Political Science', 'History', 'Geography', 'English', 'Philosophy'),
    ('English', 'History', 'Political Science', 'Sociology', 'Economics'),
    ('English', 'History', 'Political Science', 'Sociology', 'Psychology'),
    ('English', 'History', 'Political Science', 'Sociology', 'Fine Arts'),
    ('English', 'History', 'Political Science', 'Sociology', 'Music'),
    ('English', 'History', 'Political Science', 'Sociology', 'Home Science'),
    ('English', 'History', 'Political Science', 'Sociology', 'Legal Studies'),
    ('English', 'History', 'Political Science', 'Sociology', 'Mathematics'),
    ('English', 'History', 'Political Science', 'Sociology', 'Physical Education'),
    ('English', 'History', 'Political Science', 'Sociology', 'Philosophy'),
    ('English', 'History', 'Political Science', 'Economics', 'Entrepreneurship')
]

def recomm_streams(input_subjects):
    from collections import Counter
    stream_identify = {stream for stream in all_streams if all(subject in stream for subject in input_subjects)}
    all_subjects = Counter(item for stream in stream_identify for item in stream if item not in input_subjects)
    recommended_subjects = sorted(all_subjects, key=lambda x: all_subjects[x], reverse=True)[:6]
    print(recommended_subjects)

input_subjects = ['Chemistry']
recomm_streams(input_subjects)

# test_cases=['Business Studies','Economics','English']
# test_cases=['Political Science', 'Geography','English']
test_cases=['Physics', 'Mathematics', 'English']
for subject in test_cases:
    input_subjects.append(subject)
    recomm_streams(input_subjects)
