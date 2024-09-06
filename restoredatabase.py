import os
from time import sleep

class restore(object):
    def __init__(self):
        self.file = ('.frm and .ibd folder path ex C:\\database\\') #directory location must be inside single quotes
        self.fileoutput = self.file+"output\\"
        self.listdir = os.listdir(self.file)
        self.listdiroutput = os.listdir(self.fileoutput)

    def cmd_restore(self):
        pathfile = self.listdir
        for i in pathfile:
            if ".frm" in i:
                # Change user and password mysql that running at your machine
                os.system('mysqlfrm --server=root:password@localhost --port=3311 '+self.file+str(i)+' > '+self.fileoutput+str(i.replace(".frm",""))+'.sql')
                print(i)

    def delete_list(self, pathfile):
        list_word = ["#...done."]
        openfile = open(pathfile)
        lines = openfile.readlines()
        for i in range(0,10):
            list_word.append(lines[i])
        openfile.close()
        return list_word

    def delete_text(self, name_file, openfile, savefile):
        delete_list = self.delete_list(openfile)
        with open(openfile) as fin, open(savefile, "w+") as fout:
            for line in fin:
                for word in delete_list:
                    line = line.replace(word, "")
                fout.write(line)
            fin.close()
            fout.close()
        return print('delete')

    def prosess(self):
        for i in self.listdiroutput:
            if '.sql' in i:
                self.delete_text(i,self.fileoutput+str(i),self.fileoutput+str(i).replace('.sql','.txt'))

    def marge(self):
        filenames = []
        for i in self.listdiroutput:
            if '.txt' in i:
                filenames.append(self.fileoutput+str(i))
        with open(self.file+'final.sql', 'w') as outfile:
            for names in filenames:
                with open(names) as infile:
                    outfile.write(infile.read())
                outfile.write("\n")

    def run(self):
        self.cmd_restore()
        sleep(10)
        self.prosess()
