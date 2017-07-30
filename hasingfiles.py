import hashlib
import sys

f = open(sys.argv[1], 'rb')
h = open(sys.argv[2], 'rb')

data1 = f.read()
data2 = h.read()	

file1MD5 = hashlib.md5(data1).hexdigest()
file1SHA1 = hashlib.sha1(data1).hexdigest()
file1SHA256 = hashlib.sha256(data1).hexdigest()

print '[1] MD5 : ' + file1MD5
print '[1] SHA-1 : ' + file1SHA1
print '[1] SHA-256: ' + file1SHA256

file2MD5 = hashlib.md5(data2).hexdigest()
file2SHA1 = hashlib.sha1(data2).hexdigest()
file2SHA256 = hashlib.sha256(data2).hexdigest()

print '[2] MD5 : ' + file2MD5
print '[2] SHA-1 : ' + file2SHA1
print '[2] SHA-256: ' + file2SHA256

if (file1MD5 == file2MD5 and file1SHA1 == file2SHA1 and file1SHA256 == file2SHA256):
	print "Two images are exactly same!!"

else:
	print "Two images are not same!!"


