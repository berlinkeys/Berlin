#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# this script sets the Net of some selected elements to a specified existing value

import pcbnew
import ctypes, wx


# code to setup the wx input window 

def evaluate(net):
    
    board = pcbnew.GetBoard()
    self = board
    print("Attempting to '"+net+"' out all selected Pads, Vias and Traces...")
    if not (self.GetNetsByName().__contains__(net)):      
        ctypes.windll.user32.MessageBoxW(None, 'Board has no '+net+' net.', 'SkyNet', 16)

    else:
        for p in self.GetPads():
            if p.IsSelected():
                p.SetNet(self.GetNetsByName().__getitem__(net))
                p.ClearSelected()
        for t in self.GetTracks():
            if t.IsSelected():
                t.SetNet(self.GetNetsByName().__getitem__(net))
                t.ClearSelected()
                
        ctypes.windll.user32.MessageBoxW(None, 'Operation complete.', 'SkyNet', 0)

def input(event):  
    eval = True
    evaluate(textbox.GetValue())
    exit()
    return
    
def exit(event=None):
    #frame.Hide()
    return

app = wx.App()
frame = wx.Frame()

wx.Frame.__init__(frame, None, -1, 'Skynet', style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER, size=(250, 120))
panel = wx.Panel(frame, -1) 

basicLabel = wx.StaticText(panel, -1, "Enter net:", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(100, -1))
textbox = wx.TextCtrl(panel, -1, "GND", style=wx.TE_PROCESS_ENTER, size=(125, -1))
textbox.Bind(wx.EVT_TEXT_ENTER, input)
textbox.SetInsertionPoint(0)

okButton = wx.Button(panel, label="OK", size=(100, -1))
okButton.Bind(wx.EVT_BUTTON, input)
cancelButton = wx.Button(panel, label="Cancel", size=(125, -1))
cancelButton.Bind(wx.EVT_BUTTON, exit)

sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
sizer.AddMany([basicLabel, textbox, okButton, cancelButton])
panel.SetSizer(sizer)


# main function       
def Renate():

    eval = False

    frame.Show()
    
    net = textbox.GetValue()
    if eval:
        exit()
        evaluate(net)


    

class SimplePlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "SkyNet"
        self.category = "Utility, Nettools"
        self.description = "This tool sets the Net of selected vias, traces and pads to a specified value"
    def Run(self):
        # The entry function of the plugin that is executed on user action
        Renate()

SimplePlugin().register() # Instantiate and register to Pcbnew
