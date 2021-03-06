#!/usr/bin/env python

import tracks
from utils import Singleton


class Config(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.config = None

    def update(self):
        self.config = {
            "actions": ["process_image", "text_images", "site_images", "hue_images", "copy_directories"],
            # "actions": ["process_image", "text_images", "site_images", "hue_images"],
            # "actions": ["process_image",  "site_images", "hue_images", "copy_directories"],
            # "actions": ["hue_images", "copy_directories"],
            # "actions": ["process_image"],
            # "actions": ["process_image","text_images","site_images", "copy_directories"],
            # "actions": ["text_images","site_images", "copy_directories"],
            # "actions": ["text_images"],
            # "actions": ["site_images", "copy_directories"],
            # "actions": [ "copy_directories"],
            # "process_image_fx": "fx_dreamsmooth  1,1,27,0.861,0,0,4,0,0",  # "fx_dreamsmooth 1,1,1,0.8,0,0.8,1,24,0",
            "text_dir": "texts",
            "image_dir": "images",
            "circle": False,
            "basic_image": "basic.png",
            "hue_image": "basic2.png",
            "process_image": {"name": "processedImage",
                              "gradient": {"name": "FG to BG (HSV clockwise hue)",
                                           "enable": False,
                                           "forground_color": [255, 0, 0],
                                           "background_color": [250, 0, 0]},
                              "fx": {"enable": False,
                                     "value": "fx_dreamsmooth  1,1,27,0.861,0,0,4,0,0"},
                              # "fx_dreamsmooth 1,1,1,0.8,0,0.8,1,24,0",
                              "hue_saturation": {"enable": False,
                                                 "value": [0, 0, 3, 100]}
                              },
            "hue_scale": [512, 512],
            "hue_circle": False,
            "hue_params": [0, -5, 5, 100],
            "hue_intervals": [-90, 90],

            "logo_margin": 0.03,
            "logo": "D:/MakingMusic/Automatic Music Machine/Images/logoWhite.png",

            "winamp_root": "D:/MakingMusic/Automatic Music Machine/Images/",
            "site_image_list": [
                ["SoundCloudBanner", "jpg", 2480.0, 800.0, []],

                ["YouTubeThumbnail", "jpg", 1280.0, 720.0,
                 [["logo", "upr"], ["dream_small", "lowl"], ["title_small", "centerl"], ["composer", "center"]]],

                ["YouTubeCompanionAddBanner", "png", 300.0, 60.0,
                 [["composer_small", "center"]]],

                ["YouTubeBanner", "jpg", 2560.0, 1440.0,
                 [["banner_center", "center"], ["composer_small", "banner_centeru"], ["dream_small", "lowl"]]],

                ["HDWithText", "jpg", 1920.0, 1080.0,
                 [["logo", "lowr"], ["dream", "lowl"], ["title", "centerl"], ["composer", "center"]]],

                ["HD_verticalWithText", "jpg", 1080.0, 1920.0,
                 [["logo", "lowr"], ["dream", "lowl"], ["title", "centerl"], ["composer", "center"]]],

                # ["HD", 1920.0, 1080.0, []],
                # ["HD_vertical", 1080.0, 1920.0, []],
                ["SoundCloudAlbumCoverAndBandCamp", "png", 1400.0, 1400.0,
                 [["logo", "lowr"], ["dream", "lowl"], ["title", "centerl"], ["composer", "centeru"]]],

                ["SoundCloudAvatar", "png", 800.0, 800.0, []],
                ["SpotifyBanner", "jpg", 2660.0, 1140.0, []],
                ["SpotifyHeaderMax", "jpg", 6000.0, 4000.0, []],
                ["DistroKid", "jpg", 3000.0, 3000.0, []],
                ["DistroKidWithText", "jpg", 3000.0, 3000.0,
                 [["logo", "lowr"], ["dream", "lowl"], ["title", "centerl"], ["composer", "center"]]],
                ["FacebookCoverPhoto", "png", 820.0, 360.0, []],
                ["FacebookProfilePic", "png", 400.0, 400.0, []],
                ["FacebookVideo", "jpg", 1280.0, 720.0, []],
                ["FacebookLinkShare", "jpg", 1200.0, 630.0, []],
                ["InstegramPic", "jpg", 1080.0, 1350.0, []]
            ],
            "text_list_for_video": [
                [tracks.Track().get_title(), "Segoe UI Bold", 85, (1.0, 1.0, 1.0),
                 "fx_textured_glass 17.6,11.6,0,0,0.319,7.03,5,0,50,50"],
                [tracks.Track().get_composer(), "Segoe UI Bold", 85, (1.0, 1.0, 1.0),
                 "fx_gaussian_blur  3,0,0,1,0,0,0,50,50"],
                [tracks.Track().get_banner(), "Segoe UI Light", 85, (1.0, 1.0, 1.0),
                 "fx_gcd_crt  1.8,1.8,0,0"],
                # ["DUNE SPRING", "Segoe UI Light", 85, (1.0, 1.0, 1.0),
                #  "fx_wind  20,0,0.7,20,1,0,0,0,50,50"],
                # ["DESERT DUNE", "Segoe UI Light", 85, (1.0, 1.0, 1.0),
                #  "fx_gaussian_blur  3,0,0,1,0,0,0,50,50"],
                # ["SAXY PLONTER", "Segoe UI Bold", 85, (1.0, 1.0, 1.0),
                #  "fx_wind  20,0,0.7,20,1,0,0,0,50,50"],
                # ["CAFE AU PLANET Z3", "Segoe UI Light", 85, (1.0, 1.0, 1.0),
                #  "fx_gaussian_blur  3,0,0,1,0,0,0,50,50"],
                # ["LONELY FLOATER", "Segoe UI Light", 75, (1.0, 1.0, 1.0),
                #  "fx_gaussian_blur  3,0,0,1,0,0,0,50,50"],
                # ["ELECTRIC REAGGAE", "Segoe UI Light", 65, (1.0, 1.0, 1.0),
                #  "fx_gaussian_blur  3,0,0,1,0,0,0,50,50"],
                # ["LIQUID DREAMS", "Segoe UI Light", 65, (1.0, 1.0, 1.0),
                #  "fx_gaussian_blur  3,0,0,1,0,0,0,50,50"],
                # ["BITOKANA", "Segoe UI Light", 65, (1.0, 1.0, 1.0),
                #  "fx_gaussian_blur  3,0,0,1,0,0,0,50,50"],
                # ["BUDDHA ACID BELL", "Segoe UI Light", 65, (1.0, 1.0, 1.0),
                #  "fx_gaussian_blur  3,0,0,1,0,0,0,50,50"],
                # ["DAM DAM", "Segoe UI Light", 65, (1.0, 1.0, 1.0),
                #  "fx_gaussian_blur  3,0,0,1,0,0,0,50,50"],
                # ["HUNTED ROOMS", "Segoe UI Light", 65, (1.0, 1.0, 1.0),
                #  "fx_gaussian_blur  3,0,0,1,0,0,0,50,50"],
                # ["QUEST TO BRASS", "Segoe UI Light", 65, (1.0, 1.0, 1.0),
                #  "fx_gaussian_blur  3,0,0,1,0,0,0,50,50"],
                # ["UFO TRANSMISSION", "Segoe UI Light", 65, (1.0, 1.0, 1.0),
                #  "fx_gaussian_blur  3,0,0,1,0,0,0,50,50"],
                # ["GOLEM", "Segoe UI Light", 65, (1.0, 1.0, 1.0),
                #  "fx_gaussian_blur  3,0,0,1,0,0,0,50,50"],
                # ["party set 1", "Segoe UI Light", 85, (1.0, 1.0, 1.0),
                #  "fx_gcd_crt  1.8,1.8,0,0"]
            ],
            "text_list": [
                ["composer", tracks.Track().get_composer(), "Segoe UI", 88, (1.0, 1.0, 1.0),
                 "fx_textured_glass 17.6,11.6,0,0,0.319,7.03,5,0,50,50"],
                ["banner_center", tracks.Track().get_banner(), "Segoe UI Bold", 128, (1.0, 1.0, 1.0),
                 "fx_textured_glass 17.6,11.6,0,0,0.319,7.03,5,0,50,50"],
                ["title", tracks.Track().get_title(), "Segoe UI Bold", 88, (1.0, 1.0, 1.0),
                 "fx_textured_glass 17.6,11.6,0,0,0.319,7.03,5,0,50,50"],
                ["title_small", tracks.Track().get_title(), "Segoe UI Semi-Light", 44, (1.0, 1.0, 1.0),
                 "fx_textured_glass 17.6,11.6,0,0,0.319,7.03,5,0,50,50"],
                ["dream", tracks.Track().get_painter(), "Segoe UI Light", 84, (1.0, 1.0, 1.0),
                 "fx_textured_glass 17.6,11.6,0,0,0.319,7.03,5,0,50,50"],
                ["composer_small", tracks.Track().get_composer(), "Segoe UI Semi-Light", 48, (1.0, 1.0, 1.0),
                 "fx_textured_glass 17.6,11.6,0,0,0.319,7.03,5,0,50,50"],
                ["dream_small", tracks.Track().get_painter(), "Segoe UI", 36, (1.0, 1.0, 1.0),
                 "fx_textured_glass 17.6,11.6,0,0,0.319,7.03,5,0,50,50"]
            ]
        }
