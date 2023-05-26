def recomm_streams(input_subjects):
    Science = ['Chemistry', 'Mathematics', 'English','Hindi']
    ScienceOptional = ['Biology', 'Computer Science', 'Informatics Practices', 'Biotechnology', 'Engineering Graphics', 'Multimedia and Web Technology', 'Psychology']
    Commerce = ['Accountancy', 'Economics', 'English','Hindi']
    CommerceOptional = ['Mathematics', 'Informatics Practices', 'Computer Science', 'Entrepreneurship', 'Multimedia and Web Technology', 'Psychology']
    Humanities = ['English','Hindi','History', 'Political Science', 'Sociology', 'Psychology', 'Economics', 'Mathematics', 'Physical Education', 'Multimedia and Web Technology']

    recommended_subjects = []
    if 'Business Studies' in input_subjects:
        recommended_subjects = []
        Commerce = [item for item in Commerce if item not in input_subjects]
        CommerceOptional = [item for item in CommerceOptional if item not in input_subjects]
        n = len(Commerce)
        recommended_subjects.extend(Commerce)
        recommended_subjects.extend(CommerceOptional[:6 - n])
        print('Recommended Subjects:', recommended_subjects)
    elif 'Geography' in input_subjects:
        recommended_subjects = []
        Humanities = [item for item in Humanities if item not in input_subjects]
        recommended_subjects.extend(Humanities[:6])
        print('Recommended Subjects:', recommended_subjects)
    elif 'Physics' in input_subjects:
        recommended_subjects = []
        Science = [item for item in Science if item not in input_subjects]
        ScienceOptional = [item for item in ScienceOptional if item not in input_subjects]
        n = len(Science)
        recommended_subjects.extend(Science)
        recommended_subjects.extend(ScienceOptional[:6 - n])
        print('Recommended Subjects:', recommended_subjects)
    else:
        initial_list=['Business Studies', 'Geography', 'English', 'Hindi', 'Physics']
        print('Recommended Subjects:',initial_list )

input_subjects = ['Business Studies']
test_cases = ['Accountancy', 'Economics', 'Mathematics']
# test_cases=['History', 'Political Science', 'Sociology','Economics']
# test_cases=['Chemistry', 'Mathematics', 'English','Biology']
recomm_streams(input_subjects)
for subject in test_cases:
    input_subjects.append(subject)
    recomm_streams(input_subjects)
