import zipfile

with zipfile.ZipFile('workbook.zip', 'r') as zip_file:
	count = 0
	for i in zip_file.infolist():
		if not i.is_dir():
			count += 1
	print(count)
