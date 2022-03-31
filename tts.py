import os

def tts_output(text):
    os.system('echo {0}'.format(text))
    return