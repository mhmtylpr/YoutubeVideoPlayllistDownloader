from pytube import YouTube
from pytube import Playlist
print("___   ___            ___   ___    ___      ___    ")
print("| |   | |   ______   \  \ /  /    \  \    /  /  ")
print("| |   | |   ______    \ \/  /      \  \  /  /    ")
print("| |___| |               | |         \  \/  /   ")
print("---------               ---          ------         ")
print("\n")
print("Yapacağınız işlemi seçiniz :")
print("1)Oynatma listesi indirme")
print("2)Video indirme")

### Oynatma listesi linki eklenmediğinde hata verecek (ekle)
while True:
    try:
        sec = input("Seçiminiz: ")
        sec = int(sec)
        break
    except:
        print("lütfen 1 ya da 2 sayısını seçiniz...")
if sec == 1:
    while True:
        try:
            my_playlist = input("Oynatma listesi linki:")
            p = Playlist(my_playlist)
            break
        except:
            print("Lütfen oynatma listesinin linkini giriniz...")

    while True:
        try:
            votes = input("Link doğrumu ? (e/h): ")
            if votes not in ("eh"):
                print("lütfen e yada h harfini giriniz: ")
            elif votes in "e":
                break
            elif votes in "h":
                print("bizi kullandığınız için teşekkürler :)")
                break
        except:
            pass
    if votes == "e":
        print("1)360p \n2)720p" )
        resoltions = input("Videonuz hangi çözünürlükte indirilsin(1/2): ")
        if resoltions == "1":
            video_num = 1
            for video in p.video_urls:
                print(f"{video_num}.Video : {YouTube(video).title} - İndiriliyor.")
                YouTube(video).streams.filter(progressive="True", mime_type="video/mp4", res="360p").first().download()
                print(f"{video_num}.Video : {YouTube(video).title} - İndi.")
                video_num += 1
        elif resoltions == "2":
            for video in p.video_urls:
                video_num1 = 1
                print(f"{video_num1}.Video : {YouTube(video).title} - İndiriliyor.")
                YouTube(video).streams.filter(progressive="True", mime_type="video/mp4", res="720p").first().download()
                print(f"{video_num1}.Video : {YouTube(video).title} - İndi.")
                video_num1 += 1
        else:
            pass
elif sec == 2:
    while True:
        try:
            link = input("Videonun linki: ")
            break
        except:
            print("Lütfen videonun linkini giriniz...")
    while True:
        try:
            vote = input("e/h")
            if vote not in ("Link doğrumu ? (e/h): "):
                print("lütfen e yada h harfini giriniz: ")
            elif vote in "e":
                break
            elif vote in "h":
                print("bizi kullandığınız için teşekkürler :)")
                break
        except:
            pass
    if vote == "e":
        print("1)360p \n2)720p" )
        resoltion = input("Videonuz hangi çözünürlükte indirilsin(1/2): ")
        if resoltion == "1":
            print(f"İndirilecek olan video: {str(YouTube(link).title)}")
            YouTube(link).streams.filter(progressive="True", mime_type="video/mp4", res="360p").first().download()
            print(f"Video: {str(YouTube(link).title)} - İndi.")
        if resoltion == "2":
            print(f"İndirilecek olan video: {str(YouTube(link).title)}")
            YouTube(link).streams.filter(progressive="True", mime_type="video/mp4", res="720p").first().download()
            print(f"Video: {str(YouTube(link).title)} - İndi.")
        else:
            pass






