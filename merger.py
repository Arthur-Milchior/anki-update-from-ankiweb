import json

from anki.collection import _Collection
from anki.db import DB
from anki.utils import ids2str
from aqt import mw


def merge(col: _Collection, db_path: str):
    """Incorporate db in collection.

    Copy missing revlog.
    Keep most recent card. (Don't incorporate cards not in col)
    Keep more recent note if they have the same number of fields, otherwise ignore.
    """
    col.db.commit()
    col.db.execute(f"""attach database "{db_path}" as "incorporate" """)
    col.db.execute("""
insert or replace into cards
select inc.id, inc.nid, inc.did, inc.ord, inc.mod, inc.usn, inc.type, inc.queue, inc.due, inc.ivl, inc.factor, inc.reps, inc.lapses, inc.left, inc.odue, inc.odid, inc.flags, inc.data 
from incorporate.cards as inc inner join cards as current on current.id = inc.id
where inc.mod > current.mod
    """)
    col.db.execute("""
insert or ignore into revlog
select *
from incorporate.revlog as inc
where inc.id not in (select id from revlog)
;""")
    inc_models = json.loads(mw.col.db.scalar(
        "select models from incorporate.col"))
    same_models = []
    for mid, inc_model in enumerate(inc_models):
        cur_model = col.models.get(mid)
        if cur_model and cur_model['mod'] == inc_model['mod']:
            same_models.append(mid)
    col.db.execute(f"""
insert or replace into notes
select inc.id, inc.guid, inc.mid, inc.mod, inc.usn, inc.tags, inc.flds, inc.sfld, inc.csum, inc.flags, inc.data
from incorporate.notes as inc inner join notes as current on current.id = inc.id and current.mid = inc.mid
where inc.mod > current.mod and current.mid in {ids2str(same_models)}
    """)
    col.db.commit()
    col.db.execute("""detach database "incorporate" """)
