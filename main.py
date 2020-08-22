import pyaudio
import wave

print("Hello, World!")


class AudioConfig:
    def __init__(self):
        self.format = pyaudio.paInt16
        self.channels = 2
        self.rate = 44100
        self.chunk = 1024
        self.length = 3
        self.filename = "file.wav"


cfg = AudioConfig()
audio = pyaudio.PyAudio()

stream = audio.open(format=cfg.format, channels=cfg.channels,
                    rate=cfg.rate, input=True, frames_per_buffer=cfg.chunk)

print ("Recording")
frames = []

frameCount = int(cfg.rate / cfg.chunk * cfg.length)
for i in range(frameCount):
    data = stream.read(cfg.chunk)
    frames.append(data)

print("Finished")


stream.stop_stream()
stream.close()
audio.terminate()

wav = wave.open(cfg.filename, 'wb')
wav.setnchannels(cfg.channels)
wav.setsampwidth(audio.get_sample_size(cfg.format))
wav.setframerate(cfg.rate)
wav.writeframes(b''.join(frames))
wav.close()

