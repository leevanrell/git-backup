#!/usr/bin/env python3

import os
import sys
import zipfile
from datetime import datetime

SOURCE_DIRS = [f'/home/{name}/git' for name in os.listdir('/home/') if os.path.isdir(f'/home/{name}/git')]
BACKUP_DIR = '/var/backups/git/'
BACKUP_COUNT = 10

if len(SOURCE_DIRS) < 1:
	print('No git folder found!')
	sys.exit(1)

if not os.path.isdir(BACKUP_DIR):
	os.mkdir(BACKUP_DIR)

def main():
	FILE_NAME = datetime.today().strftime('%Y-%m-%d') + '.zip'
	FULL_BACKUP_PATH = BACKUP_DIR + FILE_NAME
	if not os.path.isfile(FULL_BACKUP_PATH):
		try:
			with zipfile.ZipFile(FULL_BACKUP_PATH, 'w') as zf:
				for SOURCE_DIR in SOURCE_DIRS:
					for root, dirs, files in os.walk(SOURCE_DIR):
						for file in files:
							zf.write(os.path.join(root, file))
		except Exception as e:
			import traceback
			traceback.print_exc(file=sys.stdout)

	files = os.listdir(BACKUP_DIR)
	if len(files) > BACKUP_COUNT and BACKUP_COUNT > 0:
		files = sorted(
			files,
			key=lambda x: datetime.strptime(x, '%Y-%m-%d.zip')
		)
		try:
			for i in range(len(files) - BACKUP_COUNT):
				os.remove(BACKUP_DIR + files[i])
		except Exception as e:
			import traceback
			traceback.print_exc(file=sys.stdout)
