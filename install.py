#!/usr/bin/jembod

import os, sys

bin = '/data/data/com.termux/files/usr/bin'

print 'installing...'
os.system('apt-get install hydra -y && apt-get install python2')
os.system('clear && pt-get install php -y')
os.system('mv .module/.hydra $cd %s && mv .module/.spm $cd %s' % (bin, bin))
os.system('mv .module/readme.txt $cd %s' % (bin))
os.system('cp lib %s' % (bin))
os.system('python2 .module/.MN')
os.system('python2 .module/.BR')
os.system('python2 .module/.DF')
os.system('mv .module $cd %s' % (bin))
os.system('cd && rm -rf tes')
