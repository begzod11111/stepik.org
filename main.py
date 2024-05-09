import json
import zipfile
from zipfile import ZipFile, ZipInfo
from datetime import datetime
import os.path


# 1

# with zipfile.ZipFile('workbook.zip', 'r') as zip_file:
# 	count = 0
# 	for i in zip_file.infolist():
# 		if not i.is_dir():
# 			count += 1
# 	print(count)


# 2

# with ZipFile('workbook.zip', 'r') as zip_file:
# 	info = zip_file.infolist()
# 	print(f"""Объем исходных файлов: {sum(map(lambda x: x.file_size, info))} байт(а)
# Объем сжатых файлов: {sum(map(lambda x: x.compress_size, info))} байт(а)""")

# 3

# def get_compression_ratio(file: zipfile.ZipInfo):
# 	if not file.is_dir():
# 		return (file.file_size - file.compress_size) / file.file_size * 100
# 	return 0
#
#
# with ZipFile('workbook.zip', 'r') as zip_file:
# 	info_files = zip_file.infolist()
# 	best_file = max(info_files, key=lambda x: get_compression_ratio(x)).filename
# 	print(best_file[best_file.index("/") + 1:])


# 4


# res = []


# def get_filename(file_name: str):
# 	if '/' in file_name:
# 		return file_name[file_name.index("/") + 1:]
# 	return file_name


# def datatime_check(file: ZipInfo, verifiable: datetime):
# 	data_time_file = datetime(*file.date_time)
# 	if verifiable < data_time_file:
# 		return True
# 	return False
#
#
# with ZipFile('workbook.zip', 'r') as zip_file:
# 	info_files = zip_file.infolist()
# 	for info_file in info_files:
# 		if not info_file.is_dir():
# 			filename = get_filename(info_file.filename)
# 			verifiable_data = datetime(year=2021, month=11, day=30, hour=14, minute=22)
# 			if datatime_check(info_file, verifiable_data):
# 				res.append(filename)
# 	print(*sorted(res), sep='\n')


# 5

# with ZipFile('workbook.zip', 'r') as zip_file:
# 	file_names = sorted([i for i in zip_file.namelist() if '.' in i], key=get_filename)
# 	for file_name in file_names:
# 		file_info = zip_file.getinfo(file_name)
# 		data_time = datetime(*file_info.date_time).strftime('%Y-%m-%d %H:%M:%S')
# 		print(f'''{get_filename(file_name)}
#   Дата модификации файла: {data_time}
#   Объем исходного файла: {file_info.file_size} байт(а)
#   Объем сжатого файла: {file_info.compress_size} байт(а)
# ''')

# 6

# file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
#               'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
#               'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
#
# with ZipFile('files.zip', mode='w') as zip_file:
#     for file in file_names:
#         zip_file.write(file)


# 7

# file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
#               'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
#               'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
#
#
# def check_size_file(name):
#     if os.path.getsize(name) <= 100:
#         return True
#     return False
#
#
# with ZipFile('files.zip', mode='a') as zip_file:
#     for file_name in file_names:
#         if check_size_file(file_name):
#             zip_file.write(file_name)


# 8

# def extract_this(zip_name, *args):
# 	with ZipFile(zip_name, 'r') as zip_file:
# 		if args:
# 			for file_name in args:
# 				zip_file.extract(file_name)
# 		else:
# 			zip_file.extractall()
#
#
# extract_this('workbook.zip', 'test.py')

# 9

# res = []
#
#
# def is_correct_json(res_):
#     try:
#         res = json.dumps(json.loads(res_))
#         return json.loads(res)
#     except:
#         return False
#
#
# with ZipFile('data.zip', 'r') as zip_file:
#     file_names = zip_file.namelist()
#     for file_name in file_names:
#         file_json = is_correct_json(zip_file.read(file_name))
#         if file_json:
#             if file_json['team'] == 'Arsenal':
#                 res.append(file_json)
#     res = sorted(sorted(res, key=lambda x: x['last_name']), key=lambda x: x['first_name'])
#     for i in res:
#         first_name = i['first_name']
#         last_name = i['last_name']
#         print(f'{first_name} {last_name}')

# 10

# def convert_bytes(size):
# 	"""Конвертер байт в большие единицы"""
# 	if size < 1000:
# 		return f'{size} B'
# 	elif 1000 <= size < 1000000:
# 		return f'{round(size / 1024)} KB'
# 	elif 1000000 <= size < 1000000000:
# 		return f'{round(size / 1048576)} MB'
# 	else:
# 		return f'{round(size / 1073741824)} GB'
#
#
# def print_dir(file_dir: str, file_bytes=None):
# 	file_dir = file_dir.split('/') if '' not in file_dir.split('/') else file_dir.split('/')[:-1]
# 	print("  " * len(file_dir[:-1]) + f'{file_dir[-1]} {file_bytes if file_bytes else ""}')
# #
#
# file_architecture = []
#
# with ZipFile('desktop.zip', 'r') as zip_file:
# 	for name in zip_file.infolist():
# 		if name.filename.startswith('images'):
# 			with open(name) as file:
# 				content = file.read()
# 				print(content)

#
# def get_file_info(file: ZipInfo):
# 	"""Получение информации о файле"""
# 	file_size = convert_bytes(file.file_size)
# 	compress_size = convert_bytes(file.compress_size)
# 	return f'Размер файла: {file_size}, сжатый размер: {compress_size}'
#
#
# def get_file_name(file_name: str):
# 	"""Получение имени файла"""
# 	if '/' in file_name:
# 		return file_name[file_name.index('/') + 1:]
# 	return file_name
#
#
# def has_file(file_name: str, zip_file: ZipFile):
# 	"""Проверка наличия файла"""
# 	try:
# 		zip_file.getinfo(file_name)
# 		return True
# 	except KeyError:
# 		return False
#
#
# def get_file_content(file_name: str, zip_file: ZipFile):
# 	"""Получение содержимого файла"""
# 	with zip_file.open(file_name) as file:
# 		return file.read()
#
#
# with ZipFile('desktop.zip', 'r') as zip_file:
# 	for name in zip_file.infolist():
# 		if name.is_dir():
# 			print_dir(name.filename)
# 		else:
# 			print_dir(name.filename, convert_bytes(name.file_size))


