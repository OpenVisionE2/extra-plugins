AC_INIT([enigma2-extra-plugins],[1.0])SparkUnionTunerType/Makefile
SparkUnionTunerType/src/Makefile
SparkUnionTunerType/po/Makefile
SparkUnionTunerType/meta/Makefile
AM_INIT_AUTOMAKE([dist-bzip2 foreign no-define tar-pax])
AC_CONFIG_HEADERS([enigma2-plugins-config.h])

# Silent rules are available since 1.11, but older versions
# are still in use. So don't use them unconditionally.
m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])

AC_USE_SYSTEM_EXTENSIONS
AC_SYS_LARGEFILE

AC_PROG_CC
AC_PROG_CXX
m4_ifdef([LT_INIT], [LT_INIT], [AC_PROG_LIBTOOL])
AC_CONFIG_MACRO_DIR([m4])

AC_CHECK_HEADERS([dbox/fp.h dbox/lcd-ks0713.h])

AC_PATH_PROG(MSGFMT, msgfmt, AC_MSG_ERROR(Could not find msgfmt))
AC_PATH_PROG(MSGINIT, msginit, AC_MSG_ERROR(Could not find msginit))
AC_PATH_PROG(MSGMERGE, msgmerge, AC_MSG_ERROR(Could not find msgmerge))
AC_PATH_PROG(MSGUNIQ, msguniq, AC_MSG_ERROR(Could not find msguniq))
AC_PATH_PROG(XGETTEXT, xgettext, AC_MSG_ERROR(Could not find xgettext))

AM_PATH_PYTHON
AX_PYTHON_DEVEL
AX_PTHREAD

AC_ARG_WITH(arch,
	AS_HELP_STRING([--with-arch],[build for ARCH, $withval]),
	[ARCH="$withval"],[ARCH=""])
AC_SUBST(ARCH)
AC_DEFINE_UNQUOTED(ARCH,"$ARCH",[box architecture])

AM_CONDITIONAL(MIPSEL, test `echo "$ARCH" | cut -b 1-6` == "mipsel")

AC_ARG_WITH(boxtype,
	AS_HELP_STRING([--with-boxtype],[build for BOXTYPE, $withval]),
	[BOXTYPE="$withval"],[BOXTYPE=""])
AC_SUBST(BOXTYPE)
AC_DEFINE_UNQUOTED(BOXTYPE,"$BOXTYPE",[box type])

AC_ARG_WITH(boxbrand,
	AS_HELP_STRING([--with-boxbrand],[build for BOXBRAND, $withval]),
	[BOXBRAND="$withval"],[BOXBRAND=""])
AC_SUBST(BOXBRAND)
AC_DEFINE_UNQUOTED(BOXBRAND,"$BOXBRAND",[box brand])

AC_ARG_WITH(stbplatform,
	AS_HELP_STRING([--with-stbplatform],[build for STBPLATFORM, $withval]),
	[STBPLATFORM="$withval"],[STBPLATFORM=""])
AC_SUBST(STBPLATFORM)
AC_DEFINE_UNQUOTED(STBPLATFORM,"$STBPLATFORM",[stb platform])

