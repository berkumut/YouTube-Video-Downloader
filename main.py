import os
import yt_dlp

# EKRANA YAZDIRIR
print(""" ENTER A VALİD NUMBER :

    1- VİDEO DOWNLOADER 
    2- EXİT
""")

# REQUESTS SELECTION FROM THE USER
try:

    choice = int(input("Pick a number : "))

except ValueError:

    print("Please enter a valid value")
    exit()

# DOWNLOAD BAR
def progress_hooks(d):
    if d["status"] == "downloading":
        percent = d["_percent_str"]
        print(percent, end="\r")

# IT LOOKS AT THE USER'S SELECTION AND CONTINUES THE PROCESS
if choice==1:
    
    url = input("Enter your url : ")
    print("Video is downloading...")


    save_path = os.path.join(os.getcwd(), "downloads")
    os.makedirs(save_path, exist_ok = True)


    # VIDEO SETTİNGS
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(save_path, '%(title)s %(id)s.%(ext)s'),
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        'progress_hooks': [progress_hooks],
    }

# REMOVE IF IT'S WRONG
elif choice==2:
    print("Exiting...")
    exit()

# WARNS IF USER DOES NOT RATE THE EVALUATION
else:
    print("Please enter a valid value")
    exit()

# DOWNLOAD BEGINS
try :

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

except yt_dlp.utils.DownloadError as error:
    print(f"An error occured please try again {error}")

