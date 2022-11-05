def __log__(string):
  print("[NovaLog] " + string)

def info(string):
  __log__("[INFO] " + string)

def warning(string):
  __log__("[WARNING] " + string)

def error(string):
  __log__("[ERROR] " + string)