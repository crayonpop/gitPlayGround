#-*-coding:cp949 -*-
import os,codecs,sys

global argv1

def proc():
    ## File Searching

    print("Starting...")
    filelist= []
    root = os.path.dirname( os.path.abspath( __file__ ) )

    print("Match File Find Start")
    for (path, dir, files) in os.walk(root):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.php' or ext == '.htm' or ext == '.css' or ext == '.js' or ext == '.html' or ext == '.txt':
                filelist.append(path +"/"+ filename) ## file Path Added

    print("Match File Find End")
    matchReadLine(filelist)

def matchReadLine(list):

	matchFile = []
	for fileList in list:
            	f= codecs.open(fileList , 'r' ,'cp949') ## File Open
            	try:
                		rawText = f.read()
            	except:
                		rawText = f.read().encode('utf-8')

            	if rawText.find(argv1) > 0 :
               		 matchFile.append(fileList+'\n')
              	
              # f.close()

	f = open("fileList.txt", 'w') 

   	for lists in matchFile :
        		f.write(lists)

   	f.close()

   	print("File Saved...")




if __name__ == '__main__':
    argv1 = sys.argv[1]
    proc()

