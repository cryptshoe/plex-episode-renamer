# Plex Episode Renamer

This Python script batch-renames episodes in a specified Plex TV show to match their file names instead of the default metadata from TVDB.

## Features

- Connects to your Plex server using a Plex token.
- Verifies the existence of the target library and show.
- Renames episode titles in Plex to the corresponding media file names.
- Interactive prompts for all necessary details.

## Prerequisites

- Python 3.7 or higher
- `plexapi` Python package (`pip install plexapi`)

## Usage

1. Run the script:
```
python plex-episode-renamer.py
```

2. Follow the interactive prompts:

- Enter your Plex server URL (e.g. `http://localhost:32400`)
- Enter your Plex token (see instructions below)
- Specify the TV library section name (default is `TV Shows`)
- Specify the exact TV show name to rename episode titles

3. Confirm the operation to start batch renaming.

## How to Get Your Plex Token

1. Open the Plex Web app by navigating to `http://YOUR_PLEX_SERVER_IP:32400/web` and sign in.

2. Click on any media item in your library, then click the three dots (context menu) and select **Get Info**.

3. In the info panel, click **View XML**.

4. Look at the URL in your browser’s address bar of the XML page. It contains a parameter `X-Plex-Token=`, followed by your token string.

5. Copy the token string (everything after `X-Plex-Token=`) for use in the script.

## Notes

- Ensure the token you use has appropriate access to the Plex server.
- The script modifies Plex metadata directly; use with caution.
- Back up your Plex database if needed before bulk operations.
