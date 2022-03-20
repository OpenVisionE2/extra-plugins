#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from Components.Button import Button
from Components.ActionMap import ActionMap
from Components.MenuList import MenuList
from Components.Sources.List import List
from Components.PluginList import resolveFilename
from Components.Task import Task, Job, job_manager, Condition
from Screens.MessageBox import MessageBox
from Screens.Screen import Screen
from Screens.TaskView import JobView
from Tools.Downloader import downloadWithProgress
from Tools.LoadPixmap import LoadPixmap
from Tools.Directories import SCOPE_PLUGINS
import urllib2
import os
from Components.SystemInfo import BoxInfo


class SH4MultiChooseOnLineImage(Screen):
    skin = '<screen name="SH4MultiChooseOnLineImage" position="center,center" size="880,620" title="SH4MultiBoot - Download OnLine Images" >\n\t\t\t  <widget source="list" render="Listbox" position="10,0" size="870,610" scrollbarMode="showOnDemand" transparent="1">\n\t\t\t\t  <convert type="TemplatedMultiContent">\n\t\t\t\t  {"template": [\n\t\t\t\t  MultiContentEntryText(pos = (0, 10), size = (830, 30), font=0, flags = RT_HALIGN_RIGHT, text = 0),\n\t\t\t\t  MultiContentEntryPixmapAlphaBlend(pos = (10, 0), size = (480, 60), png = 1),\n\t\t\t\t  MultiContentEntryText(pos = (0, 40), size = (830, 30), font=1, flags = RT_VALIGN_TOP | RT_HALIGN_RIGHT, text = 3),\n\t\t\t\t  ],\n\t\t\t\t  "fonts": [gFont("Regular", 28),gFont("Regular", 20)],\n\t\t\t\t  "itemHeight": 65\n\t\t\t\t  }\n\t\t\t\t  </convert>\n\t\t\t  </widget>\n\t\t  </screen>'

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = []
        self['list'] = List(self.list)
        self.updateList()
        self['actions'] = ActionMap(['WizardActions', 'ColorActions'], {'ok': self.KeyOk,
         'back': self.close})

    def KeyOk(self):
        self.sel = self['list'].getCurrent()
        returnValue = self.sel[2]
        if returnValue is not None:
            self.session.openWithCallback(self.quit, DownloadOnLineImage, returnValue)
        return

    def updateList(self):
        self.list = []
        mypath = resolveFilename(SCOPE_PLUGINS)
        mypath = mypath + 'Extensions/SH4MultiBoot/images/'
        mypixmap = mypath + 'openatv.png'
        png = LoadPixmap(mypixmap)
        name = _('OpenATV')
        desc = _('Download latest ATV images')
        idx = 'openatv'
        res = (name,
         png,
         idx,
         desc)
        self.list.append(res)
        mypixmap = mypath + 'openar-p.png'
        png = LoadPixmap(mypixmap)
        name = _('OPENAR')
        desc = _('Download latest OpenAR-P images')
        idx = 'openar'
        res = (name,
         png,
         idx,
         desc)
        self.list.append(res)
        self['list'].list = self.list

    def quit(self):
        self.close()


