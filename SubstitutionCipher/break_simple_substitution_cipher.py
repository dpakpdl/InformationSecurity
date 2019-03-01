import random
import re

from pycipher import SimpleSubstitution as SimpleSub

from ngram_score import NgramScore

# load our quadgram statistics
fitness = NgramScore('english_quadgrams.txt')

ctext = 'pmpafxaikkitprdsikcplifhwceigixkirradfeirdgkipgigudkcekiigpwrpucikceiginasikwduearrxiiqepcceindgmieinpwdfprduppcedoikiqiasafmfddfipfgmdafmfdteiki'

ctext = re.sub('[^A-Z]', '', ctext.upper())

max_key = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
max_score = -99e9
parent_score, parent_key = max_score, max_key[:]
print "Substitution Cipher solver, you may have to wait several iterations"
print "Press ctrl+c to exit program."
i = 0
while 1:
    i = i + 1
    random.shuffle(parent_key)
    deciphered = SimpleSub(parent_key).decipher(ctext)
    parent_score = fitness.score(deciphered)
    count = 0
    while count < 1000:
        a = random.randint(0, 25)
        b = random.randint(0, 25)
        child = parent_key[:]
        # swap two characters in the child
        child[a], child[b] = child[b], child[a]
        deciphered = SimpleSub(child).decipher(ctext)
        score = fitness.score(deciphered)
        # if the child was better, replace the parent with it
        if score > parent_score:
            parent_score = score
            parent_key = child[:]
            count = 0
        count = count + 1
    # keep track of best score seen so far
    if parent_score > max_score:
        max_score, max_key = parent_score, parent_key[:]
        print '\nbest score so far:', max_score, 'on iteration', i
        ss = SimpleSub(max_key)
        print '    best key: ' + ''.join(max_key)
        print '    plaintext: ' + ss.decipher(ctext)
