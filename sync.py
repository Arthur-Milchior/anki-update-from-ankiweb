from typing import Optional

import anki
from anki.sync import HttpSyncer, RemoteServer
from anki.utils import platDesc
from aqt import mw


class Downloader(HttpSyncer):
    def __init__(self, col, hkey, client, hostNum) -> None:
        HttpSyncer.__init__(self, hkey, client, hostNum=hostNum)
        self.postVars = dict(
            k=self.hkey, v="ankidesktop,%s,%s" % (anki.version, platDesc()),
        )
        self.col = col

    def download(self) -> Optional[str]:
        tpath = self.col.path + ".tmp"
        cont = self.req("download")
        if cont == "upgradeRequired":
            return None
        open(tpath, "wb").write(cont)
        return tpath


def dl():
    """return a path to a downloaded version of the collection."""
    hkey = mw.pm.profile["syncKey"]
    hostNum = mw.pm.profile.get("hostNum")
    server = RemoteServer(hkey, hostNum)
    dl = Downloader(mw.col, hkey, server.client, hostNum=hostNum)
    return dl.download()
