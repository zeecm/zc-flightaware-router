from zc_flightaware_router.mainwindow import Ui_mainWindow
from PySide6.QtWidgets import QMainWindow
from zc_flightaware_router.flightaware_api import FlightAwareAPI
from zc_flightaware_router.gui_classes import PandasModel

class FlightAwareRouter(QMainWindow):
    def __init__(self, api: FlightAwareAPI = FlightAwareAPI()):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self._api = api
        
        self.ui.get_airport_info_button.clicked.connect(self._get_airport_button_clicked)
        self.ui.get_route_info_button.clicked.connect(self._get_route_info_button_clicked)

    def _get_airport_button_clicked(self):
        airport_id = self.ui.airport_id_lineedit.text()
        airport_info = self._api.get_airport_information(airport_id)
        
        model = PandasModel(airport_info)
        self.ui.airport_info_table.setModel(model)
        self.ui.airport_info_table.resizeColumnsToContents()
        self.ui.airport_info_table.resizeRowsToContents()
        
    def _get_route_info_button_clicked(self):
        start_airport_id = self.ui.start_airport_lineedit.text()
        end_airport_id = self.ui.end_airport_lineedit.text()
        
        route_info = self._api.get_route_info(start_airport_id, end_airport_id)
        model = PandasModel(route_info)
        self.ui.route_info_table.setModel(model)
        self.ui.route_info_table.resizeColumnsToContents()
        self.ui.route_info_table.resizeRowsToContents()