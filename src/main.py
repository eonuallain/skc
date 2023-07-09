import os

import wx

from kubeconfig import *


class SKCTree(wx.TreeCtrl):
    def __init__(self, parent, id, position, size, style):
        wx.TreeCtrl.__init__(self, parent, id, position, size, style)

        root = self.AddRoot('Clusters')
        clusters = get_clusters()
        for cluster_name in clusters:
            cluster_node = self.AppendItem(root, cluster_name['name'])
            self.AppendItem(cluster_node, 'Nodes')
            self.AppendItem(cluster_node, 'Pods')


class SKCFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title,
                          wx.DefaultPosition, wx.Size(500, 480))

        self.splitter = wx.SplitterWindow(self, -1, style=wx.SP_LIVE_UPDATE)
        left_panel = wx.Panel(self.splitter, -1)
        self.tree = SKCTree(left_panel, 1,
                           wx.DefaultPosition,
                           wx.DefaultSize,
                           wx.TR_HIDE_ROOT |
                           wx.TR_HAS_BUTTONS)
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, id=1)
        right_panel = wx.Panel(self.splitter, -1, style=wx.SUNKEN_BORDER)
        self.display = wx.StaticText(right_panel, -1, '', style=wx.ALIGN_LEFT)
        self.splitter.SplitVertically(left_panel, right_panel, 200)
        self.splitter.SetMinimumPaneSize(1)
        left_box = wx.BoxSizer(wx.VERTICAL)
        left_box.Add(self.tree, 1, wx.EXPAND)
        left_panel.SetSizer(left_box)
        right_box = wx.BoxSizer(wx.VERTICAL)
        right_box.Add(self.display, 0, wx.ALL, 10)
        right_panel.SetSizer(right_box)
        self.Centre()

    def OnSelChanged(self, event):
        item = event.GetItem()
        try:
            item_text = self.tree.GetItemText(item)
            if "Pods" == item_text:
                print("### list pods")
            if "Nodes" == item_text:
                print("### list nodes")
            self.display.SetLabel(item_text)
        except RuntimeError:
            # ignore runtime error when shutting down, underlying C++ objects are gone
            pass


class SKCApp(wx.App):

    def OnInit(self):
        skc_frame = SKCFrame(None, -1, 'Simple Kubernetes Client')
        skc_frame.Centre()
        skc_frame.Show(True)
        self.SetTopWindow(skc_frame)

        return True


if __name__ == '__main__':
    if config_defined():
        config_path = os.environ[KUBECONFIG]
        print(f"reading {config_path}")
        config_dict = get_config(os.environ[KUBECONFIG])
    elif default_config_exists():
        default_config = get_default_config_path()
        print(f"reading {default_config}")
        config_dict = get_config(default_config)
    else:
        print('KUBECONFIG environment variable not set and default kube config not found')
        exit(1)

    skc_app = SKCApp(0)
    skc_app.MainLoop()