AC_CONFIG_FILES([
Makefile

AmlFRQ/Makefile
AmlFRQ/src/Makefile
AmlFRQ/po/Makefile

AttoVFDControl/Makefile
AttoVFDControl/src/Makefile
AttoVFDControl/meta/Makefile
AttoVFDControl/po/Makefile

AudioEffect/Makefile
AudioEffect/src/Makefile
AudioEffect/meta/Makefile
AudioEffect/po/Makefile

autoBLchanger/Makefile
autoBLchanger/meta/Makefile
autoBLchanger/po/Makefile
autoBLchanger/src/Makefile
autoBLchanger/src/images/Makefile

Blindscan/Makefile
Blindscan/src/Makefile
Blindscan/meta/Makefile
Blindscan/po/Makefile

BrcmFRQ/Makefile
BrcmFRQ/src/Makefile
BrcmFRQ/po/Makefile

BTDevicesManager/Makefile
BTDevicesManager/src/Makefile
BTDevicesManager/meta/Makefile
BTDevicesManager/po/Makefile

ChannelsImporter/Makefile
ChannelsImporter/meta/Makefile
ChannelsImporter/po/Makefile
ChannelsImporter/src/Makefile

Chefkoch/Makefile
Chefkoch/meta/Makefile
Chefkoch/src/Makefile
Chefkoch/src/db/Makefile
Chefkoch/src/pic/Makefile
Chefkoch/src/pic/FHD/Makefile
Chefkoch/src/pic/HD/Makefile

DLNABrowser/Makefile
DLNABrowser/src/Makefile
DLNABrowser/icons/Makefile
DLNABrowser/po/Makefile
DLNABrowser/meta/Makefile

DLNAServer/Makefile
DLNAServer/src/Makefile
DLNAServer/po/Makefile
DLNAServer/meta/Makefile

DMBlindscan/src/Makefile
DMBlindscan/po/Makefile
DMBlindscan/Makefile
DMBlindscan/meta/Makefile
DMBlindscan/src/images/Makefile

EPGTranslator/Makefile
EPGTranslator/meta/Makefile
EPGTranslator/po/Makefile
EPGTranslator/src/Makefile
EPGTranslator/src/pic/Makefile
EPGTranslator/src/pic/buttons/Makefile
EPGTranslator/src/pic/flag/Makefile

ABMCustomMixImporter/Makefile
ABMCustomMixImporter/meta/Makefile
ABMCustomMixImporter/po/Makefile
ABMCustomMixImporter/src/Makefile
ABMCustomMixImporter/mixes/Makefile

AboutBoxBranding/Makefile
AboutBoxBranding/meta/Makefile
AboutBoxBranding/po/Makefile
AboutBoxBranding/src/Makefile

Fempa/Makefile
Fempa/meta/Makefile
Fempa/src/Makefile
Fempa/po/Makefile

FirmwareUpgrade/Makefile
FirmwareUpgrade/src/Makefile
FirmwareUpgrade/meta/Makefile
FirmwareUpgrade/po/Makefile

FPGAUpgrade/Makefile
FPGAUpgrade/src/Makefile
FPGAUpgrade/meta/Makefile
FPGAUpgrade/po/Makefile

GBIpboxClient/Makefile
GBIpboxClient/src/Makefile
GBIpboxClient/po/Makefile

GigaBlueRemote/Makefile
GigaBlueRemote/src/Makefile
GigaBlueRemote/meta/Makefile
GigaBlueRemote/po/Makefile

GigaBlueVFDControl/Makefile
GigaBlueVFDControl/src/Makefile
GigaBlueVFDControl/meta/Makefile
GigaBlueVFDControl/po/Makefile

IceTV/Makefile
IceTV/src/Makefile
IceTV/po/Makefile

INIVFDControl/Makefile
INIVFDControl/src/Makefile
INIVFDControl/meta/Makefile
INIVFDControl/po/Makefile

EWVFDControl/Makefile
EWVFDControl/src/Makefile
EWVFDControl/meta/Makefile
EWVFDControl/po/Makefile

F3LEDControl/Makefile
F3LEDControl/src/Makefile
F3LEDControl/meta/Makefile
F3LEDControl/po/Makefile

VPLEDControl/Makefile
VPLEDControl/src/Makefile
VPLEDControl/meta/Makefile
VPLEDControl/po/Makefile

LCD4linux/Makefile
LCD4linux/src/Makefile
LCD4linux/src/data/Makefile
LCD4linux/src/data/audio/Makefile
LCD4linux/src/data/Clock1/Makefile
LCD4linux/src/data/Clock2/Makefile
LCD4linux/src/data/Clock3/Makefile
LCD4linux/src/data/Clock4/Makefile
LCD4linux/src/data/Clock5/Makefile
LCD4linux/src/data/Clock6/Makefile
LCD4linux/src/data/Clock7/Makefile
LCD4linux/src/data/Clock8/Makefile
LCD4linux/src/data/Clock9/Makefile
LCD4linux/src/data/Clock10/Makefile
LCD4linux/src/meteo/Makefile
LCD4linux/src/renderer/Makefile
LCD4linux/src/wetter/Makefile
LCD4linux/meta/Makefile
LCD4linux/po/Makefile

LCNScanner/Makefile
LCNScanner/src/Makefile
LCNScanner/po/Makefile

LEDBrightnessSetup/Makefile
LEDBrightnessSetup/src/Makefile
LEDBrightnessSetup/meta/Makefile
LEDBrightnessSetup/po/Makefile

LottoExtended/Makefile
LottoExtended/src/Makefile
LottoExtended/po/Makefile

MICOMUpgrade/Makefile
MICOMUpgrade/src/Makefile
MICOMUpgrade/src/bin/Makefile
MICOMUpgrade/meta/Makefile
MICOMUpgrade/po/Makefile
MICOMUpgrade/buttons/Makefile

MiniTV/Makefile
MiniTV/src/Makefile
MiniTV/po/Makefile

MultiTransCodingSetup/Makefile
MultiTransCodingSetup/src/Makefile
MultiTransCodingSetup/meta/Makefile
MultiTransCodingSetup/po/Makefile

OdinM7VFDControl/Makefile
OdinM7VFDControl/src/Makefile
OdinM7VFDControl/meta/Makefile
OdinM7VFDControl/po/Makefile

OnDemand/Makefile
OnDemand/src/Makefile
OnDemand/src/icons/Makefile
OnDemand/meta/Makefile
OnDemand/po/Makefile

OpentvZapper/Makefile
OpentvZapper/src/Makefile
OpentvZapper/po/Makefile

opt9600VFD/Makefile
opt9600VFD/src/Makefile
opt9600VFD/meta/Makefile
opt9600VFD/po/Makefile

ProgrammlistenUpdater/Makefile
ProgrammlistenUpdater/src/Makefile
ProgrammlistenUpdater/po/Makefile

TransCodingSetup/Makefile
TransCodingSetup/meta/Makefile
TransCodingSetup/po/Makefile
TransCodingSetup/src/Makefile

TunerServer/Makefile
TunerServer/src/Makefile
TunerServer/meta/Makefile
TunerServer/po/Makefile

ReZap/Makefile
ReZap/src/Makefile
ReZap/meta/Makefile

RCUSelect/Makefile
RCUSelect/src/Makefile
RCUSelect/conf/Makefile
RCUSelect/po/Makefile
RCUSelect/meta/Makefile

SABnzbdSetup/Makefile
SABnzbdSetup/src/Makefile
SABnzbdSetup/po/Makefile

SatipClient/Makefile
SatipClient/src/Makefile
SatipClient/po/Makefile
SatipClient/meta/Makefile

SimpleFanControl/Makefile
SimpleFanControl/src/Makefile
SimpleFanControl/meta/Makefile
SimpleFanControl/po/Makefile

SF8VFDControl/Makefile
SF8VFDControl/src/Makefile
SF8VFDControl/meta/Makefile
SF8VFDControl/po/Makefile

SH4MultiBoot/Makefile
SH4MultiBoot/src/Makefile
SH4MultiBoot/src/bin/Makefile
SH4MultiBoot/src/images/Makefile
SH4MultiBoot/src/SH4MultiBootClient/Makefile
SH4MultiBoot/po/Makefile

StreamTV/Makefile
StreamTV/src/Makefile
StreamTV/meta/Makefile
StreamTV/po/Makefile
StreamTV/icons/Makefile

tmdb/Makefile
tmdb/src/Makefile
tmdb/src/pic/Makefile
tmdb/src/tmdbsimple/Makefile
tmdb/meta/Makefile
tmdb/po/Makefile

TVSpielfilm/Makefile
TVSpielfilm/meta/Makefile
TVSpielfilm/src/Makefile
TVSpielfilm/src/db/Makefile
TVSpielfilm/src/font/Makefile
TVSpielfilm/src/picons/Makefile
TVSpielfilm/src/pics/Makefile
TVSpielfilm/src/pics/FHD/Makefile
TVSpielfilm/src/pics/FHD/buttons/Makefile
TVSpielfilm/src/pics/FHD/icons/Makefile
TVSpielfilm/src/pics/FHD/logos/Makefile
TVSpielfilm/src/pics/FHD/selectors/Makefile
TVSpielfilm/src/pics/HD/Makefile
TVSpielfilm/src/pics/HD/buttons/Makefile
TVSpielfilm/src/pics/HD/icons/Makefile
TVSpielfilm/src/pics/HD/logos/Makefile
TVSpielfilm/src/pics/HD/selectors/Makefile

UFSVFD/Makefile
UFSVFD/src/Makefile
UFSVFD/meta/Makefile
UFSVFD/po/Makefile

USBsafe/Makefile
USBsafe/src/Makefile
USBsafe/po/Makefile

VentonFanControl/Makefile
VentonFanControl/src/Makefile
VentonFanControl/meta/Makefile
VentonFanControl/po/Makefile

VuRemote/Makefile
VuRemote/src/Makefile
VuRemote/meta/Makefile
VuRemote/po/Makefile

VuDuoFanControl/Makefile
VuDuoFanControl/src/Makefile
VuDuoFanControl/meta/Makefile
VuDuoFanControl/po/Makefile

WetekAudio/Makefile
WetekAudio/src/Makefile
WetekAudio/po/Makefile

WetekFRQ/Makefile
WetekFRQ/src/Makefile
WetekFRQ/po/Makefile

WetekSync/Makefile
WetekSync/src/Makefile

WirelessAccessPoint/Makefile
WirelessAccessPoint/src/Makefile
WirelessAccessPoint/meta/Makefile
WirelessAccessPoint/po/Makefile

xmlUpdate/Makefile
xmlUpdate/meta/Makefile
xmlUpdate/po/Makefile
xmlUpdate/src/Makefile

XtrendFanControl/Makefile
XtrendFanControl/src/Makefile
XtrendFanControl/meta/Makefile
XtrendFanControl/po/Makefile

XtrendRemote/Makefile
XtrendRemote/src/Makefile
XtrendRemote/meta/Makefile
XtrendRemote/po/Makefile

ADBVFD/Makefile
ADBVFD/src/Makefile
ADBVFD/meta/Makefile
ADBVFD/po/Makefile

CuberevoVFD/Makefile
CuberevoVFD/src/Makefile
CuberevoVFD/meta/Makefile
CuberevoVFD/po/Makefile

fs9000VFD/Makefile
fs9000VFD/src/Makefile
fs9000VFD/meta/Makefile
fs9000VFD/po/Makefile

hchsxx00VFD/Makefile
hchsxx00VFD/src/Makefile
hchsxx00VFD/meta/Makefile
hchsxx00VFD/po/Makefile

hs742xVFD/Makefile
hs742xVFD/src/Makefile
hs742xVFD/meta/Makefile
hs742xVFD/po/Makefile

hs7110VFD/Makefile
hs7110VFD/src/Makefile
hs7110VFD/meta/Makefile
hs7110VFD/po/Makefile

hs7810aVFD/Makefile
hs7810aVFD/src/Makefile
hs7810aVFD/meta/Makefile
hs7810aVFD/po/Makefile

hs8200VFD/Makefile
hs8200VFD/src/Makefile
hs8200VFD/meta/Makefile
hs8200VFD/po/Makefile

hs9510VFD/Makefile
hs9510VFD/src/Makefile
hs9510VFD/meta/Makefile
hs9510VFD/po/Makefile

pace7241VFD/Makefile
pace7241VFD/src/Makefile
pace7241VFD/meta/Makefile
pace7241VFD/po/Makefile

PiconManager/Makefile
PiconManager/meta/Makefile
PiconManager/src/Makefile
PiconManager/src/pic/Makefile
PiconManager/po/Makefile

PiconsUpdater/Makefile
PiconsUpdater/src/Makefile
PiconsUpdater/meta/Makefile
PiconsUpdater/po/Makefile

spark7162VFD/Makefile
spark7162VFD/src/Makefile
spark7162VFD/meta/Makefile
spark7162VFD/po/Makefile

SparkUnionTunerType/Makefile
SparkUnionTunerType/src/Makefile
SparkUnionTunerType/po/Makefile
SparkUnionTunerType/meta/Makefile

sparkVFD/Makefile
sparkVFD/src/Makefile
sparkVFD/meta/Makefile
sparkVFD/po/Makefile

TopfieldVFD/Makefile
TopfieldVFD/src/Makefile
TopfieldVFD/meta/Makefile
TopfieldVFD/po/Makefile

])
AC_OUTPUT
