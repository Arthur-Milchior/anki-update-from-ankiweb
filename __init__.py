from aqt import mw
from aqt.qt import *

from .merger import merge
from .sync import dl


def act():
    path = dl()
    if path:
        merge(mw.col, path)


action = QAction(mw)
action.setText("Partial sync")
mw.form.menuTools.addAction(action)
action.triggered.connect(act)
