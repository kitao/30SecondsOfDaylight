import pyxel


class DaylightControl:
    DAYLIGHT_SECS = 30
    MAX_SECS = DAYLIGHT_SECS * 2

    def __init__(self):
        self.frame_cnt = 0
        self.sec_cnt = 0

    def update(self, world):
        # 0-27 = day = all normal tile colours
        # 28 = early dusk = all orange except nearest
        # 29 = late dusk = all dark red except nearest
        # 30-57 = night = all dark blue except nearest
        # 58 = early dawn = all dark red except nearest
        # 59 = late dawn = all orange except nearest

        self.frame_cnt += 1
        if self.frame_cnt == 10:
            self.frame_cnt = 0
            self.sec_cnt += 1
            if self.sec_cnt == self.MAX_SECS:
                self.sec_cnt = 0

        if self.frame_cnt == 0:
            if self.sec_cnt == 29:  # night time spooky music
                pyxel.playm(2, loop=False)
            elif self.sec_cnt == 58:  # happy end of night
                pyxel.playm(3, loop=False)
            elif self.sec_cnt == 0:
                pyxel.playm(1, loop=False)

        if self.sec_cnt > 29 and self.sec_cnt < 58:
            for i in range(2, 16):
                pyxel.pal(i, 1)
        elif self.sec_cnt == 28 or self.sec_cnt == 59:
            for i in range(2, 16):
                pyxel.pal(i, 9)
        elif self.sec_cnt == 29 or self.sec_cnt == 58:
            for i in range(2, 16):
                pyxel.pal(i, 2)

    def is_night(self):
        if self.sec_cnt >= 0 and self.sec_cnt <= 27:
            return False
        else:
            return True
