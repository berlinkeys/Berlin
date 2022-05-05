#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# this script sets the Net of some selected elements to GND

import pcbnew
import ctypes
board = pcbnew.GetBoard()

def Ground():
    self = board

    print("Attempting to Ground out all selected Pads, Vias and Traces...")
    if not (self.GetNetsByName().__contains__("GND")):      
        ctypes.windll.user32.MessageBoxW(None, 'Board has no "GND" net.', 'Ground', 16)

    else:
        for p in self.GetPads():
            if p.IsSelected():
                p.SetNet(self.GetNetsByName().__getitem__("GND"))
                p.ClearSelected()
        for t in self.GetTracks():
            if t.IsSelected():
                t.SetNet(self.GetNetsByName().__getitem__("GND"))
                t.ClearSelected()
                
        ctypes.windll.user32.MessageBoxW(None, 'Operation complete.', 'Ground', 0)


class SimplePlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Ground"
        self.category = "Utility, Nettools"
        self.description = "This tool sets the Net of selected vias, traces and pads to GND"
    def Run(self):
        # The entry function of the plugin that is executed on user action
        Ground()

SimplePlugin().register() # Instantiate and register to Pcbnew
