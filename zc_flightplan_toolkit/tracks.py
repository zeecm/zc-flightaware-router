import requests
from loguru import logger


def get_north_atlantic_tracks(
    url: str = "https://www.notams.faa.gov/common/nat.html",
) -> str:
    """Returns HTML representation for display in QTextBrowser"""
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        return _extract_north_atlantic_tracks(response.text).strip()
    logger.warning("Failed to retrieve north atlantic tracks data")
    return "Failed to retrieve North Atlantic Tracks Data"


def _extract_north_atlantic_tracks(html: str) -> str:
    html_tr_tag = "<tr>"
    first_html_tr_tag_index = html.index(html_tr_tag)
    second_html_tr_tag_index = html.index(html_tr_tag, first_html_tr_tag_index + 1)

    return html[second_html_tr_tag_index:]


def get_pacific_tracks(
    url: str = "https://www.notams.faa.gov/dinsQueryWeb/advancedNotamMapAction.do",
) -> str:
    form_data = {
        "queryType": "pacificTracks",
        "actionType": "advancedNOTAMFunctions",
        "submit": "Pacific Tracks",
    }
    response = requests.post(url, data=form_data)
    if response.status_code == 200:
        return _process_pacific_tracks_data(response.text)
    logger.warning("Failed to retrieve Pacific Tracks Data")
    return "Failed to retrieve Pacific Tracks Data"


def _process_pacific_tracks_data(html: str) -> str:
    start_of_data = "Data Current as of:"
    end_of_data = "End of Report"

    start_index = html.index(start_of_data)
    end_index = html.index(end_of_data)

    return html[start_index:end_index]
