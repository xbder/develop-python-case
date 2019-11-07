# -*- coding：utf-8 -*-

import pyaudio
import wave
import time
import numpy as np

'''
    Python调用麦克风生成WAV文件
'''

# input_filename = "input.wav"                           # 麦克风采集的语音输入
# input_filepath = "D:/data/iat_tingxie/"              # 输入文件的path
# in_path = input_filepath + input_filename

# def get_audio(filepath):
#     aa = str(input("是否开始录音？   （y/N）"))
#     if aa == str("y") :
#         CHUNK = 256
#         FORMAT = pyaudio.paInt16
#         CHANNELS = 1                # 声道数
#         RATE = 16000                # 采样率
#         RECORD_SECONDS = 30
#         WAVE_OUTPUT_FILENAME = filepath
#         p = pyaudio.PyAudio()
#
#         stream = p.open(format=FORMAT,
#                         channels=CHANNELS,
#                         rate=RATE,
#                         input=True,
#                         frames_per_buffer=CHUNK)
#
#         print("*"*10, "开始录音：请在", RECORD_SECONDS, "秒内输入语音")
#         frames = []
#         batches = int(RATE / CHUNK)
#         for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#             if i % batches == 0:
#                 print("\r[{0}]".format(int(RECORD_SECONDS - i / batches)), end='', flush=True)
#             data = stream.read(CHUNK)
#             frames.append(data)
#         print("*"*10, "录音结束\n")
#
#         stream.stop_stream()
#         stream.close()
#         p.terminate()
#
#         wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#         wf.setnchannels(CHANNELS)
#         wf.setsampwidth(p.get_sample_size(FORMAT))
#         wf.setframerate(RATE)
#         wf.writeframes(b''.join(frames))
#         wf.close()
#     elif aa == str("N"):
#         exit()
#     else:
#         print("无效输入，请重新选择")
#         get_audio(in_path)

def get_audio2(filepath):
    # aa = str(input("是否开始录音？   （y/N）"))
    CHUNK = 256
    FORMAT = pyaudio.paInt16
    CHANNELS = 1  # 声道数
    RATE = 16000  # 采样率
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = filepath
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("*" * 10, "开始录音：请在", RECORD_SECONDS, "秒内输入语音")
    frames = []
    batches = int(RATE / CHUNK)
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        if i % batches == 0:
            print("\r[{0}]".format(int(RECORD_SECONDS - i / batches)), end='', flush=True)
        data = stream.read(CHUNK)
        frames.append(data)
    print("*" * 10, "录音结束\n")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

'''
    循环录音到同一个文件
'''
def loop_recording(filepath):
    # aa = str(input("是否开始录音？   （y/N）"))
    CHUNK = 256
    FORMAT = pyaudio.paInt16
    CHANNELS = 1  # 声道数
    RATE = 16000  # 采样率
    RECORD_SECONDS = 3
    WAVE_OUTPUT_FILENAME = filepath
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("*" * 10, "开始录音：请在", RECORD_SECONDS, "秒内输入语音")
    frames = []
    batches = int(RATE / CHUNK)
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        if i % batches == 0:
            print("\r[{0}]".format(int(RECORD_SECONDS - i / batches)), end='', flush=True)
        data = stream.read(CHUNK)
        frames.append(data)
    print("*" * 10, "录音结束\n")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


# def wav2pcm(wav_file, to_pcm):
#     f = open(wav_file, 'rb')
#     f.seek(0)
#     f.read(44)
#     data = np.fromfile(f, dtype=np.int16)
#     data.tofile(to_pcm)


if __name__ == '__main__':
    dir_paths = ['D:/data/iat_tingxie/']
    to_pcm = "D:/data/loop_recording.pcm"

    while True:
        inputfile = dir_paths[0] + str(time.time()).replace('.', '') + ".wav"
        print(inputfile)
        loop_recording(inputfile)    # 录音
        # wav2pcm(inputfile, to_pcm)       # 转pcm文件
    # inputfile = dir_paths[0] + "loop_recording.wav"
    # inputfile = dir_paths[0] + str(time.time()).replace('.', '') + ".wav"
    # print(inputfile)
    # loop_recording(inputfile)