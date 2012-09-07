#!/usr/bin/env python

import urllib2
import base64
import json
import sys

class RequestWithMethod(urllib2.Request):
    def __init__(self, url, method, headers={}):
        self._method = method
        urllib2.Request.__init__(self, url, headers)

    def get_method(self):
        if self._method:
            return self._method
        else:
            return urllib2.Request.get_method(self) 

if __name__ == "__main__":

	url = 'ENTER_RULES_API_URL_HERE'
	UN = 'ENTER_USERNAME_HERE'
        PWD = 'ENTER_PASSWORD_HERE'

	base64string = base64.encodestring('%s:%s' % (UN, PWD)).replace('\n', '')
	
	req = RequestWithMethod(url, 'GET')
	req.add_header('Content-type', 'application/json')
	req.add_header("Authorization", "Basic %s" % base64string)
	response = urllib2.urlopen(req)
	the_page = response.read()
	print the_page
