PLACEHOLDERS = '[name]'
with open('/Users/matheshanandan/Downloads/Mail Merge Project Start/Input/Letters/starting_letter.txt') as letter:
    letter_content = letter.read()




with open('/Users/matheshanandan/Downloads/Mail Merge Project Start/Input/Names/invited_names.txt') as names:
    name_list = names.readlines()
    for name in name_list:
        stripped_name = name.strip()
        actual_names = letter_content.replace(PLACEHOLDERS, stripped_name)
        print(actual_names)
        with open(f'/Users/matheshanandan/Downloads/Mail Merge Project Start/Output/ReadyToSend/letter_for{stripped_name}.docx', mode = 'w') as completed_letter:
            completed_letter.write(actual_names)





