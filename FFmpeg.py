import glob
import os
import subprocess

TAG = r"\Warszawa"
INPUT_DIR = r'I:\DCIM\100MEDIA'
OUTPUT_DIR = r'E:\DJI Video' + TAG
FFMPEG_COMMAND = 'ffmpeg -i'
FFMPEG_WD = r'C:\Users\Piotr\Desktop\FFmpeg\bin'
file_name_only = ""

if not os.path.isdir(OUTPUT_DIR):
    subprocess.run(['mkdir', OUTPUT_DIR], cwd=FFMPEG_WD, shell=True)

MP4_file_names_List = glob.glob(INPUT_DIR + r'\*.MP4')

for input_video_absolute_path in MP4_file_names_List:
    file_name_only = os.path.basename(input_video_absolute_path)
    subprocess.run(['ffmpeg', '-i', input_video_absolute_path, OUTPUT_DIR + r'\\' + file_name_only], cwd=FFMPEG_WD,
                   shell=True)
