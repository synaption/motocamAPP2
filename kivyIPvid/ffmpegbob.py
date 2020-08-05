import ffmpeg

stream = ffmpeg.input('http://192.168.1.6:8081/')
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'output.mp4')
ffmpeg.run(stream)
