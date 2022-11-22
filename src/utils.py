import glob
import os


def menu():
    lof = glob.glob("../media/*.mp4")
    for f in lof:
        print(lof.index(f) + 1, f[len("../media/"):])

    nof = int(input("Number of file to select: "))

    name = lof[nof - 1]
    print_name = name[len("../media/"):]
    print("You've chosen: " + print_name)
    print("\n")

    return name


def resolution_menu():
    resolutions = ["720p", "480p", "360x240", "160x120"]

    for resolution in resolutions:
        print(resolutions.index(resolution) + 1, resolution)

    n = int(input("Resolution desired: "))
    print("You've chosen: " + resolutions[n - 1])
    print("\n")

    if n == 1:
        return "scale=1280:720", "720p_resolution"
    elif n == 2:
        return "scale=854:420", "480p_resolution"
    elif n == 3:
        return "scale=360:240", "360x240_resolution"
    elif n == 4:
        return "scale=160:120", "160x120_resolution"


def codecs_menu():
    codecs = ["vp8", "vp9", "h265", "av1"]

    for codec in codecs:
        print(codecs.index(codec) + 1, codec)

    n = int(input("Codec desired: "))
    print("You've chosen: " + codecs[n - 1])
    print("\n")

    return codecs[n - 1]


def resizer(file_name):
    # Select resolution desired
    resolution, new_name = resolution_menu()
    new_name = "../media/" + new_name

    # Apply transformation using ffmpeg
    command = f'ffmpeg -i {file_name} -vf {resolution} {new_name}.mp4'
    os.system(command)


def converter(file_name):
    # Sources:

    # https://trac.ffmpeg.org/wiki/Encode/VP8
    # https://trac.ffmpeg.org/wiki/Encode/VP9
    # https://trac.ffmpeg.org/wiki/Encode/H.265
    # https://trac.ffmpeg.org/wiki/Encode/AV1

    # Select codec desired
    codec = codecs_menu()

    # Apply transformation using ffmpeg

    command = f'ffmpeg -i {file_name} -c:v '
    new_name = "../media/" + file_name[:-4] + "_" + codec  # remove .mp4 from file_name

    if codec == "vp8":
        command += f'libvpx -crf 10 -b:v 1M -c:a libvorbis {new_name}.webm'
    elif codec == "vp9":
        command += f'libvpx-vp9 -b:v 2M {new_name}.webm'  # ABR method, two pass recommended
    elif codec == "h265":
        command += f'libx265 -crf 26 -preset fast -c:a aac -b:a 128k {new_name}.mp4'
    elif codec == "av1":
        command += f'libaom-av1 -crf 30 {new_name}.mkv'

    # print(command)
    os.system(command)


def mosaic(file_name1, file_name2, file_name3, file_name4, output_name):

    command = f'ffmpeg -i {file_name1} -i {file_name2} -i {file_name3} -i {file_name4} ' + \
              '-filter_complex "nullsrc=size=1280x720 [base];' + \
              '[0:v] setpts=PTS-STARTPTS, scale=640x360 [upperleft];' + \
              '[1:v] setpts=PTS-STARTPTS, scale=640x360 [upperright];' + \
              '[2:v] setpts=PTS-STARTPTS, scale=640x360 [lowerleft];' + \
              '[3:v] setpts=PTS-STARTPTS, scale=640x360 [lowerright];' + \
              '[base][upperleft] overlay=shortest=1 [tmp1]; ' + \
              '[tmp1][upperright] overlay=shortest=1:x=640 [tmp2]; ' + \
              '[tmp2][lowerleft] overlay=shortest=1:y=360 [tmp3]; ' + \
              f'[tmp3][lowerright] overlay=shortest=1:x=640:y=360" -c:v libx265 ../media/{output_name}.mp4'

    os.system(command)

