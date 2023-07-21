import sys

import pytest

if not sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)

from PySide6.QtCore import Qt
from pytest_mock import MockerFixture
from pytestqt.qtbot import QtBot  # type: ignore

from zc_flightplan_toolkit.gui_window import FlightAwareRouter


@pytest.mark.parametrize(
    "airport_id",
    [
        ("WSSS"),
        ("KLAX"),
        ("EGLL"),
    ],
)
def test_get_airport_button(qtbot: QtBot, mocker: MockerFixture, airport_id: str):
    get_airport_info_mock = mocker.patch(
        "zc_flightplan_toolkit.gui_window.FlightAwareAPI.get_airport_information"
    )

    toolkit = FlightAwareRouter()
    toolkit.show()
    qtbot.addWidget(toolkit)

    toolkit.ui.airport_id_lineedit.setText(airport_id)
    qtbot.mouseClick(toolkit.ui.get_airport_info_button, Qt.MouseButton.LeftButton)

    get_airport_info_mock.assert_called_once_with(airport_id)


@pytest.mark.parametrize(
    "start_id, end_id",
    [
        ("WSSS", "WMKK"),
        ("KLAX", "KJFK"),
        ("EGLL", "VVNB"),
    ],
)
def test_get_route_button(
    qtbot: QtBot, mocker: MockerFixture, start_id: str, end_id: str
):
    get_route_info_mock = mocker.patch(
        "zc_flightplan_toolkit.gui_window.FlightAwareAPI.get_route_info"
    )

    toolkit = FlightAwareRouter()
    toolkit.show()
    qtbot.addWidget(toolkit)

    toolkit.ui.start_airport_lineedit.setText(start_id)
    toolkit.ui.end_airport_lineedit.setText(end_id)
    qtbot.mouseClick(toolkit.ui.get_route_info_button, Qt.MouseButton.LeftButton)

    get_route_info_mock.assert_called_once_with(start_id, end_id)


def test_get_north_atlantic_tracks_button(qtbot: QtBot, mocker: MockerFixture):
    mocker.patch(
        "zc_flightplan_toolkit.gui_window.get_north_atlantic_tracks",
        return_value="mock_tracks",
    )

    toolkit = FlightAwareRouter()
    toolkit.show()
    qtbot.addWidget(toolkit)

    qtbot.mouseClick(
        toolkit.ui.get_north_atlantic_tracks_button, Qt.MouseButton.LeftButton
    )

    assert toolkit.ui.north_atlantic_text_display.toPlainText() == "mock_tracks"


def test_get_pacific_tracks_button(qtbot: QtBot, mocker: MockerFixture):
    mocker.patch(
        "zc_flightplan_toolkit.gui_window.get_pacific_tracks",
        return_value="mock_tracks",
    )

    toolkit = FlightAwareRouter()
    toolkit.show()
    qtbot.addWidget(toolkit)

    qtbot.mouseClick(toolkit.ui.get_pacific_tracks_button, Qt.MouseButton.LeftButton)

    assert toolkit.ui.pacific_tracks_display.toPlainText() == "mock_tracks"
