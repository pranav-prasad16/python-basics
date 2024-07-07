import json
import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL)
''')

def list_all_videos():
    print('\n')
    print('*' * 50)
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print('No data in the table')
    print('*' * 50)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    if cursor.rowcount>0:
        print('Video added to db successfully')
    else:
        print('Video not added to db')
    conn.commit()

def update_video_details(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    if cursor.rowcount>0:
        print(f'Video with the id: {video_id} updated successfully')
    else:
        print(f'No video with the id: {video_id} found')
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id, ))
    if cursor.rowcount>0:
        print(f'Video with the id: {video_id} deleted successfully')
    else:
        print(f'No video with the id: {video_id} found')
    conn.commit()
    

def main():
    while True:
        print('\n Youtube Manager | choose an option :')
        print('1. List all youtube videos')
        print('2. Add a youtube video')
        print('3. Update a youtube video details')
        print('4. Delete a youtube video')
        print('5. Exit the app')
        # print(videos)
        print('\n')
        choice = input('Enter your choice: ')

        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input('Enter video name: ')
                time = input('Enter video time: ')
                add_video(name, time)
            case '3':
                video_id = input('Enter the video Id to be updated: ')
                name = input('Enter the new video name: ')
                time = input('Enter the new video time: ')
                update_video_details(video_id, name, time)
            case '4':
                video_id = input('Enter the video Id to be deleted: ')
                delete_video(video_id)
            case '5':
                break
            case _:
                print('Invalid Choice')

    conn.close()

if __name__ == '__main__':
    main()