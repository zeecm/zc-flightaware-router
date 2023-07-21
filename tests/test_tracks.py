from zc_flightplan_toolkit.tracks import get_north_atlantic_tracks, get_pacific_tracks


def test_get_north_atlantic_tracks():
    tracks = get_north_atlantic_tracks()
    assert "EAST LVLS" in tracks
    assert "WEST LVLS" in tracks


def test_get_pacific_tracks():
    tracks = get_pacific_tracks()
    assert "PACOTS TRACK" in tracks
