import keyboard
import os

def open_spotify():
    os.system("start spotify")

def close_spotify():
    os.system("taskkill /f /im spotify.exe")

def hotkey_event():
    close_spotify()
    open_spotify()

keyboard.add_hotkey('ctrl+alt+s', hotkey_event)

print("Drücke Strg + Alt + S, um Spotify zu öffnen und zu schließen.")
keyboard.wait('esc')

# Program to restart Spotify automatically, to bypass ads / in dev...


