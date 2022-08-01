import requests
import zippyshare_downloader
input = open("asmr-url.txt", "r+")
err_log = open("error.log", "w+")
placer = True
while placer:
    url_orig = input.readline().strip('\n')
    if url_orig == "":
        print("Download ended.")
        break
    url_zippy = requests.get(url=url_orig).url
    if ("japaneseasmr" in url_zippy):
        print("Download Failed: No source available " + url_orig)
        err_log.write(url_orig + '\n')
        continue
    try:
        zippyshare_downloader.download(url_zippy)
    except BaseException:
        print("Download Failed: File deleted or banned " + url_orig)
        err_log.write(url_orig + '\n')
    else:
        print("Download successfully " + url_orig)
input.close()
err_log.close()
