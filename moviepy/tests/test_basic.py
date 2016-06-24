"""
Tests meant to be run with pytest
"""

import pytest
import os
from moviepy.editor import *

@pytest.fixture
def fixtures_path():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures')

def test_open_mp4(fixtures_path):
    video = VideoFileClip(os.path.join(fixtures_path, "youtube.mp4"))
    assert video.duration == 204.08
    assert video.w == 1280
    assert video.h == 720

def test_open_mov(fixtures_path):
    video = VideoFileClip(os.path.join(fixtures_path, "Louis_StarIsBorn.mov"))
    assert video.duration == 1.56
    assert video.w == 1920
    assert video.h == 1080
