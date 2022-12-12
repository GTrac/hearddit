import tests.utils

def test_no_user_home(test_app):
    res = test_app.get('/')
    page_data: str = res.data.decode()

    assert res.status_code == 200
    assert f'<p class="">Join Hearddit</p>' in page_data
    assert f'<a href="/login" class="nav-link btn-hearddit-primary">Log in</a>' in page_data