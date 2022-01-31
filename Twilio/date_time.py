from datetime import datetime


def get_now():
	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	return(dt_string)