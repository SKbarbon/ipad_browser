import ui
import time

v = ui.load_view('Develop_mode')






def AUTO_RUN(self):
	
	if self.title == "auto show - stoped":
		self.title = "auto show - started"
		
	else:
		self.title = "auto show - stoped"
		
	while v['auto_shower'].title == "auto show - started":
		v['webview1'].load_html(v['textview1'].text)
		
		time.sleep(1)




def RUN_STOP(self):
	v['webview1'].load_html(v['textview1'].text)


v['auto_shower'].action = AUTO_RUN
v['RUN_STOP'].action = RUN_STOP
v.present('sheet')
