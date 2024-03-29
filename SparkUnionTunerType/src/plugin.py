# -*- coding: utf-8 -*-
from Screens.Screen import Screen
from Screens.Standby import TryQuitMainloop
from Screens.MessageBox import MessageBox
from Components.ActionMap import ActionMap
from Components.config import getConfigListEntry, ConfigSelection
from Components.ConfigList import ConfigListScreen
from Components.Sources.StaticText import StaticText
from Plugins.Plugin import PluginDescriptor
from os.path import isfile
import fileinput

option = 'options spark7162-fe UnionTunerType='
filename = '/etc/modprobe.d/_spark7162.conf' # modules-conf.conf
#filename = '/etc/modules-load.d/_spark7162.conf' # modules.conf


class UnionTunerType(Screen, ConfigListScreen):

    def __init__(self, session):
        self.session = session
        Screen.__init__(self, self.session)
        self.skinName = ['Setup']
        self.setTitle(_('spark7162 select tuner mode'))
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'cancel': self.cancel,
         'ok': self.ok,
         'green': self.ok,
         'red': self.cancel}, -2)
        t = None
        if isfile(filename):
            settings = open(filename)
            while True:
                s = settings.readline().strip()
                if s == '':
                    break
                if s.startswith(option):
                    try:
                        t = s[len(option)]
                    except IndexError:
                        print('[SparkUnionTunerType] bad format in modprobe config')

                    break

            settings.close()
        if t is None:
            t = 't'
        self.tunerconfig = ConfigSelection(default=t, choices=[('t', _('terrestrial')), ('c', _('cable'))])
        conf = []
        conf.append(getConfigListEntry(_('UnionTunerType'), self.tunerconfig))
        ConfigListScreen.__init__(self, conf, session=self.session)
        self['key_red'] = StaticText(_('Cancel'))
        self['key_green'] = StaticText(_('OK'))

    def settingsWrite(self, result):
        if result is not None and result:
            for line in fileinput.input(filename, inplace=1):
                if line.startswith(option):
                    print(option + self.tunerconfig.value)
                else:
                    print(line)
            fileinput.close()
            self.session.open(TryQuitMainloop, retvalue=2)
        self.close()

    def ok(self):
        if self.tunerconfig.isChanged():
            self.session.openWithCallback(self.settingsWrite, MessageBox, _('Are you sure to save the current configuration and reboot your receiver?\n\n'))
        else:
            self.close()

    def cancel(self):
        self.close()


def main(session, **kwargs):
    session.open(UnionTunerType)


def menu(menuid, **kwargs):
    if menuid == 'scan':
        return [(_('SparkUnionTunerType config'),
          main,
          'UnionTunerType',
          None)]
    else:
        return []


def Plugins(**kwargs):
    return PluginDescriptor(name=_('UnionTunerType config'), description=_('Select spark7162 dvb-t/c tuner mode'), where=PluginDescriptor.WHERE_MENU, fnc=menu)
