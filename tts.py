import os

def tts_output(text):
    f = open("text.txt", "w")
    f.write(text)
    f.close()
    cmd = 'text2wave text.txt -o ./static/text.wav -eval "(voice_cmu_us_ksp_cg)"'
    os.system(cmd)

    return