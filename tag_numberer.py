#!/usr/bin/env python  
import os

#start = 381
#end = 462

#end += 1

list_ = [15,16,33,34,53,72,73]

#for i in range(start,end):
for i in list_:

	print i

	"""
	tag = str(i)
	tag_quoted = '"'+tag+'"'+"'"
	os.system('./chilitags-creator ' + tag + ' 56')
	os.system("convert -pointsize 12 -fill black -draw 'text 392,740 " + tag_quoted +' '+tag+'.png '+ tag + '_numbered.png')
	os.system('convert ' + tag + "_numbered.png " + tag + "_numbered.pdf")
	os.system("./cpdf remaining.pdf " + tag + "_numbered.pdf -o remaining.pdf" )
	os.system('mv ' + tag + '_numbered.pdf ./pdf_versions')
	os.system('mv ' + tag + '.png ./raw_tags')
	os.system('mv ' + tag + '_numbered.png ./numbered_tags')
	"""

