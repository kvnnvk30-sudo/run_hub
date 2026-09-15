import pytest


@pytest.mark.parametrize(
    'title,suite_name,duration_seconds,status',
    [
        ('name_max', 'robert_polson', 52, 'PASSED'),  # UI-1
    ]
)
def test_create_run_success(login_in_as, title, suite_name, duration_seconds, status):
    page = login_in_as(title, suite_name, duration_seconds, status=status)
    page.wait_for_selector(f'#runs-list >> text={title}', timeout=5000)
    assert page.locator(f'#runs-list >> text={title}').is_visible()


@pytest.mark.parametrize(
    'title,suite_name,duration_seconds,status,invalid_field',
    [
        ('', 'robert_polson', 52, 'PASSED', 'title'),                       # UI-2
        ('ab', 'robert_polson', 52, 'PASSED', 'title'),                     # UI-3
        ('name_max', '', 52, 'PASSED', 'suite_name'),                       # UI-4
        ('name_max', 'robert_polson', 52, '', 'status'),                    # UI-5
        ('name_max', 'robert_polson', None, 'PASSED', 'duration_seconds'),  # UI-6
        ('name_max', 'robert_polson', 0, 'PASSED', 'duration_seconds'),     # UI-7
    ]
)
def test_form_validation_blocks_submit(login_in_as, title, suite_name, duration_seconds, status, invalid_field):
    page = login_in_as(title, suite_name, duration_seconds, status=status)
    valid = page.locator(f'[name="{invalid_field}"]').evaluate('el => el.validity.valid')
    assert valid is False