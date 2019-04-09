from pyaudio import PyAudio, paInt16 
import numpy as np
import wave
import multiprocessing


class Recorder:
    def __init__(self):
        self.NUM_SAMPLES = 2000      #pyaudio内置缓冲大小
        self.SAMPLING_RATE = 8000    #取样频率
        self.LEVEL = 500         #声音保存的阈值
        self.COUNT_NUM = 20      #NUM_SAMPLES个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
        self.SAVE_LENGTH = 8         #声音记录的最小长度：SAVE_LENGTH * NUM_SAMPLES 个取样
        self.recording = False     #录音时间，单位s
        self.Voice_String = []

    def savewav(self,filename):
        wf = wave.open(filename, 'wb') 
        wf.setnchannels(1) 
        wf.setsampwidth(2) 
        wf.setframerate(self.SAMPLING_RATE) 
        wf.writeframes(np.array(self.Voice_String).tostring()) 
        # wf.writeframes(self.Voice_String.decode())
        wf.close() 

    def recorder(self):
        pa = PyAudio() 
        stream = pa.open(format=paInt16, channels=1, rate=self.SAMPLING_RATE, input=True, 
                         frames_per_buffer=self.NUM_SAMPLES)
        save_buffer = []
        self.recording = True
        timec = 30
        while True:
            # print time_count
            # 读入NUM_SAMPLES个取样
            string_audio_data = stream.read(self.NUM_SAMPLES) 
            # 将读入的数据转换为数组
            audio_data = np.fromstring(string_audio_data, dtype=np.short)
            # 计算大于LEVEL的取样的个数
            large_sample_count = np.sum( audio_data > self.LEVEL )
            # 如果个数大于COUNT_NUM，则至少保存SAVE_LENGTH个块
            if large_sample_count > self.COUNT_NUM:
                save_buffer.append( string_audio_data )
            timec -= 1
            print(timec)
            if not self.recording or timec == 0:
                if len(save_buffer)>0:
                    self.Voice_String = save_buffer
                    save_buffer = [] 
                    print("Recode a piece of  voice successfully!")
                    return True
                else:
                    return False

    def stop_record(self):
        self.recording = False


if __name__ == "__main__":
    r = Recorder()
    r.recorder()
    r.savewav('test.wav')
    print("sign")
    # r.recorder()
    # r.savewav("test.wav")