from pytube import YouTube
import moviepy.editor as mp
import os
import re
import cv2


path_to_save_audio = "E:/CodeRush/YoutubePipeline/Audios"
path_to_save_videos = f"E:/CodeRush/YoutubePipeline/Videos"
frame_interval = int(100)

try:
    if not os.path.exists('Videos'):
        os.makedirs('Videos')

except:
    print("Error Creating Videos directory")

try:
    if not os.path.exists('Audios'):
        os.makedirs('Audios')

except:
    print("Error Creating Audios directory")

try:
    if not os.path.exists('Images'):
        os.makedirs('Images')

except:
    print("Error Creating Images directory")


def download_video(url):
    yt = YouTube(url)
    name_ = yt.title
    yt = yt.streams.get_highest_resolution()
    f_extension = yt.mime_type.split('/')[-1]
    saved_file_name = name_+"."+f_extension
    print(f"Saved file name is {saved_file_name}")
    yt.download(output_path= path_to_save_videos)

def extract_audio(videoname_):
    name = videoname_.split('.')[0]
    input_path = f'Videos/{videoname_}'
    print(input_path)
    output_path = f'{path_to_save_audio}/{name}.mp3'
    video = mp.VideoFileClip(input_path)
    video.audio.write_audiofile(output_path)


def extract_frames(videoname_):
    name = videoname_.split('.')[0]
    input_path = f'Videos/{videoname_}'
    vdo = cv2.VideoCapture(input_path)
    try:
        if not os.path.exists(f'Images/{name}'):
            os.makedirs(f'Images/{name}')

    except:
        print("Error Creating directory")
    
    currentframe = 0
    ret, frame = vdo.read()
    while(ret):
        if (currentframe % frame_interval) == 0:
            name_ = f'Images/{name}/frame' + str(currentframe) + '.jpg'
            cv2.imwrite(name_, frame)
    
        ret, frame = vdo.read()
        currentframe+=1


if __name__ == "__main__":
    flag = 1
    while(flag):
        url = input("Enter URL to download video: ")
        download_video(url)
        more_videos = input("Do you want to download other vidoes? Yes or No?")
        if more_videos.lower() == 'yes' or more_videos.lower() == 'y':
            continue
        else:
            flag = 0
    
    for video in os.listdir("Videos"):
        extract_audio(video)
        print("Frames of the video is extracting")
        extract_frames(video)