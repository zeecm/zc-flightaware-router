from zc_flightaware_router.mainwindow import Ui_MainWindow


class FlightAwareRouter(Ui_MainWindow):
    def __init__(self):
        super(FlightAwareRouter, self).__init__()
        self.setupUi(self)
