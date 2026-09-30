import requests


def fetch_thumbnail_response(video_id):
    """Return a JSON-safe thumbnail URL for the requested YouTube video."""
    if not video_id:
        return None

    thumbnail_url = f"https://i.ytimg.com/vi/{video_id}/mqdefault.jpg"
    try:
        response = requests.get(thumbnail_url, timeout=10)
        response.raise_for_status()
        return thumbnail_url

    except requests.exceptions.RequestException as e:
        print(f"Error downloading the thumbnail: {e}")
        return None

 