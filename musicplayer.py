import pygame

def play_music(file_path):
    pygame.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
def pause_music():
    try:
        pygame.mixer.music.pause()
    except Exception as e:
        print("Error:", e)

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def setvolumelevel(level):
    pygame.mixer.music.set_volume(float(level))