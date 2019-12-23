
# Video

## Resize

[FFMpeg info](https://trac.ffmpeg.org/wiki/Scaling%20(resizing)%20with%20ffmpeg)

```bash
$ ffmpeg -i input.avi -vf scale=320:240 output.avi
```

## Crop

```bash
$ ffmpeg -i /video/Perso/GoPro/GOPR0035.MP4 -strict -2 -vf "crop=1920:1080:150:150" after.mp4
``` 

## Stabilize

Basic stabilization:

```bash
$ ffmpeg -i input.mov -vf deshake output.mov
```

Advanced Stabilization:

* https://scottlinux.com/2016/09/17/video-stabilization-using-vidstab-and-ffmpeg-on-linux/
* https://www.epifocal.net/blog/video-stabilization-with-ffmpeg

https://hub.docker.com/r/jrottenberg/ffmpeg/

```bash
$ docker run -v $(pwd):/tmp/workdir -v /video/Perso/GoPro:/tmp/video jrottenberg/ffmpeg:alpine -i /tmp/video/GOPR0032.MP4 -vf vidstabtransform=input=transform_vectors.trf:zoom=1:smoothing=30,unsharp=5:5:0.8:3:3:0.4 -vcodec libx264 -preset slow -tune film -crf 18 -acodec copy /tmp/workdir/SMOOTH_OUTPUT_VIDEO.mp4
```

## convert to GIF

Convert video to animated GIF:

```bash
$ sudo apt-get install ffmpeg imagemagick
$ ffmpeg -i input.mp4 -vf scale=480:-1 -r 3 -f image2pipe -vcodec ppm - | convert -delay 20 -loop 0 - output.gif
```

## concat

Concat multiple video (useful when kids want to see a bunch of episodes and playlists are not available)

```bash
$ for f in ./*.mp4; do echo "file '$f'" >> mylist.txt; done
$ ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.mp4
```

[Source docs](https://trac.ffmpeg.org/wiki/Concatenate)