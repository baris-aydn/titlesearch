# 📺 YouTube Channel Video Title CLI

A lightweight command-line tool to **fetch all video titles** from a YouTube channel and **search them interactively** — perfect for archiving or exploring content.

---

## Features

- Extracts **all video titles** from a YouTube channel.
- Search titles with an easy CLI.
- Saves titles to a local `channel_titles.json` file.
- No need to fetch again unless you want to update.

---

## Installation

```bash
pip install yt-dlp

First Time Usage

    ⚠️ Use the full /videos page URL of a YouTube channel.
    Example:
    https://www.youtube.com/@veritasium/videos
    or
    https://www.youtube.com/channel/UCxxxxxx/videos

python youtube_titles_cli.py --url https://www.youtube.com/@CHANNEL_NAME/videos

Subsequent Usage

Just run the CLI to search through previously saved titles:

python youtube_titles_cli.py

    Use the interactive prompt to type search terms.

    Type exit to quit.

Output

    Titles are saved in channel_titles.json

    You can reuse or inspect this file manually if needed.

Notes

    This tool uses yt-dlp with the extract_flat option to quickly and safely fetch metadata without downloading videos.

    Supports both @handle and legacy channel/UCxxxx formats — as long as you append /videos.

this document is created with AI assist.
