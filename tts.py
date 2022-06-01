import os
import librosa
import soundfile as sf

def tts_output(text, base_voice = False):
    f = open("text.txt", "w")
    f.write(text)
    f.close()
    cmd = 'text2wave text.txt -o ./static/text.wav -eval "(voice_cmu_us_ksp_cg)"'
    os.system(cmd)
    if not base_voice:
        return
    


    samples, sr = librosa.load('./static/text.wav',sr=None)

    def manipulate(data, sampling_rate, pitch_factor):
        return librosa.effects.pitch_shift(data, sampling_rate, pitch_factor)

    normal_shift = manipulate(samples, sr, -1)

    sf.write('./static/base_voice.wav', normal_shift, sr, subtype='PCM_24')
