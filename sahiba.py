import pygame
import time
import sys

# Ensure proper encoding for Hindi lyrics
sys.stdout.reconfigure(encoding='utf-8')

# 🔊 Path to your Sahiba audio file (.wav format)
wav_path = "C:\\Users\\Asus\\OneDrive\\Documents\\Audacity\\Sahiba.wav"

# 🎶 Updated lyrics (line-by-line display)
lyrics_lines = [
    "Teri talab mujhko, teri talab jaana ho tu kabhi rubru",
    "Shor sharaba jo seene mein hai mere, kaise byaan main karun",
    "Haal jo mera hai, main kisko bataun mere sahiba",
    "Dil na kiraye ka, thoda toh sambhalo na",
    "Naazuk hai yeh, toot jata hai",
    "Sahiba neendein veendein aaye na",
    "Raatein kaati jaye na",
]

# ⏱️ Delay between lines (adjust to match song pacing)
delay = 5.7

# Initialize mixer and play song
pygame.mixer.init()
try:
    pygame.mixer.music.load(wav_path)
    pygame.mixer.music.play()
    print("\n🎶 Now Playing: Sahiba\n")
    print("📝 Lyrics (synchronized):\n")

    for line in lyrics_lines:
        print(line)
        time.sleep(delay)

    print("\n✅ Lyrics finished.")
    while pygame.mixer.music.get_busy():
        time.sleep(1)

except pygame.error as e:
    print(f"⚠️ Error loading song: {e}")
    