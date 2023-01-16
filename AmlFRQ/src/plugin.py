# -*- coding: utf-8 -*-
from Screens.Screen import Screen
from Plugins.Plugin import PluginDescriptor
from Components.Button import Button
from Components.ActionMap import ActionMap
from Components.ConfigList import ConfigList, ConfigListScreen
from Components.config import config, configfile, ConfigSubsection, getConfigListEntry, ConfigSelection
from Components.Label import Label
from Components.SystemInfo import BoxInfo
import Screens.Standby as Screens
from enigma import eTimer

platform = BoxInfo.getItem("platform")

config.plugins.aml = ConfigSubsection()
if platform == "dmamlogic":
    config.plugins.aml.governor = ConfigSelection('performance', [
        ('interactive', 'Interactive - responsive and savvy'),
        ('schedutil', 'schedutil - scheduler-driven (suggested)'),
        ('performance', 'Performance -max full time (default)')], **('default', 'choices'))
    config.plugins.aml.maxfrq = ConfigSelection('1800000', [
        ('500000', '500 MHz'),
        ('667000', '667 MHz'),
        ('1000000', '1 GHz'),
        ('1200000', '1.2 GHz'),
        ('1398000', '1.4 GHz'),
        ('1512000', '1.5 GHz'),
        ('1608000', '1.6 GHz'),
        ('1704000', '1.7 GHz'),
        ('1800000', _('1.8 GHz (default)'))], **('default', 'choices'))
    config.plugins.aml.minfrq = ConfigSelection('500000', [
        ('500000', '500 MHz (default)'),
        ('667000', '667 MHz'),
        ('1000000', '1 GHz'),
        ('1200000', '1.2 GHz'),
        ('1398000', '1.4 GHz'),
        ('1512000', '1.5 GHz'),
        ('1608000', '1.6 GHz'),
        ('1704000', '1.7 GHz'),
        ('1800000', _('1.8 GHz'))], **('default', 'choices'))
    config.plugins.aml.maxfrq2 = ConfigSelection('1704000', [
        ('500000', '500 MHz'),
        ('667000', '667 MHz'),
        ('1000000', '1 GHz'),
        ('1200000', '1.2 GHz'),
        ('1398000', '1.4 GHz'),
        ('1512000', '1.5 GHz'),
        ('1608000', '1.6 GHz'),
        ('1704000', '1.7 GHz (default)')], **('default', 'choices'))
    config.plugins.aml.minfrq2 = ConfigSelection('500000', [
        ('500000', '500 MHz (default)'),
        ('667000', '667 MHz'),
        ('1000000', '1 GHz'),
        ('1200000', '1.2 GHz'),
        ('1398000', '1.4 GHz'),
        ('1512000', '1.5 GHz'),
        ('1608000', '1.6 GHz'),
        ('1704000', '1.7 GHz')], **('default', 'choices'))


def leaveStandby():
    print('[AmlFRQ] Leave Standby')
    initBooster()


def standbyCounterChanged(configElement):
    print('[AmlFRQ] In Standby')
    initStandbyBooster()
    inStandby = inStandby
    import Screens.Standby
    inStandby.onClose.append(leaveStandby)


def initBooster():
    print('[AmlFRQ] initBooster')

    try:
        f = open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq', 'w')
        f.write(config.plugins.aml.maxfrq.getValue())
        f.close()
        f = open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq', 'w')
        f.write(config.plugins.aml.minfrq.getValue())
        f.close()
        f = open('/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq', 'w')
        f.write(config.plugins.aml.maxfrq2.getValue())
        f.close()
        f = open('/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq', 'w')
        f.write(config.plugins.aml.minfrq2.getValue())
        f.close()
        f = open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor', 'w')
        f.write(config.plugins.aml.governor.getValue())
        f.close()
        f = open('/sys/devices/system/cpu/cpu2/cpufreq/scaling_governor', 'w')
        f.write(config.plugins.aml.governor.getValue())
        f.close()
    finally:
        return None
        return None


def initStandbyBooster():
    print('[AmlFRQ] initStandbyBooster')

    try:
        f = open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq', 'w')
        f.write(config.plugins.aml.minfrq.getValue())
        f.close()
        f = open('/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq', 'w')
        f.write(config.plugins.aml.minfrq2.getValue())
        f.close()
    finally:
        return None
        return None


