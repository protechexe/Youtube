import os
from art import *
from termcolor import colored
from tabulate import tabulate
import platform
import time
import yt_dlp as youtube_dl

def ClearScreen():
    os.system("cls" if os.name == "nt" else "clear")

def ProgramSuresi():
    while True:
        islem = GetInput("Devam etmek için entera, çıkış yapmak için 5 e basın: ")
        if islem == "5":
            exit()
        else:
            break

def PrintBanner():
    banner = text2art("Youtube TR", font="big", chr_ignore=True)
    print(banner)
    print("Youtube Paneline Hoş Geldiniz!")
    print("İnstagram: @yuns.eemrree")
    print("-"*65,"\n")
    
def PrintMenu():
    table = [
        ["1","Video Bilgileri Gösterme"],
        ["2","Video Küçük Resim İndirme"],
        ["3","Video İndirme"],
        ["4","Videodan Ses İndirme"],
        ["5","Çıkış"],
    ]

    headers = ["İşlem","Numara"]
    print(tabulate(table, headers, tablefmt="grid"))

def PrintInfo(message):
    print(colored("[INFO] ", "green") + message)

def PrintSuccess(message):
    print(colored("[SUCCESS] ", "light_green") + message)

def PrintError(message):
    print(colored("[ERROR] ", "red") + message)

def GetDownloadPath():
    system = platform.system()
    if system == "Windows":
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "Darwin":
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "Linux":
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "Android":
        return "/storage/emulated/0/Download"
    else:
        raise Exception("Desteklenmeyen Platform")

def GetInput(prompt):
    return input("[?] " + prompt)

def VideoBilgiCekme():
    try:
        url = GetInput("Lütfen Bir Youtube Linki Girin: ")
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'skip_download': True,
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', None)
            video_author = info_dict.get('uploader', None)
            video_views = info_dict.get('view_count', None)
            video_length = info_dict.get('duration', None)

        PrintInfo(f"Video Başlığı: {video_title}")
        PrintInfo(f"Video Sahibi: {video_author}")
        PrintInfo(f"İzlenme Sayısı: {video_views}")
        PrintInfo(f"Video Uzunluğu: {video_length} saniye")

    except Exception as e:
        PrintError("Bir hata oluştu, lütfen tekrar deneyin. " + str(e))

    finally:
        print("-"*65)
        ProgramSuresi()

def KucukResimIndirme():
    try:
        url = GetInput("Lütfen Bir Youtube Linki Girin: ")
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'skip_download': True,
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            thumbnail_url = info_dict.get('thumbnail', None)

        PrintSuccess(f"Video Küçük Resmi: {thumbnail_url}")

    except Exception as e:
        PrintError("Bir hata oluştu, lütfen tekrar deneyin. " + str(e))

    finally:
        print("-"*65)
        ProgramSuresi()

def VideoIndirme():
    try:
        url = GetInput("Lütfen Bir Youtube Linki Girin: ")
        PrintInfo("Video İndiriliyor, lütfen bekleyin..")
        print("-"*65)

        download_path = GetDownloadPath()
        PrintInfo(f"İndirme dizini: {download_path}")
        print("-"*65)

        ydl_opts = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'format': 'best',
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("-"*65)
        PrintSuccess(f"Video İndirme İşlemi Tamamlandı. İndirilen Dizin: {download_path}")

    except Exception as e:
        PrintError("Bir hata oluştu, lütfen tekrar deneyin. " + str(e))

    finally:
        print("-"*65)
        ProgramSuresi()

def SesIndirme():
    try:
        url = GetInput("Lütfen Bir Youtube Linki Girin: ")
        PrintInfo("Video sese dönüştürülüyor, lütfen bekleyin..")
        print("-"*65)

        download_path = GetDownloadPath()
        PrintInfo(f"İndirme dizini: {download_path}")
        print("-"*65)

        ydl_opts = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("-"*65)
        PrintSuccess(f"Videodan Ses Dönüştürme İşlemi Tamamlandı. İndirilen Dizin: {download_path}")

    except Exception as e:
        PrintError("Bir hata oluştu, lütfen tekrar deneyin. " + str(e))

    finally:
        print("-"*65)
        ProgramSuresi()

while True:
    ClearScreen()
    PrintBanner()
    PrintMenu()

    islem = GetInput("Bir işlem seçin (1-5): ")
    if islem == "1":
        PrintInfo("Lütfen Bekleyin..")
        time.sleep(1)
        print("-"*65)
        VideoBilgiCekme()
    elif islem == "2":
        PrintInfo("Lütfen Bekleyin..")
        time.sleep(1)
        print("-"*65)
        KucukResimIndirme()
    elif islem == "3":
        PrintInfo("Lütfen Bekleyin..")
        time.sleep(1)
        print("-"*65)
        VideoIndirme()
    elif islem == "4":
        PrintInfo("Lütfen Bekleyin..")
        time.sleep(1)
        print("-"*65)
        SesIndirme()
    elif islem == "5":
        PrintInfo("Çıkış Yapılıyor..")
        time.sleep(1)
        break
    else:
        print("Lütfen yapmak istediğiniz işlemi numara ile girin..")
