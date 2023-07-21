import requests


def get_north_atlantic_tracks(
    url: str = "https://www.notams.faa.gov/common/nat.html",
) -> str:
    """Returns HTML representation for display in QTextBrowser"""
    response = requests.get(url, timeout=5)
    return _extract_north_atlantic_tracks(response.text).strip()


def _extract_north_atlantic_tracks(html_text: str) -> str:
    html_tr_tag = "<tr>"
    first_html_tr_tag_index = html_text.index(html_tr_tag)
    second_html_tr_tag_index = html_text.index(html_tr_tag, first_html_tr_tag_index + 1)

    return html_text[second_html_tr_tag_index:]


if __name__ == "__main__":
    tracks = get_north_atlantic_tracks()
    print(tracks)
