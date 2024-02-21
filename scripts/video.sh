#!/usr/bin/env sh

#!/bin/sh

######
## Generate video thumbnails
## Rubenerd Industries
## Updated to use yt-dlp instead of youtube-dl

set -e
set -x

SERVER="frogren.se"

PLAY1X="../metadata/play@1x.png"
PLAY2X="../metadata/play@2x.png"

## Download video thumbnail
VIDEO=$(yt-dlp --list-thumbnails --no-warnings --no-sponsorblock $1 | tail -n 1 | awk '{ print $4 }')
curl -Lo thumb.webp $VIDEO

## Get video title
TITLE=`yt-dlp --get-title --no-warnings --no-sponsorblock $1`

## Get video ID
ID=`echo $1 | awk -F= '{ print $2 }'`

## Get year for archive
YEAR=`date '+%Y'`

## Generate image URLs
## TODO: Make clipboard copy work on FreeBSD, not just macOS
FILE="https://frogren.se/files/$YEAR/yt-$ID"
HTML="<figure><p><a target="_BLANK" href=\"$1\" title=\"Play $TITLE\"><img src=\"$FILE@1x.jpg\" srcset=\"$FILE@1x.jpg 1x, $FILE@2x.jpg 2x\" alt=\"Play $TITLE\" style=\"width:500px;height:281px;\" /></a></p></figure>"
echo $HTML | pbcopy

## Create thumbnails
convert -resize 1000x563 "thumb.webp" -quality 97 -crop 1000x562+0+0 +repage +page "$PLAY2X" -flatten "yt-$ID@2x.jpg"
convert -resize 500x281 "thumb.webp" -quality 97 "yt-$ID@1x.jpg" "$PLAY1X" -flatten "yt-$ID@1x.jpg"
rm -rf "thumb.webp"

## Upload files and delete on success
scp yt-$ID@*jpg $SERVER:$YEAR/ && rm -rf yt-$ID@*jpg && rm -rf "$THUMB"
