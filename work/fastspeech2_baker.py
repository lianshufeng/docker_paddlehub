import paddlehub as hub

# 需要合成语音的文本
sentences = ['这是一段测试语音合成的音频,']

model = hub.Module(
    name='fastspeech2_baker',
    version='1.0.0')
wav_files =  model.generate(sentences)

# 打印合成的音频文件的路径
print(wav_files)