import requests
import time

# 1. Your Configurations
LASTFM_API_KEY = "81c0098be9ccd301f3c4d0dcf4f96ebd"
LASTFM_USERNAME = "Magician890"
ESP32_IP = "http://10.0.0.77"  # <-- Replace with your real ESP32 IP address

ESP32_URL = f"{ESP32_IP}/update"
LASTFM_URL = "http://ws.audioscrobbler.com/2.0/"
last_song = ""

print(f"PC Monitor started. Watching Last.fm account: {LASTFM_USERNAME}...")

while True:
    try:
        params = {
            "method": "user.getrecenttracks",
            "user": LASTFM_USERNAME,
            "api_key": LASTFM_API_KEY,
            "format": "json",
            "limit": 1
        }
        res = requests.get(LASTFM_URL, params=params, timeout=5)
        
        if res.status_code == 200:
            track_data = res.json()["recenttracks"]["track"]
            if track_data:
                track = track_data[0] if isinstance(track_data, list) else track_data
                
                is_playing = "@attr" in track and track["@attr"].get("nowplaying") == "true"
                
                if is_playing:
                    song_name = track["name"]
                    artist_name = track["artist"]["#text"]
                    print("🎵 Music is playing...")

                    if song_name != last_song:
                        print(f"📦 Sending Track: {song_name} by {artist_name}")
                        
                        payload = {
                            "song": song_name,
                            "artist": artist_name
                        }
                        
                        esp_res = requests.post(ESP32_URL, json=payload, timeout=5)
                        if esp_res.status_code == 200:
                            print("✅ Successfully pushed to ESP32!")
                            last_song = song_name
                else:
                    if last_song != "Paused":
                        print("⏸️ Music Paused.")
                        requests.post(ESP32_URL, json={"song": "Music Paused", "artist": ""}, timeout=5)
                        last_song = "Paused"
        else:
            print(f"❌ Last.fm API Error: Code {res.status_code}")

    except Exception as e:
        print(f"Network error: {e}")

    time.sleep(7)
