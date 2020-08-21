#!/bin/bash

# Both watch and save a broadcast stream at the same time
# Assumes both youtube-dl and mpv are installed.
# NB. Mpv can be substituted for any other media player
# that accepts a stdstream input from the shell, e.g. mplayer

URL=$1
TITLE=$(youtube-dl --skip-download --get-title --no-warnings $URL | sed 2d | awk '{print tolower($0)}')
youtube-dl $URL -o - | tee "$TITLE".mp4 | mpv -