class DownloadOnLineImage(Screen):
    skin = '\n\t<screen position="center,center" size="560,500" title="SH4MultiBoot - Download Image">\n\t\t<ePixmap position="0,460"   zPosition="1" size="140,40" pixmap="buttons/red.png" transparent="1" alphatest="on" />\n\t\t<ePixmap position="140,460" zPosition="1" size="140,40" pixmap="buttons/green.png" transparent="1" alphatest="on" />\n\t\t<widget name="key_red" position="0,460" zPosition="2" size="140,40" valign="center" halign="center" font="Regular;21" transparent="1" shadowColor="black" shadowOffset="-1,-1" />\n\t\t<widget name="key_green" position="140,460" zPosition="2" size="140,40" valign="center" halign="center" font="Regular;21" transparent="1" shadowColor="black" shadowOffset="-1,-1" />\n\t\t<widget name="imageList" position="10,10" zPosition="1" size="550,450" font="Regular;20" scrollbarMode="showOnDemand" transparent="1" />\n\t</screen>'

    def __init__(self, session, distro):
        Screen.__init__(self, session)
        self.session = session
        Screen.setTitle(self, _('SH4MultiBoot - Download Image'))
        self['key_green'] = Button(_('Install'))
        self['key_red'] = Button(_('Exit'))
        self.filename = None
        self.imagelist = []
        self.simulate = False
        self.imagePath = '/media/sh4multiboot/SH4MultiBootUpload'
        self.distro = distro
        if self.distro == 'openar':
            self.feed = 'openar'
            self.feedurl = 'http://taapat.ho.ua/Download'
        else:
            self.feed = 'openatv'
            self.feedurl = 'http://images.mynonpublic.com/openatv/6.4'
        self['imageList'] = MenuList(self.imagelist)
        self['actions'] = ActionMap(['OkCancelActions', 'ColorActions'], {'green': self.green,
         'red': self.quit,
         'cancel': self.quit}, -2)
        self.onLayoutFinish.append(self.layoutFinished)
        return

    def quit(self):
        self.close()

    def box(self):
        box = BoxInfo.getItem("model")
        urlbox = box
        stb = '1'
        if self.distro == 'openatv':
            if box == "spark":
                box = "fulanspark1"
                urlbox = box
            elif box == "spark7162":
                box = "sparktriplex"
                urlbox = box
        return (box, urlbox, stb)

    def green(self, ret=None):
        sel = self['imageList'].l.getCurrentSelection()
        if sel == None:
            print('[SH4MultiBoot-Download] Nothing to select!')
            return
        else:
            file_name = self.imagePath + '/' + sel
            self.filename = file_name
            self.sel = sel
            box = self.box()
            self.hide()
            url = self.feedurl + '/' + box[0] + '/' + sel
            print('[SH4MultiBoot-Download] Image download URL: ', url)
            try:
                u = urllib2.urlopen(url)
            except:
                self.session.open(MessageBox, _('The URL to this image is not correct!'), type=MessageBox.TYPE_ERROR)
                self.close()

            open(file_name, 'wb')
            meta = u.info()
            file_size = int(meta.getheaders('Content-Length')[0])
            print('[SH4MultiBoot-Download] Downloading: %s Bytes: %s' % (sel, file_size))
            job = ImageDownloadJob(url, file_name, sel)
            job.afterEvent = 'close'
            job_manager.AddJob(job)
            job_manager.failed_jobs = []
            self.session.openWithCallback(self.ImageDownloadCB, JobView, job, backgroundable=False, afterEventChangeable=False)
            return

    def ImageDownloadCB(self, ret):
        if ret:
            return
        elif job_manager.active_job:
            job_manager.active_job = None
            self.close()
            return
        else:
            if len(job_manager.failed_jobs) == 0:
                self.session.openWithCallback(self.startInstall, MessageBox, _('Do you want to install this image now?'), default=False)
            else:
                self.session.open(MessageBox, _('Download failed!'), type=MessageBox.TYPE_ERROR)
            return

    def startInstall(self, ret=None):
        if ret:
            from Plugins.Extensions.SH4MultiBoot.plugin import SH4MultiBootImageInstall
            self.session.openWithCallback(self.quit, SH4MultiBootImageInstall)
        else:
            self.close()

    def layoutFinished(self):
        box = self.box()[0]
        urlbox = self.box()[1]
        stb = self.box()[2]
        print('[SH4MultiBoot-Download] Feed URL: ', self.feedurl)
        print('[SH4MultiBoot-Download] STB: ', box)
        print('[SH4MultiBoot-Download] URL-Box: ', urlbox)
        self.imagelist = []
        if stb != '1':
            url = self.feedurl
        elif self.distro in ('openatv'):
            url = '%s/index.php?open=%s' % (self.feedurl, box)
        elif self.distro == 'openar':
            url = '%s' % (self.feedurl)
        else:
            url = self.feedurl
        print('[SH4MultiBoot-Download] URL: ', url)
        req = urllib2.Request(url)
        try:
            response = urllib2.urlopen(req)
        except urllib2.URLError as e:
            print('[SH4MultiBoot-Download] URL error: %s' % e)
            return

        try:
            the_page = response.read()
        except urllib2.HTTPError as e:
            print('[SH4MultiBoot-Download] HTTP download error: %s' % e.code)
            return

        lines = the_page.split('\n')

        tt = len(box)
        fobj = open("/tmp/output.txt", "w")
        if stb == '1':
            for line in lines:
                fobj.write(line)
                if line.find("<a href='%s/" % box) > -1:
                    t = line.find("<a href='%s/" % box)
                    t2 = line.find("'>egami")
                    t3 = line.find("'>atemio")
                    if self.feed in 'openatv':
                        self.imagelist.append(line[t + tt + 10:t + tt + tt + 39])
                elif line.find('<a href="download.php?file=' + box + '/') > -1:
                    t4 = line.find('file=' + box)
                    t5 = line.find('.zip" class="')
                    self.imagelist.append(line[t4 + len(box) + 6:t5 + 4])
                elif line.find('href="TaapatOpenAR-') > -1:
                    t4 = line.find('TaapatOpenAR-')
                    t5 = line.find('.zip"')
                    self.imagelist.append(line[t4:t5 + 4])
                elif line.find("<a href='%s/" % urlbox) > -1:
                    ttt = len(urlbox)
                    t = line.find("<a href='%s/" % urlbox)
                    t5 = line.find(".zip'")
                    self.imagelist.append(line[t + ttt + 10:t5 + 4])
            fobj.close()
        else:
            self.imagelist.append(stb)
        self['imageList'].l.setList(self.imagelist)


