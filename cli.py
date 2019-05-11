from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
import os
from pyfiglet import Figlet
import tempfile

def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

def question():
    print(Figlet(font='epic').renderText('RCTNGL'))
    style = style_from_dict({
        Token.Separator: '#0091ea',
        Token.QuestionMark: '#76ff03',
        Token.Selected: '#cc5454',  # default
        Token.Pointer: '#ffab00 bold',
        Token.Answer: '#d500f9',
    })


    questions = [
        {
            'type':'input',
            'message':'Name of Project',
            'name':'name'
        },
        {
            'type': 'checkbox',
            'message': 'Load Modules',
            'name': 'modules',
            'choices': [
                Separator('Essentials'),
                {
                    'name': 'Spacing',
                    'checked': True
                },
                {
                    'name': 'Colour',
                    'checked': True
                },
                Separator('= Additional Styling ='),
                {
                    'name':'Shadows'
                },
                {
                    'name':'Fonts'
                }
            ]
        },
        {
            'type': 'list',
            'name': 'template',
            'message': 'Which template would you like to use?',
            'choices': ['Jekyll','React','Static','None']
        },
        {
            'type':'confirm',
            'name':'vars',
            'message':'Would you like to modify the variables?',
            'default':False
        }
    ]

    answers1 = prompt(questions,style=style)
    if answers1.get('vars'):
        answers2 = prompt({'type':'confirm','name':'editorvariables','message':'Would you like to use a custom file to generate the variables?','default':True},style=style)
        if answers2.get('editorvariables'):
            path = prompt({
                'type':'input',
                'message':'Please enter the path to your variable file',
                'name':'path'
            })
        else:
            path = prompt({
                'type':'editor',
                'message':'Please create your JSON file in this editor.',
                'name':'json'
            })
    try:
        os.makedirs(answers1.get('name'))
    except OSError:  
        prRed ("Creation of the directory %s failed" % answers1.get('name'))
    else:  
        prCyan ("Successfully created the directory %s" % answers1.get('name'))

question()
