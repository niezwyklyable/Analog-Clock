
from datetime import datetime
import pygame
from constants import BLACK, GREEN, RADIUS, GRAD, BLUE, WHITE, RED
import math

class Clock():
    def __init__(self, win):
        self.win = win
        self.center = (self.win.get_width() // 2, self.win.get_height() // 2)
        self.sec_ind_len = int(0.8 * RADIUS)
        self.min_ind_len = int(0.55 * RADIUS)
        self.hour_ind_len = int(0.3 * RADIUS)

    def get_time(self):
        datetime_obj = datetime.now()
        time = datetime_obj.strftime('%H:%M:%S')
        return time.split(':') # zwraca liste stringow

    def get_hours(self):
        hours = int(self.get_time()[0])
        return hours
        
    def get_mins(self):
        mins = int(self.get_time()[1])
        return mins

    def get_secs(self):
        secs = int(self.get_time()[2])
        return secs

    def update(self):
        secs = self.get_secs()
        mins = self.get_mins()
        hours = self.get_hours()
        self.win.fill(BLACK)
        self.draw_frame()
        self.draw_clock_face()
        self.draw_seconds_indicator(secs)
        self.draw_minutes_indicator(mins, secs)
        self.draw_hours_indicator(hours, mins, secs)
        pygame.display.update()

    def draw_frame(self):
        width = self.win.get_width()
        height = self.win.get_height()
        pygame.draw.rect(self.win, WHITE, (0, 0, width - 1, height - 1), width = 4)

    def draw_clock_face(self):
        pygame.draw.circle(self.win, GREEN, self.center, RADIUS, width=2)

        for alfa in [i*30 for i in range(12)]:
            sin_alfa = math.sin(math.radians(alfa))
            cos_alfa = math.cos(math.radians(alfa))
            pygame.draw.line(self.win, GREEN, \
               (self.center[0] + int((RADIUS - GRAD - 1) * cos_alfa), self.center[1] + int((RADIUS - GRAD - 1) * sin_alfa)), \
               (self.center[0] + int((RADIUS - 1) * cos_alfa), self.center[1] + int((RADIUS - 1) * sin_alfa)), \
               width=2)

    def draw_seconds_indicator(self, secs):
        alfa = secs / 60 * 360 - 90
        sin_alfa = math.sin(math.radians(alfa))
        cos_alfa = math.cos(math.radians(alfa))
        pygame.draw.line(self.win, BLUE, \
            self.center, \
            (self.center[0] + int((self.sec_ind_len - 1) * cos_alfa), self.center[1] + int((self.sec_ind_len - 1) * sin_alfa)), \
            width=2)

    def draw_minutes_indicator(self, mins, secs):
        alfa = mins / 60 * 360 + (secs / 60) / 60 * 360 - 90
        sin_alfa = math.sin(math.radians(alfa))
        cos_alfa = math.cos(math.radians(alfa))
        pygame.draw.line(self.win, WHITE, \
            self.center, \
            (self.center[0] + int((self.min_ind_len - 1) * cos_alfa), self.center[1] + int((self.min_ind_len - 1) * sin_alfa)), \
            width=2)

    def draw_hours_indicator(self, hours, mins, secs):
        if hours >= 12:
            hours -= 12

        alfa = hours / 12 * 360 + (mins / 60) / 12 * 360 + (secs / 60) / 60 / 12 * 360 - 90
        sin_alfa = math.sin(math.radians(alfa))
        cos_alfa = math.cos(math.radians(alfa))
        pygame.draw.line(self.win, RED, \
            self.center, \
            (self.center[0] + int((self.hour_ind_len - 1) * cos_alfa), self.center[1] + int((self.hour_ind_len - 1) * sin_alfa)), \
            width=2)
