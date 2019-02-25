import shutil

BASE_PATH = '/home/jupyter-student_'
directories = []

for num in range(1, 16):
    PATH = BASE_PATH + str(num).rjust(2, '0')
    directories.append(PATH)


for directory in directories:
    dst_dir = f'{directory}/lesson_material'
    try: 
        print('copying to', dst_dir)
        shutil.copytree('lesson_materials', dst_dir)
    except:
        shutil.rmtree(dst_dir)
        print('failed to copy to', dst_dir)
        print('removing old copy')
        shutil.copytree('lesson_materials', dst_dir)
        print('copied!')