import os
import re
from plexapi.server import PlexServer

def get_user_input(prompt, default=None):
    if default:
        prompt = f"{prompt} [{default}]: "
    else:
        prompt = f"{prompt}: "
    response = input(prompt).strip()
    return response if response else default

def clean_title(filename):
    # Remove season-episode pattern (e.g. S01E01, s01e01, S1E1)
    title = re.sub(r'(?i)s\d{1,2}e\d{1,2}', '', filename)
    # Replace dots with spaces and strip whitespace
    title = title.replace('.', ' ').strip()
    return title

def get_filename_without_extension(media_part):
    path = media_part.file
    base = os.path.basename(path)
    return os.path.splitext(base)[0]

def confirm(prompt="Proceed? (y/n): "):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")

def main():
    plex_url = get_user_input("Enter Plex server URL", "http://localhost:32400")
    plex_token = get_user_input("Enter Plex token")

    plex = PlexServer(plex_url, plex_token)

    # Loop until valid library chosen
    while True:
        library_name = get_user_input("Enter TV library section name", "TV Shows")
        libraries = [lib.title for lib in plex.library.sections()]
        if library_name in libraries:
            break
        print(f"Library '{library_name}' not found. Available libraries:")
        for lib in libraries:
            print(f"  - {lib}")

    library = plex.library.section(library_name)

    # Loop until valid show chosen
    while True:
        show_name = get_user_input("Enter exact TV show name to rename episodes")
        show_titles = [show.title for show in library.all()]
        if show_name in show_titles:
            break
        print(f"Show '{show_name}' not found in library '{library_name}'. Available shows:")
        for title in show_titles:
            print(f"  - {title}")

    print("\nConfiguration:")
    print(f"  Plex URL: {plex_url}")
    print(f"  Library: {library_name}")
    print(f"  Show: {show_name}")

    if not confirm("Proceed with batch renaming? (y/n): "):
        print("Operation cancelled.")
        return

    show = library.get(show_name)
    print(f"Renaming episodes for show: {show.title}")

    for episode in show.episodes():
        media_part = episode.media[0].parts[0]
        raw_title = get_filename_without_extension(media_part)
        new_title = clean_title(raw_title)
        print(f'Renaming episode "{episode.title}" to "{new_title}"')
        episode.editTitle(new_title)

    print("Batch renaming complete.")

if __name__ == '__main__':
    main()
