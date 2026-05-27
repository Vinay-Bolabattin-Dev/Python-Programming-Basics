# Save this file as render_helper.py

def clean_filename(title):
    """
    Takes a messy project title and formats it cleanly 
    for an Instagram reel asset.
    """
    return title.lower().replace(" ", "_") + "_edited.mp4"
