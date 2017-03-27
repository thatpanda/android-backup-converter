# convert adb backup to tar
#
# create backup for a specific app:
# adb backup -f test.backup com.example.test
#
# http://stackoverflow.com/questions/15558353/how-can-one-pull-the-private-data-of-ones-own-android-app
# http://stackoverflow.com/questions/19225467/backing-up-android-device-using-adb

import sys
import zlib

with open("test.backup", "rb") as f:
    f.read(24)
    content = f.read()

with open("test.tar", "wb") as f:
    f.write(zlib.decompress(content))
