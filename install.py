#!/usr/bin/jembod

import os, time

bin = '/data/data/com.termux/files/usr/bin'
lucu = 'clear >$(tty)'

print '\ainstalling...'
time.sleep(0.9)
os.system('%s' % (lucu))
os.system('apt-get install hydra -y && apt-get install python2')
os.system('clear && apt-get install php -y')
os.system('mv .module/.hydra $cd %s && mv .module/.smp $cd %s' % (bin, bin))
os.system('mv .module/readme.txt $cd %s' % (bin))
os.system('mv .module/.menu $cd %s' % (bin))
os.system('mv lib %s' % (bin))
os.system('python2 .module/.MN')
os.system('python2 .module/.BR')
os.system('python2 .module/.DF')
os.system('mv .module $cd %s' % (bin))
os.system('cd && rm -rf tes')
