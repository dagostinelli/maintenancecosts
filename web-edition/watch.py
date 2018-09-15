import os
import pyinotify
import functools
from subprocess import call

wm = pyinotify.WatchManager()
notifier = pyinotify.Notifier(wm)

mask = pyinotify.IN_CLOSE_WRITE

wm.add_watch('book/', mask)

def on_event(notifier, stuff):
	call(["make", "build"])

on_loop_func = functools.partial(on_event, stuff=dict())

notifier.loop(callback=on_loop_func)
