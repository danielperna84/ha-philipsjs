import requests
import json
import logging

LOG = logging.getLogger(__name__)
BASE_URL = 'http://{0}:1925/{1}/{2}'
TIMEOUT = 5.0
CONNFAILCOUNT = 5
DEFAULT_API_VERSION = 1

class PhilipsTV(object):
    def __init__(self, host, api_version=DEFAULT_API_VERSION):
        self._host = host
        self._connfail = 0
        self.api_version = api_version
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
            resp = requests.get(BASE_URL.format(self._host, self.api_version, path), timeout=TIMEOUT)
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
            resp = requests.post(BASE_URL.format(self._host, self.api_version, path), data=json.dumps(data), timeout=TIMEOUT)
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
            self.volume = audiodata['current'] / self.max_volume
            self.muted = audiodata['muted']
        else:
            self.min_volume = None
            self.max_volume = None
            self.volume = None
            self.muted = None

    def getChannels(self):
        if self.api_version >= '5':
            return self.getSources()
        r = self._getReq('channels')
        if r:
            self.channels = r

    def getChannelId(self):
        if self.api_version >= '5':
            return self.getSourceId()
        r = self._getReq('channels/current')
        if r:
            self.channel_id = r['id']

    def setChannel(self, id):
        if self.api_version >= '5':
            return self.setSource(id)
        if self._postReq('channels/current', {'id': id}):
            self.channel_id = id

    def getSources(self):
        if self.api_version >= '5':
            r = self._getReq('channeldb/tv/channelLists/alltv')
            if r:
                self.sources = r['Channel']
        else:
            r = self._getReq('sources')
            if r:
                self.sources = r

    def getSourceId(self):
        if self.api_version >= '5':
            r = self._getReq('activities/tv')
            if r:
                self._source_id = r['channel']['ccid']
            else:
                self.source_id = None
        else:
            r = self._getReq('sources/current')
            if r:
                self.source_id = r['id']
            else:
                self.source_id = None

    def getSourceName(self, srcid):
        if self.api_version >= '5':
            return srcid['name']
        else:
            return self.sources.get(srcid, dict()).get('name', None)

    def setSource(self, id):
        def setChannelBody(ccid):
            return {"channelList": {"id": "alltv"}, "channel": {"ccid": ccid}}
        if self.api_version >= '5':
            if self._postReq('activities/tv', setChannelBody(id['ccid'])):
                self.source_id = id
        else:
            if self._postReq('sources/current', {'id': id}):
                self.source_id = id

    def setVolume(self, level):
        if level:
            if self.min_volume != 0 or not self.max_volume:
                self.getAudiodata()
            if not self.on:
                return
            try:
                targetlevel = int(level * self.max_volume)
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
