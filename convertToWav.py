import moviepy.editor as mp

convertVideoPath = r"convert.wav"

def convert(sourceVideoPath):
    clip = mp.VideoFileClip(sourceVideoPath)
    clip.audio.write_audiofile(convertVideoPath)