class AmlFRQ(Screen, ConfigListScreen):

    def __init__(self, session, args=(None,)):
        getDesktop = getDesktop
        import enigma
        DESKHEIGHT = getDesktop(0).size().height()
        if DESKHEIGHT == 720:
            self.skin = '\n\t\t\t<screen  position="0,0" size="1280,720" title="CPU Frequency Setup" flags="wfNoBorder" backgroundColor="#25062748">\n\t\t\t<widget source="Title" render="Label" position="140,93" size="1000,45" zPosition="2" horizontalAlignment="center" font="Regular; 24" backgroundColor="#25062748" transparent="1" verticalAlignment="center" />\n\t\t\t<ePixmap name="" position="140,100" size="1000,546" pixmap="MetrixHD/ibts/background.png" zPosition="-10" />\n\t\t\t<eLabel name="" position="156,151" size="855,432" zPosition="-5" />\n\t\t\t<ePixmap pixmap="enigma2/icon/default.png" position="1044,189" size="60,46" zPosition="1" />\n\t\t\t<eLabel name="" position="1028,290" size="96,33" font="Regular; 18" verticalAlignment="center" horizontalAlignment="center" text="Exit" />\n\t\t\t<ePixmap pixmap="MetrixHD/buttons/buttons.png" position="142,595" size="733,37" alphaTest="blend" zPosition="100" />\n\t\t\t\n\t\t\t<widget name="key_red" position="156,595" size="236,37" zPosition="1" font="Regular; 18" horizontalAlignment="center" verticalAlignment="center" backgroundColor="#9f1313" transparent="0" foregroundColor="#cccccc" />\n\t\t\t<widget name="key_green" position="401,595" size="236,37" zPosition="1" font="Regular; 18" horizontalAlignment="center" verticalAlignment="center" backgroundColor="#1f771f" transparent="0" foregroundColor="#cccccc" />\n\t\t\t<widget name="key_yellow" position="646,595" size="236,37" zPosition="1" font="Regular; 18" horizontalAlignment="center" verticalAlignment="center" backgroundColor="#a08500" transparent="0" foregroundColor="#cccccc" />\n\t\t\t\n\t\t\t<widget name="config" position="166,160" size="840,169" scrollbarMode="showOnDemand" font="Regular; 18" itemHeight="32" selectionPixmap="MetrixHD/SkinDesign/CoolNow.png" transparent="1" scrollbarSliderforegroundColor="#cccccc" scrollbarBorderColor="#25062748" />\n\t\t\t<widget name="tempc"  position="166,366"  size="486,33" font="Regular; 18" verticalAlignment="center" horizontalAlignment="left" />\n\t\t\t<widget name="voltc"  position="166,406"  size="486,33" font="Regular; 18" verticalAlignment="center" horizontalAlignment="left" />\n\t\t\t<widget name="frqc"   position="166,446"  size="486,33" font="Regular; 18" verticalAlignment="center" horizontalAlignment="left" />\n\t\t\t<widget name="frqc"   position="166,486"  size="486,33" font="Regular; 18" verticalAlignment="center" horizontalAlignment="left" />\n\t\t\t\n\t\t\t<eLabel name="" position="1028,248" size="96,33" font="Regular; 18" verticalAlignment="center" horizontalAlignment="center" text="OK" />\n\t\t\t</screen>'
        else:
            self.skin = '\n\t\t\t<screen  position="0,0" size="1920,1080" title="CPU Frequency Setup" flags="wfNoBorder" backgroundColor="#25062748">\n\t\t\t<widget source="Title" render="Label" position="210,140" size="1500,68" zPosition="2" horizontalAlignment="center" font="Regular; 36" backgroundColor="#25062748" transparent="1" verticalAlignment="center" />\n\t\t\t<ePixmap name="" position="210,150" size="1500,820" pixmap="MetrixHD/ibts/background.png" zPosition="-10" />\n\t\t\t<eLabel name="" position="235,227" size="1283,648" zPosition="-5" />\n\t\t\t<ePixmap pixmap="enigma2/icon/default.png" position="1567,284" size="90,70" zPosition="1" />\n\t\t\t<eLabel name="" position="1542,435" size="145,50" font="Regular; 28" verticalAlignment="center" horizontalAlignment="center" text="Exit" />\n\t\t\t<ePixmap pixmap="MetrixHD/buttons/buttons.png" position="214,893" size="1100,56" alphaTest="blend" zPosition="100" />\n\t\t\t<widget name="key_red" position="235,893" size="354,56" zPosition="1" font="Regular; 28" horizontalAlignment="center" verticalAlignment="center" backgroundColor="#9f1313" transparent="0" foregroundColor="#cccccc" />\n\t\t\t<widget name="key_green" position="602,893" size="354,56" zPosition="1" font="Regular; 28" horizontalAlignment="center" verticalAlignment="center" backgroundColor="#1f771f" transparent="0" foregroundColor="#cccccc" />\n\t\t\t<widget name="key_yellow" position="969,893" size="354,56" zPosition="1" font="Regular; 28" horizontalAlignment="center" verticalAlignment="center" backgroundColor="#a08500" transparent="0" foregroundColor="#cccccc" />\n\t\t\t<widget name="config" position="250,240" size="1260,244" scrollbarMode="showOnDemand" font="Regular; 28" itemHeight="48" selectionPixmap="MetrixHD/SkinDesign/CoolNow.png" transparent="1" scrollbarSliderforegroundColor="#cccccc" scrollbarBorderColor="#25062748" />\n\t\t\t<widget name="tempc"  position="250,550"  size="680,50" font="Regular; 28" verticalAlignment="center" horizontalAlignment="left" />\n\t\t\t<widget name="voltc"  position="250,610"  size="680,50" font="Regular; 28" verticalAlignment="center" horizontalAlignment="left" />\n\t\t\t<widget name="frqc"   position="250,670"  size="680,50" font="Regular; 28" verticalAlignment="center" horizontalAlignment="left" />\n\t\t\t<widget name="frqc2"   position="250,730"  size="680,50" font="Regular; 28" verticalAlignment="center" horizontalAlignment="left" />\n\t\t\t\n\t\t\t<eLabel name="" position="1542,372" size="145,50" font="Regular; 28" verticalAlignment="center" horizontalAlignment="center" text="OK" />\n\t\t\t</screen>'
        Screen.__init__(self, session)
        self.onClose.append(self.abort)
        self.onChangedEntry = []
        self.list = []
        ConfigListScreen.__init__(self, self.list, self.session, self.changedEntry, **('session', 'on_change'))
        self.createSetup()
        self['key_red'] = Button(_('Cancel'))
        self['key_green'] = Button(_('Save'))
        self['key_yellow'] = Button(_('Test'))
        self['setupActions'] = ActionMap([
            'SetupActions',
            'ColorActions'], {
            'save': self.save,
            'cancel': self.cancel,
            'ok': self.save,
            'yellow': self.Test}, -2)

    def createSetup(self):
        print('[AmlFRQ] createSetup initializing')
        self.editListEntry = None
        self.list = []
        self.list.append(getConfigListEntry(_('Set MAX CPU frequency for cores  0 and 1'), config.plugins.aml.maxfrq))
        self.list.append(getConfigListEntry(_('Set MIN CPU frequency for cores  0 and 1'), config.plugins.aml.minfrq))
        self.list.append(getConfigListEntry(_('Set MAX CPU frequency for cores  2, 3, 4 and 5'), config.plugins.aml.maxfrq2))
        self.list.append(getConfigListEntry(_('Set MIN CPU frequency for cores  2, 3, 4 and 5'), config.plugins.aml.minfrq2))
        self.list.append(getConfigListEntry(_('Set Scaling governor'), config.plugins.aml.governor))
        self['config'].list = self.list
        self['config'].l.setList(self.list)
        self['tempc'] = Label()
        self['voltc'] = Label()
        self['frqc'] = Label()
        self['frqc2'] = Label()
        self.timer = eTimer()
        if self.getcurrentData not in self.timer.callback:
            print('[AmlFRQ] createSetup in Timer')
            self.timer.callback.append(self.getcurrentData)
            self.timer.start(2000, True)

    def getcurrentData(self):
        self.temp = 'N/A'
        self.voltage = 'N/A'
        self.cfrq = 'N/A'
        self.cfrq2 = 'N/A'
        if platform == "dmamlogic":
            try:
                f = open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq', 'r')
                self.cfrq = f.read()
                self.cfrq = self.cfrq.strip()
                f.close()
                f = open('/sys/devices/system/cpu/cpu2/cpufreq/scaling_cur_freq', 'r')
                self.cfrq2 = f.read()
                self.cfrq2 = self.cfrq2.strip()
                f.close()
                f = open('/proc/stb/fp/temp_sensor_avs', 'r')
                self.temp = f.read()
                self.temp = self.temp.strip()
                f.close()
                f = open('/sys/devices/system/cpu/cpufreq/policy0/brcm_avs_voltage', 'r')
                self.voltage = f.read()
                self.voltage = self.voltage.strip()
                f.close()
            finally:
                pass

            try:
                self.cfrq = str(int(self.cfrq.strip()) / 1000)
                self.cfrq2 = str(int(self.cfrq2.strip()) / 1000)
                self.voltage = str(int(self.voltage, 16))
            finally:
                pass
            self['tempc'].setText(_('Current Temperature (SoC):  ' + self.temp + ' C'))
            self.icfrq = int(float(self.cfrq))
            if self.icfrq >= 500 and self.icfrq <= 1200:
                self.voltage = '0.731'
            elif self.icfrq == 1398:
                self.voltage = '0.761'
            elif self.icfrq == 1512:
                self.voltage = '0.791'
            elif self.icfrq == 1608:
                self.voltage = '0.831'
            elif self.icfrq == 1704:
                self.voltage = '0.961'
            elif self.icfrq == 1800:
                self.voltage = '0.981'

        self['voltc'].setText(_('Current CPU cores 0 and 1 Voltage:  ' + self.voltage + ' V'))
        self['frqc'].setText(_('Current CPU Frequency cores 0 and 1:  ' + self.cfrq + ' MHz'))
        self['frqc2'].setText(_('Current CPU Frequency other cores:  ' + self.cfrq2 + ' MHz'))
        self.timer.start(1000, True)

    def changedEntry(self):
        for x in self.onChangedEntry:
            x()
        self.newConfig()

    def newConfig(self):
        print(self['config'].getCurrent()[0])
        if self['config'].getCurrent()[0] == _('Start Boot Frequency'):
            self.createSetup()
            return None

    def abort(self):
        self.timer.stop()
        if self.getcurrentData in self.timer.callback:
            self.timer.callback.remove(self.getcurrentData)
        print('[AmlFRQ] aborting')

    def save(self):
        for x in self['config'].list:
            x[1].save()
        configfile.save()
        initBooster()
        self.close()

    def cancel(self):
        initBooster()
        for x in self['config'].list:
            x[1].cancel()
        self.close()

    def Test(self):
        initBooster()


