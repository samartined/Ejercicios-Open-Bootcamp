import time

def get_time():
  """Obtiene la fecha y la hora actuales."""
  return time.localtime()

def display_time():
  """Muestra la fecha y la hora actuales en pantalla."""
  current_time = get_time()
  formatted_date = time.strftime('%d/%m/%Y', current_time)
  formatted_time = time.strftime('%H:%M:%S', current_time)
  print(formatted_date, formatted_time)

def display_message():
  """Muestra un mensaje por pantalla avisando que es hora de volver a casa o cuántas horas quedan todavía de trabajo."""
  current_time = get_time()
  if current_time.tm_hour >= 19:
    print("Es hora de volver a casa!")
  else:
    print("Quedan %d horas para terminar el trabajo." % (24 - current_time.tm_hour))

if __name__ == "__main__":
  display_time()
  display_message()
