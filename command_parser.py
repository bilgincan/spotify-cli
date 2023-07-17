import argparse
from commands.authorization import login, logout
from commands.play import *
from commands.queue import *


def main():
    parser = argparse.ArgumentParser(description='Spotify command line interface')
    subparsers = parser.add_subparsers(dest='command')

    # Authorization commands
    login_parser = subparsers.add_parser('login', help='Proceed login and save credentials')
    login_parser.set_defaults(func=login)

    logout_parser = subparsers.add_parser('logout', help='Logout from Spotify')
    logout_parser.set_defaults(func=logout)

    # Play commands
    pause_parser = subparsers.add_parser('pause', help='Pause current song')
    pause_parser.set_defaults(func=pause)

    resume_parser = subparsers.add_parser('resume', help='Resume current song')
    resume_parser.set_defaults(func=resume)

    play_parser = subparsers.add_parser('play', help='Play a song')
    play_parser.add_argument('song', help='Song name')

    play_playlist_parser = subparsers.add_parser('playlist', help='Play a playlist')
    play_playlist_parser.add_argument('playlist', help='Playlist name')

    play_genre_parser = subparsers.add_parser('genre', help='Play a genre')
    play_genre_parser.add_argument('genre', help='Genre name')

    get_current_song_parser = subparsers.add_parser('current_song', help='Get current song')
    get_current_song_parser.set_defaults(func=get_current_song)

    shuffle_parser = subparsers.add_parser('shuffle', help='Shuffle current playlist')
    shuffle_parser.set_defaults(func=shuffle)

    next_parser = subparsers.add_parser('next', help='Play next song')
    next_parser.set_defaults(func=next)

    previous_parser = subparsers.add_parser('previous', help='Play previous song')
    previous_parser.set_defaults(func=previous)

    add_item_parser = subparsers.add_parser('add_item', help='Add item to queue')
    add_item_parser.add_argument('item', help='Item name')

    show_queue_parser = subparsers.add_parser('show_queue', help='Show queue')
    show_queue_parser.set_defaults(func=show_queue)

    args = parser.parse_args()

    if args.command == 'play':
        play(args.song)
        return

    if args.command == 'playlist':
        play_playlist(args.playlist)
        return

    if args.command == 'genre':
        play_genre(args.genre)
        return
    
    if args.command == 'add_item':
        add_item(args.item)
        return

    args.func()


if __name__ == '__main__':
    main()