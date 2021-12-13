# CMT309 - CMT314 2021-2022 Coursework Q2 Test Code
# Oktay Karakus, PhD
# ************************************************************************************
def pluralize(word):
    '''
    1) Please copy and pass your codes for pluralize() function below.
    2) Do required changes in function definition for the arguments if needed.
    '''
    pn = read_file()
    x = ['empty_string', 'proper_noun', 'already_in_plural', 'success']
    vowel = ['a', 'e', 'i', 'o', 'u']
    if word == '':
      re = {'plural': '', 'status': x[0]}
    elif word[-1] == 's': 
      re = {'plural': word, 'status': x[2]}
    elif str.lower(word) in pn:
      re = {'plural': word, 'status': x[1]}
    elif word[-1] in vowel:
      re = {'plural': word + 's', 'status': x[3]}
    elif word[-1] == 'y':
      re = {'plural': word[:-1] + 'ies', 'status': x[3]}
    elif word[-1] == 'f':
      re = {'plural': word[:-1] + 'ves', 'status': x[3]}
    elif word[-2:] == 'sh' or word[-2:] == 'ch' or word[-1] == 'z':
      re = {'plural': word + 'es', 'status': x[3]}
    else:
      re = {'plural': word + 's', 'status': x[3]}
    return re

def read_file():
    file = open('proper_nouns.txt', mode="r", encoding="utf-8")
    con = file.readlines()
    pn = list((i.replace('\n', '').strip()) for i in con) 
    return pn



