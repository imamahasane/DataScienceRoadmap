book = {}

book['imam'] = {
    'name': 'Imam Ahasan',
    'age': 23,
    'Address': 'mirpur-1'
}

book['naima'] = {
    'name': 'Naima Ahasan',
    'age': 30,
    'Address': 'mirpur-2'
}

book['samiul'] = {
    'name': 'Samiul Ahasan',
    'age': 17,
    'Address': 'mirpur-12'
}

import json

a = json.dumps(book)
# print(a)


with open ("/Users/imamahasan/DataScience/1_Python/book.txt", 'w') as f:
    f.write(a)

