from glob import glob

pth = "/home/r/Рабочий_стол/Python/dave_grohl_detection/annotations/xmls/"

gl = glob(pth+"*.xml")

with open("annotations/trainval.txt", "w") as f1:
    for g in gl:
        fin_name = g.split('/')[-1].split('.xml')[0]
        f1.writelines(fin_name + '\n')
        print(fin_name)

