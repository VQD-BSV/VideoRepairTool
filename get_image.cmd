@echo off

"./FFmpeg/ffmpeg.exe" -i BSVRecovery.vn  -vf "select=eq(n\,0)" -q:v 2 -vsync vfr F_1.JPG

"./FFmpeg/ffmpeg.exe" -i BSVRecovery.vn -vf "select='eq(n\,floor(n/2))'" -vsync vfr -q:v 2 F_2.jpg

"./FFmpeg/ffmpeg.exe" -sseof -1 -i BSVRecovery.vn -update 1 -q:v 1 -frames:v 1 F_3.jpg
