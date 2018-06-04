#!/usr/bin/python
#coding=utf-8
### author: Jessie ###
### created on 4th June 2018 ###
import os
import sys
reload(sys)            # python3 doesn't support
sys.setdefaultencoding('utf-8')  # python3 does not support
import sqlite3
import wx

class database:
    def __init__(self):
        self.con = sqlite3.connect('sina_news.db')
        self.cursor = self.con.cursor()

    def select(self, idx):
        idx = int(Input.GetValue())
        cmd = 'select * from news where id=%d'%idx
        self.cursor.execute(cmd)
        values = self.cursor.fetchall()
        output = ''
        for tnew in values:
            output = 'time:\t' + tnew[1] + '\ntitle:\t' + tnew[2] + '\nurl:\t' + tnew[3]
        contents.SetValue(output)

    def show(self,event):
        sql = "select * from news"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        temp ='Last news number: '
        for item in result[-1]:
            temp += str(item)+'\n'
        contents.SetValue(temp)
        contents.AppendText('\n\n~~(=^_^=)~~(=^_^=)~~(=^_^=)~~\n')
        contents.AppendText('\nWarning: That\'s all news database.\n')

def help(event):
    contents.AppendText("Please input number id. News database is searched by id.\n\n")
    contents.AppendText("if you have any questions, feel free to connect me :)\n")
    contents.AppendText("Design and Support by xu meng-yuan.\n")


if __name__ == '__main__':
    solve = database()

    try:
        app = wx.App()
        win = wx.Frame(None,title='News Database Search',size=(610,335))
        bkg = wx.Panel(win)

        showButton = wx.Button(bkg,label = 'Show')
        showButton.Bind(wx.EVT_BUTTON,solve.show)
        helpButton = wx.Button(bkg,label = 'Help')
        helpButton.Bind(wx.EVT_BUTTON,help)
        selectButton = wx.Button(bkg,label = 'Select')
        selectButton.Bind(wx.EVT_BUTTON,solve.select)
        Input = wx.TextCtrl(bkg)
        contents = wx.TextCtrl(bkg,style = wx.TE_MULTILINE | wx.HSCROLL)

        hbox = wx.BoxSizer()
        hbox.Add(Input, proportion=1,flag = wx.EXPAND)
        hbox.Add(showButton, proportion=0, flag=wx.LEFT, border=5)
        hbox.Add(selectButton, proportion=0, flag=wx.LEFT, border=5)
        hbox.Add(helpButton, proportion=0, flag=wx.LEFT, border=5)

        vbox=wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(contents, proportion=1, flag = wx.EXPAND | wx.LEFT | wx.BOTTOM |wx.RIGHT, border=5)

        bkg.SetSizer(vbox)
        win.Show()
        app.MainLoop()

    finally:
        solve.cursor.close()
        solve.con.close()