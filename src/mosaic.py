from utils import *

# 160x120 resolution
resolution = "160x120_resolution"
video1 = f'../media/{resolution}_vp8.webm'
video2 = f'../media/{resolution}_vp9.webm'
video3 = f'../media/{resolution}_h265.mp4'
video4 = f'../media/{resolution}_av1.mkv'

mosaic(video1, video2, video3, video4, "160x120_mosaic")

# 360x240 resolution
resolution = "360x240_resolution"
video1 = f'../media/{resolution}_vp8.webm'
video2 = f'../media/{resolution}_vp9.webm'
video3 = f'../media/{resolution}_h265.mp4'
video4 = f'../media/{resolution}_av1.mkv'

mosaic(video1, video2, video3, video4, "360x240_mosaic")

# 480p resolution
resolution = "480p_resolution"
video1 = f'../media/{resolution}_vp8.webm'
video2 = f'../media/{resolution}_vp9.webm'
video3 = f'../media/{resolution}_h265.mp4'
video4 = f'../media/{resolution}_av1.mkv'

mosaic(video1, video2, video3, video4, "480p_mosaic")

# 720p resolution
resolution = "720p_resolution"
video1 = f'../media/{resolution}_vp8.webm'
video2 = f'../media/{resolution}_vp9.webm'
video3 = f'../media/{resolution}_h265.mp4'
video4 = f'../media/{resolution}_av1.mkv'

mosaic(video1, video2, video3, video4, "720p_mosaic")
