import yt_dlp
import json
import os

DATA_FILE = "channel_titles.json"


def fetch_titles(channel_url):
    print("[+] Fetching video titles from:", channel_url)
    ydl_opts = {
        'extract_flat': True,
        'force_generic_extractor': False,
        'quiet': True,
        'dump_single_json': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel_url, download=False)
        titles = [entry.get("title") for entry in info.get("entries", []) if entry.get("title")]

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(titles, f, ensure_ascii=False, indent=2)

    print(f"[✓] Saved {len(titles)} titles to {DATA_FILE}")


def load_titles():
    if not os.path.exists(DATA_FILE):
        print("[!] No title data found. Run with a channel URL first.")
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def search_titles(titles, query):
    return [title for title in titles if query.lower() in title.lower()]


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Fetch and search YouTube channel video titles.")
    parser.add_argument("--url", help="YouTube channel URL (only needed the first time).")
    args = parser.parse_args()

    if args.url:
        fetch_titles(args.url)

    titles = load_titles()
    if not titles:
        return

    print("\n🔍 Type a search term to find matching video titles. Type 'exit' to quit.\n")
    while True:
        query = input("Search: ").strip()
        if query.lower() == "exit":
            break
        results = search_titles(titles, query)
        if results:
            print(f"\nFound {len(results)} result(s):")
            for title in results:
                print("•", title)
        else:
            print("No matches found.")
        print()


if __name__ == "__main__":
    main()
