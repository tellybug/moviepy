"""
Tests meant to be run with pytest
"""

import pytest
import os
from moviepy.editor import *


@pytest.fixture
def fixtures_path():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures')

def fixtures_file(name):
    return os.path.join(fixtures_path(), name)


def setup_module(module):
    download_webfile("M3EO_qzrKB0", fixtures_file('youtube.mp4'))
    download_webfile('http://tellybug-static.s3.amazonaws.com/xfitv.tellybug.com/video/20161009/201053/TXF_TX13_Ryan_081016_APP.mp4',
                     fixtures_file('TXF_TX13_Ryan_081016_APP.mp4'))

def teardown_module(module):
    pass


def test_open_mp4(fixtures_path):
    video = VideoFileClip(os.path.join(fixtures_path, "youtube.mkv"))
    assert video.duration == 204.1
    assert video.w == 1920
    assert video.h == 1080


def test_open_mov(fixtures_path):
    video = VideoFileClip(os.path.join(fixtures_path, "Louis_StarIsBorn.mov"))
    assert video.duration == 1.56
    assert video.w == 1920
    assert video.h == 1080


def test_open_image(fixtures_path):
    image = ImageClip(os.path.join(fixtures_path, "Reggie.jpg"))
    assert image.w == 5674
    assert image.h == 3191


def test_resize_image(fixtures_path):
    image = ImageClip(os.path.join(fixtures_path, "Reggie.jpg"))
    image = image.resize((1920, 1080))
    assert image.w == 1920
    assert image.h == 1080


def test_open_corrupt_metadata(fixtures_path):
    video = VideoFileClip(os.path.join(fixtures_path, 'TXF_TX13_Ryan_081016_APP.mp4'))
    assert video.w == 1920
    assert video.h == 1080
