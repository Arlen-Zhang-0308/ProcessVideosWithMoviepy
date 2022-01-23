from operator import concat
from tracemalloc import start
from cv2 import composeRT
from moviepy.editor import *

def moviepy_SplitVideo(src, startTime, endTime=0, outPath=''): 
    ''' 从一段视频中截取出一部分，输出为截取出来的部分和去掉截取部分的原视频两个文件。

        Parameters
        -------------
        @src：      视频路径
        @startTime：截取开始时间。
        @endTime：  截取终止之间。若不指定值，默认为0，此时直接截取到原视频末尾。
        @outPath：  输出路径。若不指定值，默认为空字符串，此时输出路径即为当前程序所在路径；
                    若路径为单个字符'1'，则输出路径为源文件路径。
    '''
    vid = VideoFileClip(src)
    dur = vid.duration
    filename = vid.filename
    if outPath == '1': 
        outPath0 = src.replace(filename, '')
    else: 
        outPath0 = outPath
    if endTime > startTime:            # 截取视频
        print('---视频截取---')
        outvid = CompositeVideoClip([vid.subclip(startTime, endTime)])
        outvid.write_videofile(outPath0 + filename[:-4] + '_Out1' + filename[-4:])
        outvid = concatenate_videoclips([vid.subclip(0, startTime), vid.subclip(endTime, dur)])
        outvid.write_videofile(outPath0 + filename[:-4] + '_Out2' + filename[-4:])
    else:                               # 切分为两个视频
        print('---视频分割---')
        outvid = CompositeVideoClip([vid.subclip(startTime, dur)])
        outvid.write_videofile(outPath0 + filename[:-4] + '_Out2' + filename[-4:])
        vid.close()
        vid = VideoFileClip(src)
        outvid = CompositeVideoClip([vid.subclip(0, startTime)])
        outvid.write_videofile(outPath0 + filename[:-4] + '_Out1' + filename[-4:])
    
if __name__ == '__main__':
    filePath = input('要剪辑的文件：')
    startT = input('剪辑开始时间：')
    endT = input('剪辑结束时间：')
    moviepy_SplitVideo(filePath, startT, endT)
