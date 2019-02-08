from os import path, chdir
from subprocess import Popen, PIPE
from pyperclip import copy

try:
    while True:
        print("Please enter your local git repository path")
        print(r"Example: C:\Users\Documents\REPO ")
        local_git_repo_name = input(">>> ")

        if path.isdir(local_git_repo_name):
            break

        print(r"folder in not exist, please try again")

    date_after = input("Date After (2019-01-08) >>> ")
    date_after = '--after="' + date_after + ' 00:00"'
    date_before = input("Date Before (2019-01-09) >>> ")
    date_before = '--before="' + date_before + ' 00:00"'
    key_word = input("Key Word >>> ")

    chdir(local_git_repo_name)

    cmd = 'git log --pretty=format:"%h | %s" ' + date_after + ' ' + date_before

    print('\n' + cmd + '\n')
    pipe = Popen(cmd, shell=True, stdout=PIPE)
    text = str(pipe.communicate()[0])

    if text.startswith("b'") and text.endswith("'"):
        text = text[2:len(text)-1]

    text_list = str(text).split('\\n')

    result_list = []

    if len(key_word) > 0:
        for line in text_list:
            if key_word in line:
                print(line)
                result_list.append(line)
    else:
        for line in text_list:
            print(line)
            result_list.append(line)

    result_list.reverse()

    result = ''
    for i in result_list:
        result = i.split(' | ')[1] + '; ' + result

    print("\n" + f"len of result list is {len(result_list)}" + "\n")
    print(result)
    copy(result)
    print("result copied to buffer...")
    input("press enter for exit")

except Exception as error:
    print('ERROR:' + error.__str__())
    input("Something went wrong... \n press enter for exit")
