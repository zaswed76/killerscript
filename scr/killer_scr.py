import psutil
import time



from log import logger

log = logger()
def main():
    for process in psutil.process_iter():
        try:
            proc = process.cmdline()
        except (psutil._exceptions.AccessDenied, psutil._exceptions.NoSuchProcess):
            pass
        else:
            for p in proc:
                if "chromedriver" in p:
                    process.terminate()
                    log.warning("chromedriver exit")
                    time.sleep(5)
                if "chrome" in p:
                    if "--test-type=webdriver" in proc:
                        process.terminate()
                        log.warning("chrome exit")
                    else:
                        log.debug("{}\nchrome not exit".format(p))
                if "stat3" in p:
                    log.warning("{}\nstat3 exit")
                    process.terminate()

main()