class U5_Booster:

    def __init__(self, session):
        print('[AmlFRQ] U5_Booster initializing')
        self.session = session
        self.service = None
        self.onClose = []
        initBooster()

    def shutdown(self):
        self.abort()

    def abort(self):
        self.timer.stop()
        if self.getcurrentData in self.timer.callback:
            self.timer.callback.remove(self.getcurrentData)
        print('[AmlFRQ] U5_Booster aborting')

    config.misc.standbyCounter.addNotifier(standbyCounterChanged, False, **('initial_call',))


def main(menuid):
    if menuid != 'system':
        return []
    return [
        (None('CPU Control'), startBooster, 'CPU Control', None)]


def startBooster(session, **kwargs):
    session.open(AmlFRQ)


wbooster = None
gReason = -1
mySession = None


def dinobotbooster():
    global wbooster, wbooster
    if gReason == 0 and mySession != None and wbooster == None:
        print('[AmlFRQ] Dinobooster Starting !!')
        wbooster = U5_Booster(mySession)
        return None
    if None == 1 and wbooster != None:
        print('[AmlFRQ] Dinobooster Stopping !!')
        wbooster = None


def sessionstart(reason, **kwargs):
    global mySession, gReason
    print('[AmlFRQ] sessionstart')
    if 'session' in kwargs:
        mySession = kwargs['session']
    else:
        gReason = reason
    dinobotbooster()


def Plugins(**kwargs):
    return [
        PluginDescriptor([
            PluginDescriptor.WHERE_AUTOSTART,
            PluginDescriptor.WHERE_SESSIONSTART], sessionstart, **('where', 'fnc')),
        PluginDescriptor('FRQ Setup', 'Set CPU speed settings', PluginDescriptor.WHERE_MENU, main, **('name', 'description', 'where', 'fnc'))]
