import os
import time
#
# ####### PROVERKA NAHODJAWEISJA DIRIKTORII
print(os.getcwd())
#
# ####### IZMENENIE NAHOWDENIJA DIRIKTORII
# os.chdir('folder_test')
# print(os.getcwd())
#

# ######## POLUCHENIE ZAIMINOVANIE FAILOV V PAPKE
print(os.listdir())
# # # # #
# # # # # ##### Dlja sozdanija diriktorij(sozdaet 1 raz)
# # # # # # os.mkdir('news_folder\\news_folder3')
# # # # #
# # # # # os.makedirs('new5', exist_ok=True)
# # # # # os.makedirs('new1/new2.new3/new4', exist_ok=True)
# # # # #
# # # # # time.sleep(7)
# # # # ##### Udaljaet poslenjuju direktoriju ( esli ona pustaja)
# # # # # os.rmdir('new1/new2.new3/new4')
# # # # #
# # # # # ######### Udaljaet vse
# # # # # os.removedirs('new1/new2.new3/new4')
# # # # ########## Udalenie faily v papke
# # # # # os.remove('new5')
# # # #
# # # # ### Rename filesa and remove by "/"
# # # # # os.rename('new5', 'new8')
# # # #
# # # # ####### posmotret info i razmer faila
# # # # # print(os.stat('news_folder').st_size)
# # # #
# # # # ########### Prohodit po vsem vozmozhnym deriktorijam
# # # # # print(os.walk(''))
# # # # # print(list(os.walk('../')))
# # # #
# # # # dir_info = os.walk(os.getcwd())
# # # # # dir_info = os.walk(os.getcwd('C:\\'))
# # # #
# # # for dirpath, dirname, filename in dir_info:
# # # #     print('Current path:', dirpath)
# # # #     print('Directories', dirname)
# # # #     print('Files', filename)
# # #
# # # for file in filename:
# # # print(os.path.join(dirpath, filename))
# # #
# # #
# # # ########### perecheslenie i poluchenii info system
# # # # print(os.environ)
# # # ########3 vyborochboe
# # # # print(os.environ()
# # # print(os.getenv('HOMEDRIVE'))
# # #
# # # ################# always'/' if u change
# # # file_path = os.getenv('HOMEDRIVE') + '/test.txt'
# # # print(file_path)
# #
# # ###### join sobiraet
# # # file_path = os.path.join(os.getenv('HOMEDRIVE'), 'test.txt')
# # # print(file_path)
# #
# # ######## dirname razryvaet i vernet direktoriju
# # print(os.path.dirname('C:/allaa/tester.py'))
# # ######## vernet vse
# # print(os.path.split('C:/agara/tester.py['[1]))
# # ######## rasshitrenie faila
# # print(os.path.splitext('C:/agara/tester.py'))
# #
# # print(os.path.splitdrive('C:/dasdas/tester.py'))
#
# ######## proverka na nalichie direktorij ili failov TRUE OR FALSE
# print(os.path.exists('C:/'))
# print(os.path.exists('C:/dfasfasdasd/tester.py'))
#
# ######### javljaetsja li nastojashej direktoriej
# print(os.path.isdir('C:\\asasas'))
# ######## proverka failov
# print(os.path.isfile('news_folder'))
#
# Check
# print(dir)
# print(dir(os.path))
##### dobratsja do opredelennyh failov
for file in os.listdir():
    if os.path.isfile(file) and os.path.splitext(file)[1]== '.txt':
        print(file)

print(os.getlogin())