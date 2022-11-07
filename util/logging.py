import sys, pygame, datetime

###########################
logDebugToConsole = True
###########################

f = open("latest.log", "w")
# Overwrite file
f.write("")
f.close()

f = open("latest.log", "a")


def __log__(string):
    print("[NovaLog] " + string)
    f.write("\n" + string)


def info(string):
    __log__("[INFO] " + string)


def warning(string):
    __log__("[WARNING] " + string)


def error(string):
    __log__("[ERROR] " + string)


def debug(string):
    if logDebugToConsole:
        __log__("[DEBUG] " + string)
    else:
        f.write("\n[DEBUG]" + string)


info("NovaLog initialized")
info("Created log file at " + str(datetime.datetime.now()) + " - Running on Python " +
     str(sys.version_info[0]) + "." + str(sys.version_info[1]) + " on " + sys.platform + " with pygame " + pygame.version.ver)
