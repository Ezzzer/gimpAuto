#!/usr/bin/env python

title = "CAFE AU PLANET Z3"
composer = "E Z Z Z E R"
painter = "DREAM"
banner = "PSY MELODIC TECHNO MUSIC"
root_dir = "D:/MakingMusic/Automatic Music Machine/3.In Progress/Bit8_planet cafe"

config = {"root_dir": root_dir,
          "actions": ["process_image", "text_images", "site_images", "hue_images", "copy_directories"],
          # "actions": ["processed_image"],
          # "actions": ["processed_image","text_images","site_images", "copy_directories"],
          # "actions": ["text_images","site_images", "copy_directories"],
          # "actions": ["site_images", "copy_directories"],
          # "actions": [ "copy_directories"],
          "process_image_fx": "fx_dreamsmooth 3,1,1,0.8,0,0.8,1,24,0",
          "circle": True,
          "process_image_hue_params": [-35, -10, 0, 100],
          "process_image_hue_intervals": [-90, 90],
          "hue_circle": False,
          "hue_scale": [512, 512],
          "site_image_offset": 0,
          "basic_image": "basic.png",
          "image_dir": "images",
          "text_dir": "texts",
          "processed_image": "processedImage.png",
          "logo_margin": 0.03,
          "logo": "D:/MakingMusic/Automatic Music Machine/Images/logoWhite.png",
          "winamp_root": "D:/MakingMusic/Automatic Music Machine/Images/",
          "site_image_list": [
              ["YouTubeThumbnail", 1280.0, 720.0,
               [["logo", "upr"], ["dream_small", "lowl"], ["title_small", "centerl"], ["composer", "center"]]],
              ["YouTubeBanner", 2560.0, 1440.0,
               [["banner_center", "center"], ["composer_small", "banner_centeru"], ["dream_small", "lowl"]]],
              ["HDWithText", 1920.0, 1080.0,
               [["logo", "lowr"], ["dream", "lowl"], ["title", "centerl"], ["composer", "center"]]],
              ["HD_verticalWithText", 1080.0, 1920.0,
               [["logo", "lowr"], ["dream", "lowl"], ["title", "centerl"], ["composer", "center"]]],
              ["HD", 1920.0, 1080.0, []],
              ["HD_vertical", 1080.0, 1920.0, []],
              ["SoundCloudBanner", 2480.0, 520.0, []],
              ["SoundCloudAlbumCoverAndBandCamp", 1400.0, 1400.0,
               [["logo", "lowr"], ["dream", "lowl"], ["title", "centerl"], ["composer", "centeru"]]],
              ["SoundCloudAvatar", 800.0, 800.0, []],
              ["SpotifyBanner", 2660.0, 1140.0, []],
              ["SpotifyHeaderMax", 6000.0, 4000.0, []],
              ["DistroKid", 3000.0, 3000.0, []],
              ["DistroKidWithText", 3000.0, 3000.0,
               [["logo", "lowr"], ["dream", "lowl"], ["title", "centerl"], ["composer", "center"]]],
              ["FacebookCoverPhoto", 820.0, 360.0, []],
              ["FacebookProfilePic", 400.0, 400.0, []],
              ["FacebookVideo", 1280.0, 720.0, []],
              ["FacebookLinkShare", 1200.0, 630.0, []],
              ["InstegramPic", 1080.0, 1350.0, []]
          ],
          "text_list_for_video": [
              [title, "Segoe UI Light", 85, (1.0, 1.0, 1.0), "ripple  3.4,20,2,0,0"],
              ["PSYCHEDELIC", "Segoe UI Bold", 85, (1.0, 1.0, 1.0), "fx_gaussian_blur  3,0,0,1,0,0,0,50,50"],
              ["MELODIC", "Segoe UI Light", 85, (1.0, 1.0, 1.0), "fx_gcd_crt  1.8,1.8,0,0"],
              ["TECHNO", "Segoe UI Light", 85, (1.0, 1.0, 1.0), "fx_wind  20,0,0.7,20,1,0,0,0,50,50"],
              ["MUSIC", "Segoe UI Light", 85, (1.0, 1.0, 1.0), "fx_dreamsmooth  1,1,1,0.8,0,0.8,1,24,0.0"],
              ["DANCE", "Segoe UI Bold", 85, (1.0, 1.0, 1.0), "fx_wind  20,0,0.7,20,1,0,0,0,50,50"],
              ["TRANCE", "Segoe UI Light", 85, (1.0, 1.0, 1.0), "fx_gaussian_blur  3,0,0,1,0,0,0,50,50"],
              ["LOVE", "Segoe UI Light", 85, (1.0, 1.0, 1.0), "fx_gaussian_blur  3,0,0,1,0,0,0,50,50"],
              ["melody", "Segoe UI Bold", 85, (1.0, 1.0, 1.0), "fx_dreamsmooth  3,1,1,0.8,0,0.8,1,24,0.0"],
              ["tech", "Segoe UI Light", 85, (1.0, 1.0, 1.0), "fx_gcd_crt  1.8,1.8,0,0"]],
          "text_list": [
              ["composer", composer, "Segoe UI Light", 85, (1.0, 1.0, 1.0),
               "fx_textured_glass 17.6,11.6,0,0,0.319,7.03,5,0,50,50"],
              ["banner_center", banner, "Segoe UI Light", 84, (1.0, 1.0, 1.0),
               "fx_textured_glass 17.6,11.6,0,0,0.319,7.03,5,0,50,50"],
              ["title", title, "Segoe UI Light", 88, (1.0, 1.0, 1.0),
               "fx_textured_glass 17.6,11.6,0,0,0.319,7.03,5,0,50,50"],
              ["title_small", title, "Segoe UI Light", 44, (1.0, 1.0, 1.0),
               "fx_textured_glass 17.6,11.6,0,0,0.319,7.03,5,0,50,50"],
              ["dream", painter, "Segoe UI Light", 84, (1.0, 1.0, 1.0),
               "fx_textured_glass 17.6,11.6,0,0,0.319,7.03,5,0,50,50"],
              ["composer_small", composer, "Segoe UI Light", 45, (1.0, 1.0, 1.0),
               "fx_textured_glass 17.6,11.6,0,0,0.319,7.03,5,0,50,50"],
              ["dream_small", painter, "Segoe UI Light", 36, (1.0, 1.0, 1.0),
               "fx_textured_glass 17.6,11.6,0,0,0.319,7.03,5,0,50,50"]
          ]
          }
