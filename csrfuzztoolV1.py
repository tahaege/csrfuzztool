#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError


def bilgi():
	print"00000000000000000000000000000000000000000000000"
	print'CyberStrugggleRanger Fuzz Aracı'
	print'Programlayan : Taha Ege Aydın'                                                       
	print"00000000000000000000000000000000000000000000000"
	
def fuzzbaslat():

	link = raw_input("Site Adresi \n(http:// kullanmadan):")
	sublink = raw_input("Fuzz Listesinin Dosya Yolu :")
	a = open(sublink,"r");
	print "\n\nBulunan Linkler : \n"

	while True:
		sub_link = a.readline()
		if not sub_link:
			break
		istek_link = "http://"+link+"/"+sub_link
		istek = Request(istek_link)
		try:
			response = urlopen(istek)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
 			print "Bulundu >>",istek_link

bilgi()
fuzzbaslat()
