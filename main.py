import wx


from kubeconfig import *

if config_defined():
    config_dict = get_config()
    print(config_dict)
else:
    print('KUBECONFIG environment variable not set')
    exit(1)

app = wx.App()
frame = wx.Frame(parent=None, title='SKC')
frame.Centre()
frame.Show()
app.MainLoop()
