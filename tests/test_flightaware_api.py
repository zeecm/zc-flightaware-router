from zc_flightaware_router.flightware_api import template_function


def test_template_function():
    result = template_function(1)
    assert result == 1
