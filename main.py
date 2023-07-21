import sys

from PySide6.QtWidgets import QApplication

from zc_flightplan_toolkit.gui_window import FlightAwareRouter

if __name__ == "__main__":
    app = QApplication(sys.argv)
    router = FlightAwareRouter()
    router.show()
    sys.exit(app.exec())
