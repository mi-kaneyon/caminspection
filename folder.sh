#!/bin/bash
#sleep
export OPENBLAS_CORETYPE=ARMV8
nautilus --browser ~/kensa/cam_autofocus-main/Check
wmctrl -r Check -e 0,1000,0,400,640 -b add,below


