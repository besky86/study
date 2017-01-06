import time
import os.path
from string import Template
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']


class BatchRename(Template):
    delimiter = '%'

fmt = raw_input('Enter rename style (%d-date %n-seqnum %f-format):  ')

t = BatchRename(fmt)
import pdb
pdb.set_trace()
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    print base,
    newname = t.substitute(d=date, n=i, f=ext)
print '{0} --> {1}'.format(filename, newname)
