import requests
import json
import logging

LOG = logging.getLogger(__name__)
BASE_URL = 'http://{0}:1925/1/{1}'
TIMEOUT = 5.0
CONNFAILCOUNT = 5

class PhilipsTV(object):
    def __init__(self, host):
        self._host = host
        self._connfail = 0
        self.on = None
        self.name = None
        self.min_volume = None
        self.max_volume = None
        self.volume = None
        self.muted = None
        self.sources = None
        self.source_id = None
        self.channels = None
        self.channel_id = None

    def _getReq(self, path):
        try:
            if self._connfail:
                LOG.debug("Connfail: %i", self._connfail)
                self._connfail -= 1
                return None
            resp = requests.get(BASE_URL.format(self._host, path), timeout=TIMEOUT)
            self.on = True
            return json.loads(resp.text)
        except requests.exceptions.RequestException as err:
            LOG.debug("Exception: %s", str(err))
            self._connfail = CONNFAILCOUNT
            self.on = False
            return None

    def _postReq(self, path, data):
        try:
            if self._connfail:
                LOG.debug("Connfail: %i", self._connfail)
                self._connfail -= 1
                return False
            resp = requests.post(BASE_URL.format(self._host, path), data=json.dumps(data), timeout=TIMEOUT)
            self.on = True
            if resp.status_code == 200:
                return True
            else:
                return False
        except requests.exceptions.RequestException as err:
            LOG.debug("Exception: %s", str(err))
            self._connfail = CONNFAILCOUNT
            self.on = False
            return False

    def update(self):
        self.getName()
        self.getAudiodata()
        self.getSources()
        self.getSourceId()

    def getName(self):
        r = self._getReq('system/name')
        if r:
            self.name = r['name']

    def getAudiodata(self):
        audiodata = self._getReq('audio/volume')
        if audiodata:
            self.min_volume = int(audiodata['min'])
            self.max_volume = int(audiodata['max'])
            self.volume = audiodata['current']
            self.muted = audiodata['muted']
        else:
            self.min_volume = None
            self.max_volume = None
            self.volume = None
            self.muted = None

    def getChannels(self):
        r = self._getReq('channels')
        if r:
            self.channels = r

    def getChannelId(self):
        r = self._getReq('channels/current')
        if r:
            self.channel_id = r['id']

    def setChannel(self, id):
        if self._postReq('channels/current', {'id': id}):
            self.channel_id = id

    def getSources(self):
        r = self._getReq('sources')
        if r:
            self.sources = r

    def getSourceId(self):
        r = self._getReq('sources/current')
        if r:
            self.source_id = r['id']
        else:
            self.source_id = None

    def setSource(self, id):
        if self._postReq('sources/current', {'id': id}):
            self.source_id = id

    def setVolume(self, level):
        if level:
            if self.min_volume != 0 or not self.max_volume:
                self.getAudiodata()
            if not self.on:
                return
            try:
                targetlevel = int(level)
            except ValueError:
                LOG.warning("Invalid audio level %s" % str(level))
                return
            if targetlevel < self.min_volume + 1 or targetlevel > self.max_volume:
                LOG.warning("Level not in range (%i - %i)" % (self.min_volume + 1, self.max_volume))
                return
            self._postReq('audio/volume', {'current': targetlevel, 'muted': False})
            self.volume = targetlevel

    def sendKey(self, key):
        self._postReq('input/key', {'key': key})