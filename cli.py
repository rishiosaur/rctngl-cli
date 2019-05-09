from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
import os

def question():
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
            prompt({
                'type':'input',
                'message':'Please enter the path to your variable file',
                'name':'path'
            })
            
    else:
        print("Creating project...")
question()