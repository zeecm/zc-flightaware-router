from zc_flightaware_router.gui_window import FlightAwareRouter
import sys
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    router = FlightAwareRouter()
    router.show()
    sys.exit(app.exec())