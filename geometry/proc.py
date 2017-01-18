import sys
sys.path.append('/Users/chris/repos/delaunay/')

from geometry.primitives import Point

Point(0, 0, 0)


def setup():
    size(600, 600)
    colorMode(HSB)
    noStroke()


def draw():
    fill(0x11000000)
    rect(0, 0, width, height)
    fill(frameCount % 255, 255, 255)
    ellipse(mouseX, mouseY, 20, 20)
    
