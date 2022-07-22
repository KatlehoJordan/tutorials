# From https://www.youtube.com/watch?v=p293_8oYXL4
# cd <to here>
# conda create --name split_screen_moviepy python=3.9.12
# conda activate split_screen_moviepy
# pip install -r requirements.txt

# Goal is to show multiple videos playing simultaneously
# download copyright-free videos from pixabay

from moviepy.editor import VideoFileClip, clips_array

length = 2

clip1 = VideoFileClip('Aerial - 18390.mp4').subclip(0, 0 + length)
clip2 = VideoFileClip('Fall - 23881.mp4').subclip(0, 0 + length)
clip3 = VideoFileClip('Sea - 13704.mp4').subclip(0, 0 + length)
clip4 = VideoFileClip('Stars - 6962.mp4').subclip(0, 0 + length)

clip_2_vids = clips_array([[clip1, clip2]])
clip_4_vids = clips_array([[clip1, clip2, clip3, clip4]])
clip_4_vids_2_rows = clips_array([[clip1, clip2], [clip3, clip4]])

clip_2_vids.write_videofile('2_vids.mp4')
clip_4_vids.write_videofile('4_vids.mp4')
clip_4_vids_2_rows.write_videofile('4_vids_2_rows.mp4')

# Note that all 3 files were made without a problem.
# Then I could play the first one without a problem.
# Attempts to play the other two led to "Server execution failed".
# After this, trying to play the first or the original files also led to the same error.
# Tried restarting computer.
