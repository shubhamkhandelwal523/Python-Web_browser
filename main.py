import sys , os, json
from typing import AsyncIterable, Container
from PyQt5 import QtGui

from PyQt5.QtWidgets import (QApplication, QSplitter, QWidget, QVBoxLayout, QHBoxLayout,
                            QPushButton, QLabel, QLineEdit, QTabBar,
                            QFrame, QStackedLayout, QSplitter, QMainWindow, QTabWidget, QShortcut, QKeySequenceEdit) 

from PyQt5.QtGui import QIcon, QKeySequence, QWindow, QImage
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class AddressBar(QLineEdit):
    def __init__(self):
        super().__init__()
    def mousePressEvent(self,e):
        self.selectAll

class App(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Browser")

        self.setBaseSize(1366,768)
        self.setMinimumSize(1366,768)
        self.CreateApp()
        self.setWindowIcon(QIcon("C:/Users/shubh/Desktop/udemy python/PyQT WEB/logo.png"))
       
        
    def CreateApp(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)

        # create Tabs
        self.tabbar = QTabBar(movable= True, tabsClosable= True)
        self.tabbar.tabCloseRequested.connect(self.CloseTab)
        self.tabbar.tabBarClicked.connect(self.SwitchTab)
        self.tabbar.setDrawBase(False)

        self.tabbar.setCurrentIndex(0)
        self.tabbar.setLayoutDirection(Qt.LeftToRight)
        self.tabbar.setElideMode(Qt.ElideLeft)

        self.shortcutNewtab =  QShortcut(QKeySequence("Ctrl+Shift+T"),self)
        self.shortcutNewtab.activated.connect(self.AddTab)

        self.shortcutReload =  QShortcut(QKeySequence("Ctrl+R"),self)
        self.shortcutReload.activated.connect(self.ReloadPage)

        # self.shortcutInspect =  QShortcut(QKeySequence("Ctrl+Shift+I"),self)
        # self.shortcutInspect.activated.connect(self.Inspect)
        # self.tabbar.addTab("Tab 1")
        # self.tabbar.addTab("Tab 2")
    
        # self.tabbar.addTab(QPushButton("Tab 1"), "First Tab")
        # self.tabbar.addTab(QPushButton("Tab 2"), "Second Tab")

        #Keep Track of Tabs
        self.tabCount = 0
        self.tabs = []

        #Create AddressBar

        self.ToolBar = QWidget()
        self.ToolBar.setObjectName("Toolbar")
        self.ToolBarLayout=  QHBoxLayout()
        self.addressbar = AddressBar()
        self.AddTabButton =  QPushButton("+")
        
        # connect addressBar + button signals
        self.addressbar.returnPressed.connect(self.BrowseTo)
        self.AddTabButton.clicked.connect(self.AddTab)

        #Set toolbar Buttons
        self.BackButton = QPushButton("🡰")
        self.BackButton.clicked.connect(self.GoBack)

        self.ForwardButton = QPushButton("🡲")
        self.ForwardButton.clicked.connect(self.GoForward)

        self.ReloadButton =  QPushButton("⟳")
        self.ReloadButton.clicked.connect(self.ReloadPage)

        self.Home = QPushButton("🏠")
        self.Home.clicked.connect(self.HomePage)

        #Build toolbar
        self.ToolBar.setLayout(self.ToolBarLayout)
        self.ToolBarLayout.addWidget(self.BackButton)
        self.ToolBarLayout.addWidget(self.ForwardButton)
        self.ToolBarLayout.addWidget(self.ReloadButton)
        self.ToolBarLayout.addWidget(self.Home)
        self.ToolBarLayout.addWidget(self.addressbar)
        self.ToolBarLayout.addWidget(self.AddTabButton)
        
    
        #set main view
        self.container =  QWidget()
        self.container.layout =  QStackedLayout()
        self.container.setLayout(self.container.layout)

        # Construct Main view from top level elements
        self.layout.addWidget(self.tabbar)
        self.layout.addWidget(self.ToolBar)
        self.layout.addWidget(self.container)

        self.setLayout(self.layout)

        self.AddTab()

        self.show()

    def CloseTab(self,i):
        self.tabbar.removeTab(i)
    
    def AddTab(self):
        i =  self.tabCount


        # set self.tabs<#> =  QWidget
        self.tabs.append(QWidget())
        self.tabs[i].layout = QVBoxLayout()
        self.tabs[i].layout.setContentsMargins(0,0,0,0)
        
    

        # For Tab Switching
        self.tabs[i].setObjectName("tab"+ str(i))
        
        # Create WebView within the tabs to level widget
        self.tabs[i].content =  QWebEngineView()
        self.tabs[i].content.load(QUrl.fromUserInput("http://google.com"))
        
        self.tabs[i].content1 =  QWebEngineView()
        self.tabs[i].content1.load(QUrl.fromUserInput("http://google.com"))

        self.tabs[i].content.titleChanged.connect(lambda: self.SetTabContent(i, "title"))
        self.tabs[i].content.iconChanged.connect(lambda: self.SetTabContent(i, "icon"))
        self.tabs[i].content.urlChanged.connect(lambda: self.SetTabContent(i, "url"))
        

        #Add widgets to tab.layout
        self.tabs[i].splitview = QSplitter()
        self.tabs[i].splitview.setOrientation(Qt.Vertical)
        self.tabs[i].layout.addWidget(self.tabs[i].splitview)

        self.tabs[i].splitview.addWidget(self.tabs[i].content)
        self.tabs[i].splitview.addWidget(self.tabs[i].content1)

        # set tablayout to .layout
        self.tabs[i].setLayout(self.tabs[i].layout)

        # add  and set new tabs content to top  stackedwidget

        self.container.layout.addWidget(self.tabs[i])
        self.container.layout.setCurrentWidget(self.tabs[i])

        # Create tab on tabbar , representing this tab,
        # Set tabdata to tab<#> So it knows what self.tabs[#] it needs to control
        self.tabbar.addTab("New Tab")
        self.tabbar.setTabData(i,{"object": "tab" + str(i),"initial": i})

        
        # print("td: ",self.tabbar.tabData(i)["object"])
        self.tabbar.setCurrentIndex(i)

        # += 1
        self.tabCount += 1

    def SwitchTab(self,i):

        # Switch to tab , get current tabs tabData ["tab0"] and find object with that name

        if self.tabbar.tabData(i):
            tab_data = self.tabbar.tabData(i)["object"]
            tab_content = self.findChild(QWidget,tab_data)
            self.container.layout.setCurrentWidget(tab_content)
            new_url = tab_content.content.url().toString()
            self.addressbar.setText(new_url)

    def BrowseTo(self):
        text = self.addressbar.text()
        print(text)

        i = self.tabbar.currentIndex()
        tab = self.tabbar.tabData(i)["object"]
        wv =  self.findChild(QWidget, tab).content

        if "http" not in text:
            if "." not in text:
                url = "https://www.google.com/#q="+ text
            else:
                url = "http://"+ text
        else:
            url = text

        wv.load(QUrl.fromUserInput(text))

    def SetTabContent(self, i, type):
        '''
            self.tabs[i].objectName = tab1
            self.tabbar.tabData(i)["object"] =  tab1
        '''
        tab_name =  self.tabs[i].objectName()
        # tab1

        count  = 0
        running =  True

        current_tab= self.tabbar.tabData(self.tabbar.currentIndex())["object"]

        if current_tab == tab_name and type == "url":
            new_url = self.findChild(QWidget, tab_name).content.url().toString()
            self.addressbar.setText(new_url)
            return False

        while running:
            tab_data_name=  self.tabbar.tabData(count)
            if count >= 99:
                running = False
            if tab_name == tab_data_name["object"]:
                if type == "title":

                    newTitle=  self.findChild(QWidget,tab_name).content.title()
                    self.tabbar.setTabText(count,newTitle)
                elif type == "icon":
                    newIcon = self.findChild(QWidget, tab_name).content.icon()
                    self.tabbar.setTabIcon(count, newIcon)

                running =  False
            else:
                count += 1
    def GoBack(self):
        activeIndex  = self.tabbar.currentIndex()
        tab_name =  self.tabbar.tabData(activeIndex)["object"]
        tab_content =  self.findChild(QWidget,tab_name).content
        
        tab_content.back()
        pass
    def GoForward(self):
        activeIndex  = self.tabbar.currentIndex()
        tab_name =  self.tabbar.tabData(activeIndex)["object"]
        tab_content =  self.findChild(QWidget,tab_name).content

        tab_content.forward()
        pass
    def ReloadPage(self):
        activeIndex  = self.tabbar.currentIndex()
        tab_name =  self.tabbar.tabData(activeIndex)["object"]
        tab_content =  self.findChild(QWidget,tab_name).content

        tab_content.reload()
        pass

    def HomePage(self):
        activeIndex  = self.tabbar.currentIndex()
        tab_name =  self.tabbar.tabData(activeIndex)["object"]
        tab_content =  self.findChild(QWidget,tab_name).content

        tab_content.load(QUrl.fromUserInput("http://google.com"))
        pass


if __name__ == "__main__":
    app =  QApplication(sys.argv)
    os.environ["QTWEBENGINE_REMOTE_DEBUGGING"] = "5490"
    
    window = App()
    with open("C:/Users/shubh/Desktop/udemy python/PyQT WEB/style.css", "r") as style:
        app.setStyleSheet(style.read())
    

    sys.exit(app.exec_())
        




