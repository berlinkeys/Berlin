#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# this script sets the Net of some selected elements to GND

#import pcbnew
import ctypes
import tkinter as tk

class Input:
    def __init__(self):
        w = tk()
        e= Entry(w)
        e.pack()
        e.focus_set()
        
def Renate():
    board = pcbnew.GetBoard()
    self = board

    net = Input()

    print("Attempting to Ground out all selected Pads, Vias and Traces...")
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


class SimplePlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "SkyNet"
        self.category = "Utility, Nettools"
        self.description = "This tool sets the Net of selected vias, traces and pads to a specified value"
    def Run(self):
        # The entry function of the plugin that is executed on user action
        Renate()

SimplePlugin().register() # Instantiate and register to Pcbnew
