#!/bin/bash
sleep 4
#gnome-terminal --geometry=80x20+30+0
export OPENBLAS_CORETYPE=ARMV8
cd ~/kensa/cam_autofocus-main/
sleep 1
wmctrl -i -r 0x02600006 -e 0,1000,0,640,400
wmctrl -i -a 0x02600006
sleep 1
python3 check_cam.py

