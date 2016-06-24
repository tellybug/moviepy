import pytest

import os
from moviepy.editor import *


def test_youtube_download():
    yt_id = "M3EO_qzrKB0"
    download_webfile(yt_id, 'youtube.mp4')
    assert os.path.isfile('youtube.mp4')
