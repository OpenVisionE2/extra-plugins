# -*- coding: utf-8 -*-
from Components.ConfigList import ConfigListScreen
from Components.config import config, configfile
from Components.ActionMap import ActionMap
from Components.MenuList import MenuList
from Components.Sources.StaticText import StaticText
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from .downloader import ConverDate
import glob
import os
import sys
from enigma import *
from Components.Console import Console

Directory = os.path.dirname(sys.modules[__name__].__file__)


class PU_Restore(Screen, ConfigListScreen):

    skin = """
        <screen name="PU_Restore" position="center,center" size="600,470">
            <ePixmap pixmap="buttons/red.png" position="5,0" size="140,40" alphaTest="on" />
            <ePixmap pixmap="buttons/green.png" position="155,0" size="140,40" alphaTest="on" />
            <ePixmap pixmap="buttons/yellow.png" position="305,0" size="140,40" alphaTest="on" />
            <widget source="key_red" render="Label" position="5,0" zPosition="1" size="140,40" font="Regular;20" horizontalAlignment="center" verticalAlignment="center" backgroundColor="#9f1313" foregroundColor="#ffffff" transparent="1" />
            <widget source="key_green" render="Label" position="155,0" zPosition="1" size="140,40" font="Regular;20" horizontalAlignment="center" verticalAlignment="center" backgroundColor="#1f771f" foregroundColor="#ffffff" transparent="1" />
            <widget source="key_yellow" render="Label" position="305,0" zPosition="1" size="140,40" font="Regular;20" horizontalAlignment="center" verticalAlignment="center" foregroundColor="#ffffff" transparent="1" />
            <widget name="ListSetting" position="25,70" size="560,350" scrollbarMode="showOnDemand" />
        </screen>
        """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.session = session
        self['ListSetting'] = MenuList([])
        self.skinName = "PU_Restore"
        self.setup_title = _("Programmlisten Restore")
        self.setTitle(self.setup_title)

        self["key_red"] = StaticText(_("Exit"))
        self["key_green"] = StaticText(_("Restore"))
        self["key_yellow"] = StaticText(_("Delete"))

        self["ColorActions"] = ActionMap(['OkCancelActions', 'ShortcutActions', "ColorActions"],
            {
            "red": self.keyCancel,
            "green": self.keyGreen,
            "yellow": self.keyYellow,
            "cancel": self.keyCancel,
            "ok": self.keyOk,
            })

        self.List = self.Search_Settings()
        self.SettingsMenu()

    def keyCancel(self):
        self.close()

    def keyOk(self):
        self.keyGreen()

    def keyGreen(self):
        self.filename = self['ListSetting'].getCurrent()
        if self.filename is not None:
            self.session.openWithCallback(self.CBselect, MessageBox, _('Selected settingslist: %s\n\nDo you want to restore this settinglist?') % (self.filename), MessageBox.TYPE_YESNO)

    def CBselect(self, req):
        if req:
            self.Do_Restore()

    def keyYellow(self):
        self.filename = self['ListSetting'].getCurrent()
        if self.filename is not None:
            self.session.openWithCallback(self.CBremove, MessageBox, _('Selected settingslist: %s\n\nDo you want to delete this settinglist?') % (self.filename), MessageBox.TYPE_YESNO)

    def CBremove(self, req):
        if req:
            Console().ePopen('rm -rf %s/Settings/enigma2/%s' % (Directory, self.filename))
            self.List = self.Search_Settings()
            self.SettingsMenu()

    def Search_Settings(self):
        list = []
        os.chdir(Directory + '/Settings/enigma2')
        for file in glob.glob('*backup.tar.gz'):
            list.append(file)
        return list

    def SettingsMenu(self):
        self['ListSetting'].setList(self.List)

    def Do_Restore(self):
        # Set Backup date
        date = ConverDate(self.filename[:6])
        config.pud.lastdate.value = date
        config.pud.save()
        configfile.save()
        # Remove current settingslist
        Console().ePopen('rm -f /etc/enigma2/lamedb')
        Console().ePopen('rm -f /etc/enigma2/*.radio')
        Console().ePopen('rm -f /etc/enigma2/*.tv')
        # Restore settingslist
        Console().ePopen('tar -xzvf %s/Settings/enigma2/%s -C /' % (Directory, self.filename))
        # Reload settingslist
        eDVBDB.getInstance().reloadServicelist()
        eDVBDB.getInstance().reloadBouquets()
        self.session.open(MessageBox, _('Setting Restored ') + self.filename + _(' of ') + date, MessageBox.TYPE_INFO, timeout=15)
        self.close()
