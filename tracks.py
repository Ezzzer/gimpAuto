#!/usr/bin/env python

current_track = "HEADLESS CHIMERA"
banner = "FUTURE HOUSE MUSIC"
composer = "E Z Z Z E R"
painter = "DREAM"

tracks = {"HEADLESS CHIMERA":
              {"title": "HEADLESS CHIMERA",
               "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\No125 - Headless Chimera'}
          }


def get_current_track():
    return tracks[current_track]


def get_track(track_id=None):
    if track_id is None:
        track = get_current_track()
    else:
        track = tracks[track_id]
    return track


def get_title(track_id=None):
    return get_track(track_id)["title"]


def get_rootDir(track_id=None):
    return get_track(track_id)["rootDir"]
