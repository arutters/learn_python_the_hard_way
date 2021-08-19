directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'chris', 'princess', 'cabinet']

def scan(input):
    words = input.split()
    operation = ''
    sentence = []

    for word in words:
        if word.lower() in directions:
            operation = 'direction'
        elif word.lower() in verbs:
            operation = 'verb'
        elif word.lower() in stop_words:
            operation = 'stop'
        elif word.lower() in nouns:
            operation = 'noun'
        elif convert_number(word):
            operation = 'number'
            word = convert_number(word)
        else:
            operation = 'error'

        sentence.append((operation, word ))  

    return sentence

def convert_number(word):
    try:
        return int(word)
    except ValueError:
        return None

# another way to 'convert_number' is to use the below instead of def a new function. This is used in the longer "spelled out" code
    # for word in words:
        # if word.isdigit():
        #     word = int(word)
        #     sentence.append(('number', word))
