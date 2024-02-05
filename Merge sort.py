#นำเข้าไลบรารี Pyglet
from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Rectangle
from pyglet.graphics import Batch
from pyglet import clock
import math

def hex_to_rgb(hex_color):
    return int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16), 255

class Renderer(Window):
    def __init__(self):
        super().__init__(900, 900, "Merge Sort")
        self.batch = Batch()
        self.x = [3, 7, 2, 1, 5, 6, 4]
        self.color = ["#00ff00", "#cd5c5c", "#4b0082", "#f0e68c", "#add8e6", "#F9C04F", "#4FACF9"]
        self.bars = []

        for e, i in enumerate(self.x):
            bar_color = hex_to_rgb(self.color[e])
            self.bars.append(Rectangle(100 + e*100, 100, 80, i*100, color=bar_color, batch=self.batch))

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    def on_update(self, deltatime):
        if not hasattr(self, 'sorted_bars'):
            self.sorted_bars = self.x.copy()
            self.merge_sort(self.sorted_bars)

            self.bars = []
            for e, i in enumerate(self.sorted_bars):
                bar_color = hex_to_rgb(self.color[e])
                self.bars.append(Rectangle(100 + e*100, 100, 80, i*100, color=bar_color, batch=self.batch))

    def on_draw(self):
        self.clear()
        self.batch.draw()

renderer = Renderer()
clock.schedule_interval(renderer.on_update, 3)
run()
