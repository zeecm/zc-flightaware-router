import sys

import pytest

if not sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)

import pandas as pd
from pandas.testing import assert_frame_equal
from PySide6.QtCore import Qt
from pytest_mock import MockerFixture
from pytest_mock.plugin import MockType
from pytestqt.qtbot import QtBot  # type: ignore

from zc_flightplan_toolkit.gui_window import FlightPlanToolkit


@pytest.fixture(autouse=True)
def mock_fetch_metar(mocker: MockerFixture) -> MockType:
    return mocker.patch(
        "zc_flightplan_toolkit.gui_window.FlightPlanToolkit._fetch_metar"
    )


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

    toolkit = FlightPlanToolkit()
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

    toolkit = FlightPlanToolkit()
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

    toolkit = FlightPlanToolkit()
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

    toolkit = FlightPlanToolkit()
    toolkit.show()
    qtbot.addWidget(toolkit)

    qtbot.mouseClick(toolkit.ui.get_pacific_tracks_button, Qt.MouseButton.LeftButton)

    assert toolkit.ui.pacific_tracks_display.toPlainText() == "mock_tracks"


def test_settings_dialog_opens(qtbot: QtBot, mocker: MockerFixture):
    dialog_mock = mocker.patch("zc_flightplan_toolkit.gui_window.PreferencesDialog")

    preferences_mock = mocker.patch(
        "zc_flightplan_toolkit.gui_window.ToolkitPreferences"
    )
    preferences_mock.get_setting.return_value = ""
    preferences_mock.set_setting.return_value = False

    toolkit = FlightPlanToolkit()
    toolkit.show()
    qtbot.addWidget(toolkit)

    toolkit.ui.toolbar_preferences_button.trigger()

    dialog_mock.assert_called_once()


def test_datis_display_gets_populated(qtbot: QtBot, mocker: MockerFixture):
    mocker.patch(
        "zc_flightplan_toolkit.gui_window.FlightAwareAPI.get_airport_information"
    )
    datis_mock = mocker.patch(
        "zc_flightplan_toolkit.gui_window.FlightAwareAPI.get_datis"
    )
    datis_mock.return_value = "mock_datis"

    toolkit = FlightPlanToolkit()
    toolkit.show()
    qtbot.addWidget(toolkit)

    toolkit.ui.airport_id_lineedit.setText("wsss")
    qtbot.mouseClick(toolkit.ui.get_airport_info_button, Qt.MouseButton.LeftButton)

    assert toolkit.ui.atis_display.toPlainText() == "mock_datis"


def test_airport_runways_table_gets_populated(qtbot: QtBot, mocker: MockerFixture):
    mocker.patch(
        "zc_flightplan_toolkit.gui_window.FlightAwareAPI.get_airport_information"
    )
    mocker.patch(
        "zc_flightplan_toolkit.gui_window.FlightAwareAPI.get_datis", return_value=""
    )
    get_runways_mock = mocker.patch(
        "zc_flightplan_toolkit.gui_window.FlightAwareAPI.get_airport_runways"
    )
    mock_data = pd.DataFrame([{"mock_column": "mock_data"}])
    get_runways_mock.return_value = mock_data

    toolkit = FlightPlanToolkit()
    toolkit.show()
    qtbot.addWidget(toolkit)

    toolkit.ui.airport_id_lineedit.setText("wsss")
    qtbot.mouseClick(toolkit.ui.get_airport_info_button, Qt.MouseButton.LeftButton)

    assert_frame_equal(toolkit.ui.runway_info_table.model().get_data(), mock_data)  # type: ignore
    # self defined function
