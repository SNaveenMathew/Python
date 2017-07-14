from sys import argv
from time import sleep
#from logging import basicConfig, INFO, getLogger, Formatter, FileHandler
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print event.event_type, event.src_path

    def on_deleted(self, event):
        print event.event_type, event.src_path

    def on_created(self, event):
        print event.event_type, event.src_path

if __name__ == "__main__":
    # basicConfig(level=INFO,
    #            format='%(asctime)s - %(message)s',
    #            datefmt='%Y-%m-%d %H:%M:%S',
    #            filename="log.txt")
    #logger = getLogger('file_watch')
    #hdlr = FileHandler('log.txt')
    #formatter = Formatter('%(asctime)s %(message)s')
    # hdlr.setFormatter(formatter)
    # logger.addHandler(hdlr)
    # logger.setLevel(INFO)
    path = argv[1] if len(argv) > 1 else '.'
    #event_handler = LoggingEventHandler()
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            #print watchmedo.observe_with(observer, event_handler, path, True)
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
