import os, time

def done():
print '\n[*] run in the new terminal just type "DarkFly"\n'
os.system('cd && rm -rf DarkFly-Tool')

bin = '/data/data/com.termux/files/usr/bin'
file = '.module/'
ngopi = '.menu'
lucu = 'clear >$(tty)'

print '\ainstalling...'
time.sleep(0.9)
os.system('%s' % (lucu))
os.system('apt-get install hydra -y')
os.system('%s && apt-get install php -y' % (lucu))
os.system('mv .module/.hydra $cd %s' % (bin))
os.system('mv .module/readme.txt $cd %s' % (bin))
os.system('python2 %s%s' % (file, ngopi,))
os.system('python2 %s.smp' % (file))
os.system('mv lib %s' % (bin))
os.system('python2 %s.MN' % (file))
os.system('python2 %s.BR' % (file))
done()
os.system('python2 %s.DF' % (file))
os.system('mv .module $cd %s' % (bin))