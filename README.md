# SCAV-S3-Video
Seminar 3 - Sistemes de Codificació d'Audio i Video SCAV
Marc Rodriguez Jareño Nia: 228997

# Exercici 1.1
 
Sources:
https://trac.ffmpeg.org/wiki/Encode/VP8
https://trac.ffmpeg.org/wiki/Encode/VP9
https://trac.ffmpeg.org/wiki/Encode/H.265
https://trac.ffmpeg.org/wiki/Encode/AV1

# Exercici 1.2

I created a function that selects the concrete resolution of the previous outputs and shows us 4 videos in one. We could see the bitrates using ffprobe

1280x720 AV1: 944 kb/s VP9: 1279 kb/s H265: 767 kb/s VP8: 533 kb/s

640x480 AV1: 593 kb/s VP9: 761 kb/s H265: 564 kb/s VP8: 493 kb/s

360x240: AV1: 408 kb/s VP9: 474 kb/s H265: 454 kb/s VP8: 419 kb/s

160x120: AV1: 308 kb/s VP9: 339 kb/s H265: 397 kb/s VP8: 350 kb/s

Some conclusions:

For lower resolutions, AV1 has less bitrate. For larger resolutions, VP8 has less bitrate but also less quality.
The parameters used may not be the most efficient ones.
AV1 can sabe about 30% bitrate compared to VP9 and h265, and about 50% h264.
VP9 seems better, in quality terms, than h265. VP8 has the worst resolution quality of the 4 codecs.

# Exercici 2

Video Conversor 

<img width="341" alt="Captura de Pantalla 2022-11-23 a las 2 06 19" src="https://user-images.githubusercontent.com/72939158/203451573-be9c6ef7-d4ba-4a8c-a256-9cab552be47b.png">

