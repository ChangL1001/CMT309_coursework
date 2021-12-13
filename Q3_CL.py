# CMT309 - 2021-2022 Coursework Q3 Test Code
# Oktay Karakus, PhD
# ************************************************************************************
import re


def function_renamer(code):
    '''
    1) Please copy and pass your codes for function_renamer() function below.
    2) Do required changes in function definition for the arguments if needed.
    '''
    func_names = re.findall('def (.*)\(', code)
    d = dict()
    new_code = code
    for func_name in func_names:
        func_hash = hash(func_name)
        under = 0
        camelcase = ''
        all_cap = func_name.upper()
        for word in func_name.split('_'):
            if word == '' and under == 0:
                camelcase += '_'
            if word != '':
                under = 1
                word = word.replace(word[0], word[0].upper()) 
                camelcase += word
        new_code = new_code.replace(func_name, camelcase)
        d[func_name] = {'hash': func_hash, 'camelcase': camelcase, 'allcaps': all_cap}
    return (d, new_code)