"""
requests test sample

run test：
> pytest -vs test_api.py
"""


def test_post_method(post, base_url):
    """
    test post request
    """
    s = post(f'{base_url}/post', data={'key': 'value'})
    assert s.status_code == 200


def test_get_method(get, base_url):
    """
    test get request
    """
    payload = {'key1': 'value1', 'key2': 'value2'}
    s = get(f"{base_url}/get", params=payload)
    assert s.status_code == 200


def test_session(session, base_url):
    """
    test session, keep requests cookie
    """
    s = session
    s.get(f"{base_url}/cookies/set/sessioncookie/123456789")
    s.get(f"{base_url}/cookies")
