import pandas
import psycopg2
import MimicServer

# NOTE:
# the events ("shit that happened") are timestamped.
# the events should be browsed in temporal order
# REGARDLESS of which table it belongs to.
# DbBrowser - have multiple cursors associated with a single connection
# Megacursor will wrap all event cursors - Megacursor will have a method "fetchone()"
# just like cursor. "fetchone()" will actually not advance any of the cursors

class SubCursor:
    def __init__(self, _mimicserverplatform=None, _sqlcommand=""):
        self._mimicserverplatform = _mimicserverplatform
        self._sqlcommand = _sqlcommand

    @property
    def sqlcommand(self):
        return self._sqlcommand




# class DbBrowser(MimicServer.MimicServerPlatform):
#     def __init__(self):
#         super().__init__()
