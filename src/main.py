#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
#import multiprocessing
#do not generate pyc file
#sys.dont_write_bytecode = True

from PySide2.QtCore import Qt, QCoreApplication
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QSplashScreen

#create application and set properties

if __name__ == '__main__':
	QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
	#QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

	app = QApplication(sys.argv)
	app.setOrganizationName('Chengdu University')
	app.setOrganizationDomain('http://www.cdu.edu.cn')
	app.setApplicationName('Krait')

	#support windows 7, 10 taskbar icon
	import ctypes
	if os.name == 'nt':
		myappid = 'CDU.Krait.ssr.1.0'
		ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

	import splash_rc
	splash_img = QPixmap(":/icons/splash.png")
	splash = QSplashScreen(splash_img)
	splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.SplashScreen | Qt.FramelessWindowHint)
	splash.setStyleSheet('''
		font-family:"Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif;
		font-size: 14px;
	''')
	splash.setEnabled(False)
	splash.show()

	def show_splash_msg(msg):
		splash.showMessage(msg, Qt.AlignCenter | Qt.AlignBottom, Qt.white)
		app.processEvents()

	import krait_rc
	show_splash_msg("Loading icon resources...")
	import config
	show_splash_msg("Loading configurations...")
	from libs import *
	show_splash_msg("Loading search engines...")
	import utils
	show_splash_msg("Loading utils library...")
	import detail
	show_splash_msg("Loading detail library...")
	import db
	show_splash_msg("Loading database library...")
	import motif
	show_splash_msg("Loading motif library...")
	#import plot
	#show_splash_msg("Loading plot library...")
	import statistics
	show_splash_msg("Loading statistical library...")
	import workers
	show_splash_msg("Loading workers...")
	import widgets
	show_splash_msg("Loading main widgets...")

	#set style sheet like css
	app.setStyleSheet(config.STYLE_QSS)

	#create main windows
	from widgets import SSRMainWindow
	win = SSRMainWindow()
	win.show()

	#stop splash screen
	splash.finish(win)

	#start the main loop
	#multiprocessing.freeze_support()
	sys.exit(app.exec_())
