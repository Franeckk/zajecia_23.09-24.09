import os
import time

print('jestem w', os.getcwd())
os.mkdir('new_folder')
time.sleep(2)
os.rename('new_folder', 'newer_folder')
time.sleep(2)
os.rmdir('newer_folder')
time.sleep(2)
print('zrobione')

# os.system(' cmd /c "cd C:\\Users\\frane\Desktop\\\\zajecia_23.09-24.09 "  ')
# os.system(' cmd /c "echo Asia > dane.txt"')

os.system(' cmd /c "cd C:\\Users\\frane\Desktop\\\\zajecia_23.09-24.09   &&   echo Asia > dane.txt"  ')
#wejdz na pulpit i wpisz 'asia' do pliku dane.txt (gdy nie ma takiego pliku to tworzy nowy)

