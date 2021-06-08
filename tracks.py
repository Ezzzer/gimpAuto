#!/usr/bin/env python
from utils import Singleton

class Track(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.current_track = "No200"
        self.banner = "FUTURE HOUSE MUSIC"
        self.composer = "E Z Z Z E R"
        self.painter = "DREAM"
        self.track_map = {
            "Liquid dreams":
                {"title": "LIQUID DREAMS",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\7.campaign\Liquid dreams'}
                 ,
            "Quasar":
                {"title": "QUASAR",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\Quasar'},
            "Dancing star":
                {"title": "DANCING STAR",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\Dancing Star'},
            "No2":
                {"title": "PSYCHO FLUTE",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\No2 - Psycho flute short version'},
            "No19":
                {"title": "DRAGON QUEST",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\No19 - Dragon Quest'},
            "No66":
                {"title": "DUNE SPRING",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\7.campaign\No66 - Dune spring'},
            "No77":
                {"title": "DESERT DUNE BASS",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\No77 - Desert dune bass'},
            "No78":
                {"title": "NEON LISTICK",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\7.campaign\No78 - Neon Listick'},
            "No79":
                {"title": "HOO HA",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\No79 - Hoo ha'},
            "No90":
                {"title": "SAXO PLONTER",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\No90 - Saxoplonter'},
            "No92":
                {"title": "NO WINGS ICARUS",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\7.campaign\No92 - No wings icarus'},
            "No105":
                {"title": "THRILLER",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\No105 - Thriller'},
            "No118":
                {"title": "SEA DRAGON",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\No118 leviathan'},
            "No124":
                {"title": "UFO TRANSMISSION",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\UFO Transmission'},
            "No125":
                {"title": "HEADLESS CHIMERA",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\No125 - Headless Chimera'},
            "No127":
                {"title": "QUEST TO BRASS",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\No127 - Questobrass'},
            "No131":
                {"title": "GOLEM",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\6.Mastered\No131 - Golem'},
            "No144":
                {"title": "HA SEVIVON",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\No144 - HaSevivon'},
            "No151":
                {"title": "JINGLE BELLS",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\No151 - Jingle bells'},
            "No155":
                {"title": "HUNTED ROOMS",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\No155 - Hunted rooms'},
            "No156":
                {"title": "QUEST WORLD",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\6.Mastered\No156 - QuestWorld'},
            "No167":
                {"title": "LONELY FLOATER",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\No167 Lonely Floater (Omama)'},
            "No177":
                {"title": "PLANET Z3",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\No177 - Plant Z3'},
            "No183":
                {"title": "DREAM MACHINES",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\No183 Dream machines'},
            "No186":
                {"title": "ELECTRIC REGGAE",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\No186 Electric Reggae'},
            "No199":
                {"title": "PARTY 44",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\6.Mastered\No199 - Party 44'},
            "No200":
                {"title": "EYE ABOVE",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\3.In Progress\No200'},
            "Bit8":
                {"title": "CAFE AU PLANET Z3",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\Bit8 planet cafe'},
            "Bit24":
                {"title": "DAM DAM",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\6.Mastered\Bit24 - Damdam'},
            "Bit38":
                {"title": "BUDDHA ACID BELL",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\4.release\Bit38 Buddha Acid Bell'},
            "Bit126":
                {"title": "BITOKANA",
                 "rootDir": r'D:\MakingMusic\Automatic Music Machine\5.released\Bit216 - Bitokana'}
        }

    def set_current_track(self, track_name):
        self.current_track = track_name

    def get_current_track(self):
        return self.track_map[self.current_track]

    def get_composer(self):
        return self.composer

    def get_banner(self):
        return self.banner

    def get_painter(self):
        return self.painter

    def get_map(self):
        return self.track_map


    def get_track(self, track_id=None):
        if track_id is None:
            track = self.get_current_track()
        else:
            track = self.track_map[track_id]
        return track

    def get_title(self, track_id=None):
        return self.get_track(track_id)["title"]

    def get_root_dir(self, track_id=None):
        return self.get_track(track_id)["rootDir"]
