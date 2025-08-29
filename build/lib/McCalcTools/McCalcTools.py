import math

def calcstuck (items):
    stuck = items // 64
    return stuck

def calcchunk (blocks):
    chunk = blocks // 16
    return chunk 

def realsize (blocks, range):
    meters = (20 * blocks)*range
    return meters

def blocksize (meters, range):
    blocks = (meters / 20) / range
    return blocks

def blockvolume (lenght, width, height):
    volume = lenght * width * height
    return volume

def circunference (diameter):
    circunference = round(2 * math.pi * (diameter / 2))
    return circunference

def area (lenght,height,range):
    area = (lenght * 20) * (height * 20) / range
    return area