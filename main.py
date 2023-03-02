from art import logo
from classes import *
import os
from datetime import datetime

partlist = []

party = None

while party != 'exit':
    os.system('clear')

    print(logo)
    entrydict = { }
    name = input('Enter your name:\n')
    while len(name) < 1:
        name = input('Enter your name:\n')
    wish = input('Enter your wish:\n')
    if len(wish) < 1:
        wish = 'Nothing in particular'

    mail = input('Enter your email address:\n')
    while '@' not in mail:
        mail = input('Enter your email address:\n')
    entrydict['name'] = name
    entrydict['wish'] = wish
    entrydict['mail'] = mail
    partlist.append(entrydict)
    party = input('Is there someone else to take part?\n'
                  'Type "exit" to conclude secret santa\n'
                  'and get the output\n'
                  'Or just press <ENTER>')

if len(partlist) < 3:
    print("Secret Santa doesn't make much sense with less than three people!\n"
          "***Quitting***")
else:

    # List for objects
    santalist = []

    for i in partlist:
        p = Participant(name=i[ 'name' ], mailadresse=i[ 'mail' ], wish=i['wish'])
        santalist.append(p)

    st = Santamat(santalist)
    result = st.getsantas()
    # resultlist for file
    resultlist = []
    with open(file=f'secret_santa_result_{datetime.now()}', mode='w') as target:

        for c, e in enumerate(result):
            out = f'{c} {e.name} gifts {result[ e ].name}, {result[ e ].name}s wish is: {result[ e ].wish}'
            print(out)
            resultlist.append(out)
            target.write(out)
            target.write('\n')

    # print(resultlist)