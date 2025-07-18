from pytube import Playlist

playlist_url = "https://youtube.com/playlist?list=PLKXJGCmofp0IBb7I6gh3vBBBgUvz2_xVw"

playlist = Playlist(playlist_url)

print("Fetching videos from playlist...\n")

for video in playlist.videos:
    video_id = video.video_id
    title = video.title.replace("\n", " ").strip()
    print(f"{video_id} | {title}")