class ImageDownloadJob(Job):

    def __init__(self, url, filename, file):
        Job.__init__(self, _('Downloading %s' % file))
        ImageDownloadTask(self, url, filename)


class DownloaderPostcondition(Condition):

    def check(self, task):
        return task.returncode == 0

    def getErrorMessage(self, task):
        return self.error_message


class ImageDownloadTask(Task):

    def __init__(self, job, url, path):
        Task.__init__(self, job, _('Downloading'))
        self.postconditions.append(DownloaderPostcondition())
        self.job = job
        self.url = url
        self.path = path
        self.error_message = ''
        self.last_recvbytes = 0
        self.error_message = None
        self.download = None
        self.aborted = False
        return

    def run(self, callback):
        self.callback = callback
        self.download = downloadWithProgress(self.url, self.path)
        self.download.addProgress(self.download_progress)
        self.download.start().addCallback(self.download_finished).addErrback(self.download_failed)
        print('[SH4MultiBoot-Download] Downloading', self.url, 'to', self.path)

    def abort(self):
        print('[SH4MultiBoot-Download] Aborting', self.url)
        if self.download:
            self.download.stop()
        self.aborted = True

    def download_progress(self, recvbytes, totalbytes):
        if recvbytes - self.last_recvbytes > 10000:
            self.progress = int(100 * (float(recvbytes) / float(totalbytes)))
            self.name = _('Downloading') + ' ' + '%d of %d kBytes' % (recvbytes / 1024, totalbytes / 1024)
            self.last_recvbytes = recvbytes

    def download_failed(self, failure_instance=None, error_message=''):
        self.error_message = error_message
        if error_message == '' and failure_instance is not None:
            self.error_message = failure_instance.getErrorMessage()
        Task.processFinished(self, 1)
        return

    def download_finished(self, string=''):
        if self.aborted:
            self.finish(aborted=True)
        else:
            Task.processFinished(self, 0)
