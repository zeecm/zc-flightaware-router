from typing import Optional

import pandas as pd
from loguru import logger
from PySide6.QtCore import (
    QAbstractTableModel,
    QItemSelection,
    QModelIndex,
    QSettings,
    Qt,
    Signal,
)
from PySide6.QtWidgets import QDialog, QTableView, QWidget

from zc_flightplan_toolkit.qdesigner_generated_ui.generated_settings import (
    Ui_preferences_dialog,
)


class CustomQTableView(QTableView):
    selection_changed = Signal()

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

    def selectionChanged(
        self, selected: QItemSelection, deselected: QItemSelection
    ) -> None:
        self.selection_changed.emit()
        return super().selectionChanged(selected, deselected)


class PandasModel(QAbstractTableModel):
    """A model to interface a Qt view with pandas dataframe"""

    def __init__(
        self,
        dataframe: pd.DataFrame,
        show_index: bool = False,
        show_headers: bool = True,
        parent=None,
    ):
        QAbstractTableModel.__init__(self, parent)
        self._dataframe = dataframe
        self._show_index = show_index
        self._show_headers = show_headers

    def rowCount(self, parent=QModelIndex()) -> int:
        """Override method from QAbstractTableModel

        Return row count of the pandas DataFrame
        """
        return len(self._dataframe) if parent == QModelIndex() else 0

    def columnCount(self, parent=QModelIndex()) -> int:
        """Override method from QAbstractTableModel

        Return column count of the pandas DataFrame
        """
        return len(self._dataframe.columns) if parent == QModelIndex() else 0

    def data(
        self, index: QModelIndex, role: Qt.ItemDataRole = Qt.ItemDataRole.DisplayRole
    ):
        """Override method from QAbstractTableModel

        Return data cell from the pandas DataFrame
        """
        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            return str(self._dataframe.iloc[index.row(), index.column()])

        return None

    def headerData(
        self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole
    ):
        """Override method from QAbstractTableModel

        Return dataframe index as vertical header data and columns as horizontal header data.
        """
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return (
                    str(self._dataframe.columns[section])
                    if self._show_headers
                    else None
                )

            if orientation == Qt.Orientation.Vertical:
                return str(self._dataframe.index[section]) if self._show_index else None

        return None

    def get_data(self, view: bool = True) -> pd.DataFrame:
        return self._dataframe if view else self._dataframe.copy()


class PreferencesDialog(QDialog):
    def __init__(
        self,
        parent: Optional[QWidget] = None,
        default_aero_api_key: str = "",
        default_checkwx_api_key: str = "",
    ):
        super().__init__(parent)
        self.ui = Ui_preferences_dialog()
        self.ui.setupUi(self)
        self.ui.aero_api_key_lineedit.setText(default_aero_api_key)
        self.ui.checkwx_api_key_lineedit.setText(default_checkwx_api_key)

        self.aero_api_key = default_aero_api_key
        self.checkwx_api_key = default_checkwx_api_key

    def exec(self) -> bool:
        if super().exec():
            self.aero_api_key = self.ui.aero_api_key_lineedit.text()
            self.checkwx_api_key = self.ui.checkwx_api_key_lineedit.text()
            return True
        return False


class ToolkitPreferences:
    def __init__(self):
        self.setting_handler = QSettings("ZhaoCong", "FlightPlanner")

    def get_setting(self, setting: str, default_setting: str = "") -> str:
        try:
            return str(self.setting_handler.value(setting, default_setting))
        except EOFError:
            return ""

    def set_setting(self, setting: str, value: str) -> bool:
        value_changed = self._value_changed(setting, value)
        self.setting_handler.setValue(setting, value)
        return value_changed

    def _value_changed(self, setting: str, new_value: str) -> bool:
        old_value = self.get_setting(setting)
        return old_value != new_value
