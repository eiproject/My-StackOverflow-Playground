import ffmpeg

inputfile = ffmpeg.input("example.mp3")
iAudio = inputfile.audio
stream = ffmpeg.output(iAudio, "example.ogg")
ffmpeg.run(stream)