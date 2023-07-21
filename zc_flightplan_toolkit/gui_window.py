from typing import Optional

from loguru import logger
from PySide6.QtWidgets import QMainWindow

from zc_flightplan_toolkit.api import FlightAwareAPI, FlightInfoAPI
from zc_flightplan_toolkit.constants import Preferences
from zc_flightplan_toolkit.gui_classes import (
    PandasModel,
    PreferencesDialog,
    ToolkitPreferences,
)
from zc_flightplan_toolkit.qdesigner_generated_ui.generated_mainwindow import (
    Ui_mainWindow,
)
from zc_flightplan_toolkit.tracks import get_north_atlantic_tracks, get_pacific_tracks


class FlightPlanToolkit(QMainWindow):
    def __init__(self, api: Optional[FlightInfoAPI] = None):
        super().__init__()
        self._api: FlightInfoAPI

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.preferences = ToolkitPreferences()

        self._initialize_api(api)

        self._setup_buttons()
        self._setup_toolbar()

    def _setup_buttons(self) -> None:
        self.ui.get_airport_info_button.clicked.connect(
            self._get_and_display_airport_info
        )
        self.ui.get_route_info_button.clicked.connect(self._get_and_display_route_info)
        self.ui.get_north_atlantic_tracks_button.clicked.connect(
            self._get_north_atlantic_tracks_button_clicked
        )
        self.ui.get_pacific_tracks_button.clicked.connect(
            self._get_pacific_tracks_button_clicked
        )

    def _initialize_api(self, api: Optional[FlightInfoAPI] = None) -> None:
        aero_api_key = self.preferences.get_setting(Preferences.AERO_API_KEY.value)
        self._api = api or FlightAwareAPI(api_key=aero_api_key)

    def _setup_toolbar(self) -> None:
        self.ui.toolbar_preferences_button.triggered.connect(self._open_settings_dialog)

    def _get_and_display_airport_info(self) -> None:
        airport_id = self.ui.airport_id_lineedit.text()

        airport_info = self._api.get_airport_information(airport_id)
        model = PandasModel(airport_info)

        self.ui.airport_info_table.setModel(model)
        self.ui.airport_info_table.resizeColumnsToContents()
        self.ui.airport_info_table.resizeRowsToContents()

        self._update_datis_display()

    def _update_datis_display(self) -> None:
        airport_datis = self._api.get_datis()
        self.ui.atis_display.setPlainText(airport_datis)

    def _get_and_display_route_info(self) -> None:
        start_airport_id = self.ui.start_airport_lineedit.text()
        end_airport_id = self.ui.end_airport_lineedit.text()

        route_info = self._api.get_route_info(start_airport_id, end_airport_id)
        model = PandasModel(route_info)

        self.ui.route_info_table.setModel(model)
        self.ui.route_info_table.resizeColumnsToContents()
        self.ui.route_info_table.resizeRowsToContents()

    def _get_north_atlantic_tracks_button_clicked(self) -> None:
        tracks_data = get_north_atlantic_tracks()
        self.ui.north_atlantic_text_display.setHtml(tracks_data)

    def _get_pacific_tracks_button_clicked(self) -> None:
        tracks_data = get_pacific_tracks()
        self.ui.pacific_tracks_display.setHtml(tracks_data)

    def _open_settings_dialog(self):
        api_key = self.preferences.get_setting(Preferences.AERO_API_KEY.value)
        dialog = PreferencesDialog(default_api_key=api_key)
        if _ := dialog.exec():
            api_key = dialog.aero_api_key
        if _ := self.preferences.set_setting(Preferences.AERO_API_KEY.value, api_key):
            self._api.reinitialize(api_key=api_key)
