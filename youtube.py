import shutil
import os
from art import *
from tabulate import tabulate
from pytube import YouTube
from pytube.exceptions import AgeRestrictedError
import platform
import time

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
        url = YouTube(GetInput("Lütfen Bir Youtube Linki Girin: "))
        print("Bilgiler getiriliyor, lütfen bekleyin...")
        time.sleep(1)

        print("-"*65)
        print("Video Başlığı:",url.title)
        print("Video Sahibi:",url.author)
        print("İzlenme Sayısı:",url.views)
        print("Video Uzunluğu:",url.length, "saniye")
        print("-"*65)

    except Exception as e:
        print("Bir hata oluştu, lütfen tekrar dene..",e)

    finally:
        print("-"*65)
        ProgramSuresi()

def KucukResimIndirme():
    try:
        url = YouTube(GetInput(" Lütfen Bir Youtube Linki Girin: "))
        print("Resim indiriliyor, lütfen bekleyin..")
        time.sleep(1)

        print("[?] Resim link olarak indirildi, linke tıklayarak resmi görüntüleyebilirsiniz.")
        time.sleep(1)

        print("-"*65)
        print("Video Küçük Resmi:",url.thumbnail_url)
        print("-"*65)

    except Exception as e:
        print("Bir hata oluştu, lütfen tekrar dene..",e)

    finally:
        print("-"*65)
        ProgramSuresi()

def VideoIndirme():
    try:
        url = YouTube(GetInput("Lütfen Bir Youtube Linki Girin: "))
        print("Video İndiriliyor, lütfen bekleyin..")
        time.sleep(1)

        download_path = GetDownloadPath()
        if not os.path.exists(download_path):
            raise Exception("İndirme Dizini Bulunamadı.")
        
        video = url.streams.filter(progressive="True").first()
        if video is None:
            raise Exception("İndirilecek Uygun Video Akışı Bulunamadı.")
        
        video.download(output_path=download_path)

        # Dosyayı Android'un paylaşılan depolama alanına taşı
        shutil.move(os.path.join(download_path, video.default_filename), os.path.join("/storage/emulated/0/Download", video.default_filename))
        print(f"[?] Video İndirme İşlemi Tamamlandı. İndirilen Dizin: /storage/emulated/0/Download/{video.default_filename}")

    except AgeRestrictedError:
        print("[?] Bu videoyu indirmek için Youtube'a giriş yapmanız gerekmektedir.")
        print("[?] Lütfen tarayıcınızdan Youtube'a giriş yapın.")

    except Exception as e:
        print("Bir hata oluştu, lütfen tekrar dene..",e)

    finally:
        print("-"*65)
        ProgramSuresi()

def SesIndirme():
    try:
        url = YouTube(GetInput("Lütfen Bir Youtube Linki Girin: "))
        print("Video sese dönüştürülüyor, lütfen bekleyin..")
        time.sleep(1)

        download_path = GetDownloadPath()
        if not os.path.exists(download_path):
            raise Exception("İndirme Dizini Bulunamadı.")
        
        ses = url.streams.filter(mime_type="audio/mp4").first()
        if ses is None:
            raise Exception("İndirilecek Uygun Ses Akışı Bulunamadı.")
        
        ses.download(output_path=download_path)

        # Dosyayı Android'un paylaşılan depolama alanına taşı
        shutil.move(os.path.join(download_path, ses.default_filename), os.path.join("/storage/emulated/0/Download", ses.default_filename))
        print(f"[?] Videodan Ses Dönüştürme İşlemi Tamamlandı. İndirilen Dizin: /storage/emulated/0/Download/{ses.default_filename}")

    except AgeRestrictedError:
        print("[?] Bu videoyu indirmek için Youtube'a giriş yapmanız gerekmektedir.")
        print("[?] Lütfen tarayıcınızdan Youtube'a giriş yapın.")

    except Exception as e:
        print("Bir hata oluştu, lütfen tekrar dene..",e)

    finally:
        print("-"*65)
        ProgramSuresi()

while True:
    ClearScreen()
    PrintBanner()
    PrintMenu()

    islem = GetInput("Bir işlem seçin (1-5): ")
    if islem == "1":
        VideoBilgiCekme()
    elif islem == "2":
        KucukResimIndirme()
    elif islem == "3":
        VideoIndirme()
    elif islem == "4":
        SesIndirme()
    elif islem == "5":
        print("Çıkış Yapılıyor..")
        break
    else:
        print("Lütfen yapmak istediğiniz işlemi numara ile girin..")
