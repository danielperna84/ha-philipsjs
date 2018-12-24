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
        self.api_version = int(api_version)
        self.on = None
        self.name = None
        self.system = None
        self.min_volume = None
        self.max_volume = None
        self.volume = None
        self.muted = None
        self.sources = None
        self.source_id = None
        self.channels = None
        self.channel_id = None
        self.session = requests.Session()

    def _getReq(self, path):
        try:
            if self._connfail:
                LOG.debug("Connfail: %i", self._connfail)
                self._connfail -= 1
                return None
            with self.session.get(BASE_URL.format(self._host, self.api_version, path), timeout=TIMEOUT) as resp:
                if resp.status_code != 200:
                    return None
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
            with self.session.post(BASE_URL.format(self._host, self.api_version, path), data=json.dumps(data), timeout=TIMEOUT) as resp:
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
        self.getSystem()
        self.getAudiodata()
        self.getSources()
        self.getSourceId()

    def getSystem(self):
        r = self._getReq('system')
        if r:
            self.system = r
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
        if self.api_version >= 5:
            self.channels = {}
            for channelListId in self.getChannelLists():
                r = self._getReq(
                    'channeldb/tv/channelLists/{}'.format(channelListId)
                )
                if r:
                    for channel in r.get('Channel', []):
                        self.channels[channel['ccid']] = channel
        else:
            r = self._getReq('channels')
            if r:
                self.channels = r

    def getChannelId(self):
        if self.api_version >= 5:
            r = self._getReq('activities/tv')
            if r and r['channel']:
                # it could be empty if HDMI is set
                self.channel_id = r['channel']['ccid']
            else:
                self.channel_id = None
        else:
            r = self._getReq('channels/current')
            if r:
                self.channel_id = r['id']

    def getChannelName(self, ccid):
        return self.channels.get(ccid, dict()).get('name', None)

    def setChannel(self, ccid):
        if self.api_version >= 5:
            def setChannelBody(ccid):
                return {"channelList": {"id": "alltv"}, "channel": {"ccid": ccid}}
            if self._postReq('activities/tv', setChannelBody(ccid)):
                self.channel_id = ccid
        else:
            if self._postReq('channels/current', {'id': ccid}):
                self.channel_id = ccid

    def getChannelLists(self):
        if self.api_version >= 6:
            r = self._getReq('channeldb/tv')
            if r:
                # could be alltv and allsat
                return [l['id'] for l in r.get('channelLists', [])]
            else:
                return []
        else:
            return ['alltv']

    def getSources(self):
        self.sources = []
        if self.api_version < 5:
            r = self._getReq('sources')
            if r:
                self.sources = r

    def getSourceId(self):
        if self.api_version < 5:
            r = self._getReq('sources/current')
            if r:
                self.source_id = r['id']
            else:
                self.source_id = None

    def getSourceName(self, srcid):
        if self.api_version < 5:
            return self.sources.get(srcid, dict()).get('name', None)

    def setSource(self, source_id):
        if self.api_version < 5:
            if self._postReq('sources/current', {'id': source_id}):
                self.source_id = source_id

    def setVolume(self, level, muted=False):
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
            self._postReq('audio/volume', {'current': targetlevel, 'muted': muted})
            self.volume = level
            self.muted = muted

    def sendKey(self, key):
        self._postReq('input/key', {'key': key})

    def openURL(self, url):
        if self.api_version >= 6:
            if (
                self.system and "browser" in (
                    self.system.get("featuring", {}).get("jsonfeatures", {}).get("activities", [])
                )
            ):
                self._postReq('activities/browser', {'url': url})
