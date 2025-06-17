# for GUI object classes/wrappers
# Working on this in wxGlade

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle("CheezeFizz WT")

        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        self.FileMenu = wx.Menu()
        self.frame_menubar.Append(self.FileMenu, "&File")
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.GridSizer(2, 1, 2, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "CheeseFizz Workout Tracker")
        sizer_1.Add(label_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        grid_sizer_1 = wx.GridSizer(1, 3, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)

        self.NewWT = wx.Button(self.panel_1, wx.ID_ANY, "New Workout")
        grid_sizer_1.Add(self.NewWT, 0, wx.ALIGN_CENTER, 0)

        self.LoadWT = wx.Button(self.panel_1, wx.ID_ANY, "Load Workout")
        grid_sizer_1.Add(self.LoadWT, 0, wx.ALIGN_CENTER, 0)

        self.ImportWT = wx.Button(self.panel_1, wx.ID_ANY, "Import Workout")
        grid_sizer_1.Add(self.ImportWT, 0, wx.ALIGN_CENTER, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()

        self.NewWT.Bind(wx.EVT_BUTTON, self.onClick)
        self.LoadWT.Bind(wx.EVT_BUTTON, self.onClick)
        self.ImportWT.Bind(wx.EVT_BUTTON, self.onClick)
        self.Bind(wx.EVT_CLOSE, self.onExit)
        # end wxGlade

    def onMenu_File(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'onMenu_File' not implemented!")
        event.Skip()

    def onClick(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'onClick' not implemented!")
        event.Skip()

    def onExit(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'onExit' not implemented!")
        event.Skip()

# end of class MyFrame

class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("New Workout")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.window_1 = wx.SplitterWindow(self, wx.ID_ANY)
        self.window_1.SetMinimumPaneSize(20)
        sizer_1.Add(self.window_1, 1, wx.EXPAND, 0)

        self.window_1_pane_1 = wx.Panel(self.window_1, wx.ID_ANY)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)

        self.tree_ctrl_1 = wx.TreeCtrl(self.window_1_pane_1, wx.ID_ANY, style=wx.BORDER_SUNKEN | wx.TR_HAS_BUTTONS | wx.TR_NO_BUTTONS | wx.TR_SINGLE)
        sizer_3.Add(self.tree_ctrl_1, 1, wx.EXPAND, 0)

        self.notebook_1 = wx.Notebook(self.window_1, wx.ID_ANY)

        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "notebook_1_pane_1")

        sizer_4 = wx.BoxSizer(wx.VERTICAL)

        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(sizer_8, 1, wx.EXPAND, 0)

        label_1 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, "Name", style=wx.ALIGN_CENTER_HORIZONTAL)
        sizer_8.Add(label_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 20)

        self.text_ctrl_1 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
        sizer_8.Add(self.text_ctrl_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(sizer_9, 1, wx.EXPAND, 0)

        label_2 = wx.StaticText(self.notebook_1_pane_1, wx.ID_ANY, "Tags (separate by semicolon)", style=wx.ALIGN_CENTER_HORIZONTAL)
        sizer_9.Add(label_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 20)

        self.text_ctrl_2 = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "")
        sizer_9.Add(self.text_ctrl_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(sizer_10, 1, wx.EXPAND, 0)

        self.button_1 = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, "Add Exercise")
        sizer_10.Add(self.button_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.button_2 = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, "Edit Exercise")
        sizer_10.Add(self.button_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.button_3 = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, "Remove Exercise")
        sizer_10.Add(self.button_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_pane_2, "notebook_1_pane_2")

        sizer_5 = wx.BoxSizer(wx.VERTICAL)

        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5.Add(sizer_11, 1, wx.EXPAND, 0)

        label_3 = wx.StaticText(self.notebook_1_pane_2, wx.ID_ANY, "Exercise", style=wx.ALIGN_CENTER_HORIZONTAL)
        sizer_11.Add(label_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 20)

        self.combo_box_1 = wx.ComboBox(self.notebook_1_pane_2, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN | wx.CB_SORT)
        sizer_11.Add(self.combo_box_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5.Add(sizer_12, 1, wx.EXPAND, 0)

        label_4 = wx.StaticText(self.notebook_1_pane_2, wx.ID_ANY, "Tags (separate by semicolon)", style=wx.ALIGN_CENTER_HORIZONTAL)
        sizer_12.Add(label_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 20)

        self.text_ctrl_4 = wx.TextCtrl(self.notebook_1_pane_2, wx.ID_ANY, "")
        sizer_12.Add(self.text_ctrl_4, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        sizer_5.Add((0, 0), 0, 0, 0)

        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5.Add(sizer_13, 1, wx.EXPAND, 0)

        self.button_4 = wx.Button(self.notebook_1_pane_2, wx.ID_ANY, "Add to Workout")
        sizer_13.Add(self.button_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.button_5 = wx.Button(self.notebook_1_pane_2, wx.ID_ANY, "Add Set")
        sizer_13.Add(self.button_5, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.button_6 = wx.Button(self.notebook_1_pane_2, wx.ID_ANY, "Remove Set")
        sizer_13.Add(self.button_6, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.notebook_1_pane_3 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_pane_3, "notebook_1_pane_3")

        sizer_6 = wx.BoxSizer(wx.VERTICAL)

        sizer_6.Add((0, 0), 0, 0, 0)

        self.notebook_1_pane_4 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_pane_4, "notebook_1_pane_4")

        sizer_7 = wx.BoxSizer(wx.VERTICAL)

        sizer_7.Add((0, 0), 0, 0, 0)

        sizer_2 = wx.StdDialogButtonSizer()
        sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self.button_7 = wx.Button(self, wx.ID_ANY, "Apply")
        sizer_2.Add(self.button_7, 0, 0, 0)

        self.button_OK = wx.Button(self, wx.ID_OK, "")
        self.button_OK.SetDefault()
        sizer_2.AddButton(self.button_OK)

        self.button_CANCEL = wx.Button(self, wx.ID_CANCEL, "")
        sizer_2.AddButton(self.button_CANCEL)

        sizer_2.Realize()

        self.notebook_1_pane_4.SetSizer(sizer_7)

        self.notebook_1_pane_3.SetSizer(sizer_6)

        self.notebook_1_pane_2.SetSizer(sizer_5)

        self.notebook_1_pane_1.SetSizer(sizer_4)

        self.window_1_pane_1.SetSizer(sizer_3)

        self.window_1.SplitVertically(self.window_1_pane_1, self.notebook_1)

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

        self.SetAffirmativeId(self.button_OK.GetId())
        self.SetEscapeId(self.button_CANCEL.GetId())

        self.Layout()

        self.text_ctrl_1.Bind(wx.EVT_TEXT_ENTER, self.onEnter)
        self.text_ctrl_2.Bind(wx.EVT_TEXT_ENTER, self.onEnter)
        self.button_1.Bind(wx.EVT_BUTTON, self.onClick)
        self.button_2.Bind(wx.EVT_BUTTON, self.onClick)
        self.button_3.Bind(wx.EVT_BUTTON, self.onClick)
        self.text_ctrl_4.Bind(wx.EVT_TEXT_ENTER, self.onEnter)
        self.button_4.Bind(wx.EVT_BUTTON, self.onClick)
        self.button_5.Bind(wx.EVT_BUTTON, self.onClick)
        self.button_6.Bind(wx.EVT_BUTTON, self.onClick)
        # end wxGlade

    def onEnter(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'onEnter' not implemented!")
        event.Skip()

    def onClick(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'onClick' not implemented!")
        event.Skip()

# end of class MyDialog

class WTApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True
