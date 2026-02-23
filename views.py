"""
Surveys Module Views
"""
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.modules_runtime.navigation import with_module_nav


@login_required
@with_module_nav('surveys', 'dashboard')
@htmx_view('surveys/pages/dashboard.html', 'surveys/partials/dashboard_content.html')
def dashboard(request):
    """Dashboard view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('surveys', 'surveys')
@htmx_view('surveys/pages/surveys.html', 'surveys/partials/surveys_content.html')
def surveys(request):
    """Surveys view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('surveys', 'responses')
@htmx_view('surveys/pages/responses.html', 'surveys/partials/responses_content.html')
def responses(request):
    """Responses view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('surveys', 'settings')
@htmx_view('surveys/pages/settings.html', 'surveys/partials/settings_content.html')
def settings(request):
    """Settings view."""
    hub_id = request.session.get('hub_id')
    return {}

