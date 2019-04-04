def is_pangram(sentence):
    string = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for i in sentence:
        if i in alphabet:
            return True
        else:
            return False   
        

