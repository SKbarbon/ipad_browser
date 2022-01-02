import ui
import os
import requests
import webbrowser
notyP = ui.load_view('NOTIFY_page')
v = ui.load_view('main')
moreP = ui.load_view('more_page')
update_release_chek = r"https://skanvyiscool.000webhostapp.com/pythonistaApps/ipad_browser/update_info.html"
news_for_update = r"https://skanvyiscool.000webhostapp.com/pythonistaApps/ipad_browser/news_info"
url_for_download = r"https://skanvyiscool.000webhostapp.com/pythonistaApps/ipad_browser/The_download_url.html"
notfy = 0



class MyWebViewDelegate (object):
	def webview_should_start_load(self, webview, url, nav_type):
		return "start_load"
	def webview_did_start_load(self, webview):
		return "did_load"
	def webview_did_finish_load(self, webview):
		return "finish_load"
	def webview_did_fail_load(self, webview, error_code, error_msg):
		return "faild_load"


def OPEN_URL_USING_INPUT(self):
	
	try:
		if 'https' in self.text:
			v['webview1'].load_url(self.text)
		
		elif 'http' in self.text:
			v['webview1'].load_url(self.text)
		
		else:
			searcher_path = 'https://duckduckgo.com/?q='
			v['webview1'].load_url(searcher_path + self.text)
		
			
			
	except:
		self.action = OPEN_URL_USING_INPUT
		if 'https' in v['textfield1'].text:
			v['webview1'].load_url(v['textfield1'].text)
		
		elif 'http' in v['textfield1'].text:
			v['webview1'].load_url(v['textfield1'].text)
		
		else:
			searcher_path = 'https://duckduckgo.com/?q='
			v['webview1'].load_url(searcher_path + v['textfield1'].text)





if v['textfield1'].text == "":
	v['webview1'].load_url('https://duckduckgo.com')
else:
	pass

def open_more_page(self):
	self.action = open_more_page
	moreP.present('sheet')




def moveTo(self):
	if self.name == "go_back":
		v['webview1'].go_back()
		
	elif self.name == "go_forward":
		v['webview1'].go_forward()
		
	else:
		v['webview1'].reload()


def RUN_DEV_MODE(self):
	self.action = RUN_DEV_MODE
	exec(open('Develop_mode.py').read())



v['textfield1'].action = OPEN_URL_USING_INPUT
v['Search_btn'].action = OPEN_URL_USING_INPUT
v['go_back'].action = moveTo
v['more_btn'].action = open_more_page
v['go_forward'].action = moveTo
v['reload_back'].action = moveTo
moreP['DEV_MOD'].action = RUN_DEV_MODE
v.present('sheet')


import requests



r = requests.get(update_release_chek)
rstr = str(r.content)


def NOTFY_PAGE_OPEN(self):
	self.action = NOTFY_PAGE_OPEN
	notyP.present('sheet')
	



if "v1.0" in rstr:
	v['Notification_btn'].hidden = True
	v['num_of_not'].hidden = True
	
else:
	v['Notification_btn'].hidden = False
	v['Notification_btn'].action = NOTFY_PAGE_OPEN
	notfy = notfy + 1
	v['num_of_not'].text = str(notfy)
	
	
	rr = requests.get(news_for_update)
	rrstr = str(rr.content)
	rrstr = rrstr.replace("b'", "")
	rrstr = rrstr.replace("[ER]", "\n")
	rrstr = rrstr.replace(r"\n", "")
	
	rrr = requests.get(url_for_download)
	rrrstr = str(rrr.content)
	
	def Download_new_app(self):
		webbrowser.open(rrrstr)
		self.action = Download_new_app
		
	
	notyP['label2'].text = rrstr
	notyP['button1'].title = "Download now!"
	notyP['textview1'].text= rrrstr
	notyP['button1'].action = webbrowser.open(rrrstr)
