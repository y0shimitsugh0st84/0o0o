import cnf
#from pyvirtualdisplay.smartdisplay import SmartDisplay


from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import ActionChains # --------------> action muv the mouse
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random,datetime,string , os ,time ,subprocess , sys , requests
import pyautogui
import Xlib.display

import pyvirtualdisplay

url_first=cnf.url_first
user_agent_list = cnf.user_agent_list
global display
display = Display(visible=1, size=(860, 860), use_xauth=False)

def end_and_clean():
	#os.system("clear")
	print("Clean TASKS ..... ", end='')
	try:
		#os.system("pkill firefox")#Xephyr geckodriver13
		os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver13 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#os.system("pkill Xephyr") Xvfb
		#os.system("pkill geckodriver13")
		os.system("rm -rf /tmp/*") 
		
		#display.start()
		#print("EEEEEEEEEEEEEEEEE!!!")
		time.sleep(1)
		#print("ENNNNNIIIIIIIIIITTTTT    !!!")
		#display.start()
		print(" OK !!!")
		print("############################################################")
	except:
		print(" NO  some_Error init_fire")




def build_driver():
	print("############################################################")
	print("BUILDING DRIVER ",end='')

	try:
		firefox_options = Firefox_Options()
		new_driver_path = cnf.new_driver_path
		new_binary_path = cnf.new_binary_path
		serv = Service(new_driver_path)
		user_agent = random.choice(user_agent_list)
		#print(user_agent)
		ops = Firefox_Options()
		ops.add_argument("--width=1024")
		ops.add_argument("--height=860")
		fp=webdriver.FirefoxProfile()
		fp.set_preference("dom.webdriver.enabled", False)
		fp.set_preference('useAutomationExtension', False)
		fp.set_preference("general.useragent.override",user_agent)
		fp.set_preference("http.response.timeout",95)
		fp.set_preference('webdriver.load.strategy','unstable')
		fp.set_preference("modifyheaders.headers.count", 2)
		fp.set_preference("dom.webdriver.enabled", False)
		fp.set_preference("modifyheaders.headers.action0", "Add")
		fp.set_preference("modifyheaders.headers.name0", "x-msisdn")
		fp.set_preference("dom.push.enabled", False)
		fp.update_preferences()
		ops.binary_location = new_binary_path
		ops.profile=fp
		driver = webdriver.Firefox(service=serv, options=ops)
		driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		driver.set_page_load_timeout(95)
		print("   OK")
	except Exception as aa:
		print("   ERROR :  "+str(aa))
	return driver











def main_task():
	try:
		#print (url_first)
		#display=self.display
		ddd="1024"
		display0 = Display(visible=0, size=(int(ddd), 860), use_xauth=False).start()
		#print(display)
		#main_task()
		#
		lunching_venom()
		#
		#
		#
		time.sleep(2)
#		input('jjj')
		display0.stop()
		time.sleep(2)
		display0 = Display(visible=0, size=(860, 860), use_xauth=False).start()
		print(display0)
		#main_task()
		display0.stop()
		#input("driver close")
		end_and_clean()
	except Exception as e :
		print("errr main"+str(e))





def lunching_venom():

	try:
		print("###########################Starting stage 01 #################################")
		
		print(" URL : "+url_first)
		#print("lunching_venom: ",end='###############################')
		try:
			driver=build_driver()
			print(driver.execute_script("return navigator.userAgent;"))
		except Exception as ex:
			print(str(ex),end='***')
			print('ERROR')
		driver.get(url_first)
		time.sleep(2)
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4.2);window.scrollTo(0, document.body.scrollHeight/4.5);")
		print("Click GO TO CAPTCHA  ..... : ",end='')
		go_to_captcha=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.LINK_TEXT, 'here')))
		action = ActionChains(driver)
		action.move_to_element(go_to_captcha).click().perform()
		time.sleep(3)
		print("  OK !!!!!!")
		
		print("Page Down  ..... : ",end='')
		rain_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.container')))
		time.sleep(1)
		#rain_button.send_keys(Keys.PAGE_DOWN)
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4.2);window.scrollTo(0, document.body.scrollHeight/4.5);")

		time.sleep(1)
		print("  OK !!!!!!")

		main_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn.btn-main')))
		
		iframes = driver.find_elements_by_xpath("//iframe")
		print(len(iframes))
		for index, iframe in enumerate(iframes):
			#print(index)
			#print(iframes[index])
			print("  SWITCH TO IFRAME "+ str(index) + " : ",end='')
			driver.switch_to.frame(index)
			print("  OK !!!!!!", end='')
			time.sleep(1)
			try:
				#input('botton clicked')
				print("Button AUDIO CHECK CAPATCHA  ... : ",end='')#Get Link
				main_button=WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.fbc-button-audio.fbc-button')))
				#print("OK !!!!")#Get Link
				#time.sleep(4)
				#main_button.click()
				#time.sleep(2)
				#input('botton clicked 0000000000')
				main_button.send_keys(Keys.RETURN)
				print("OK !!!!")#Get Link
				#print("button 010101010101010 CHECK CAPATCHA  !!!")#Get Link
				#time.sleep(2)
				driver.switch_to.parent_frame()
				time.sleep(2)
				print("Back To Frames  !!!")#Get Link
				break
			except  Exception as b :
				#print(b)
				print("NOT Found !!!")#Get Link
				driver.switch_to.parent_frame()
				#time.sleep(4)
				pass

		print("SWETCH FRAM !!!",end='')#Get Link
		driver.switch_to.parent_frame()
		time.sleep(3)
		
		try:
			submit_button=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn.btn-main')))
			#driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4.2);window.scrollTo(0, document.body.scrollHeight/4.5);")
			time.sleep(8)
			#print("Found submit !!!")#Get Link
			action = ActionChains(driver)
			action.move_to_element(submit_button).click().perform()
			
			time.sleep(5)
			print("  Submit OK !!!")#Get Link
			#submit_button.click()
			
			#main_button.send_keys(Keys.RETURN)
		except  Exception as b :
			print(b)
			print("NOT Found SUBMI !!!")#Get Link
			time.sleep(2)
		last_domain=url_first.replace("ouo.io/","ouo.io/go/")
		print(last_domain)
		while(True):
			print("")
			print(driver.current_url)
			try:

				main_button=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'btn-main')))
				time.sleep(1)
				main_button.click()
				time.sleep(2)
			except:
				prin("ohhh")
				pass

			if(driver.current_url != last_domain):
				break


		main_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'btn-main')))
		time.sleep(1)
		main_button.click()
		print("button  I'M HUMMEN BEEN !!!")#Get Link
		#driver.refrech()
		time.sleep(2)
		print(" OK !!!!!!")
		print(driver.current_url)
		input("end")
	except Exception as ex:
		print(str(ex),end='***')
		print('ERROR')



















main_task()
















#with pyvirtualdisplay.Display(visible=True):
 #   if True:  # Set to False to use Chrome...
  #      main_task()
   #     display.stop()
    #    time.sleep(12)
     #   main_task()
    #else:
     #   print('hhhh')



