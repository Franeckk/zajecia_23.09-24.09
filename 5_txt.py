path = ('my_file (1).txt')
mode = 'r'
with open(path,mode) as moj_plik:
# content1= moj_plik.read()    #przeczyta wszystko
# content2_1 = moj_plik.read(5)       #czytamy 5 pierwszych
# content2_2 = moj_plik.read(5)\
    content3 = moj_plik.readlines()

print(content3)
print(type(content3))