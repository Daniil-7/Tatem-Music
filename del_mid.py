import os
from time import time


def del_mid_def():
	dir_mid = os.listdir(path="./static/")
	for i in dir_mid:
		if len(i.split('__')) == 3:
			m = (int(i.split('__')[2].split('.')[0]) - int(time())) * -1
			if m > 1800:
				os.remove('./static/' + i)
