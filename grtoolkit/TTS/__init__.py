#Code works; not optimized for grtoolkit library
import subprocess, os

def text2speech(text, audio_dest_path, play=False, 
                balcon_voice="ScanSoft Daniel_Full_22kHz", 
                balcon_location = r"C:\Users\Gabriel\Downloads\balcon\balcon.exe"):
    """Text to speech. Outputs .wav files"""
    command = f'{balcon_location} -t "{text}" -n {balcon_voice} -w "{audio_dest_path}"' 
    process = subprocess.call(command, shell=True)
    if play:
        os.startfile(audio_dest_path)

if __name__ == "__main__":
    text = """Hello Gabriel, it is a nice day today!"""
    dest = r"C:\Users\Gabriel\Git Repositories\YTAutomation\VoiceSynth\life.wav"
    text2speech(text, dest, play=True)
