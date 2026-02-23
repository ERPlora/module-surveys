from django.utils.translation import gettext_lazy as _

MODULE_ID = 'surveys'
MODULE_NAME = _('Surveys')
MODULE_VERSION = '1.0.0'
MODULE_ICON = 'clipboard-outline'
MODULE_DESCRIPTION = _('Advanced surveys, questionnaires and response analytics')
MODULE_AUTHOR = 'ERPlora'
MODULE_CATEGORY = 'marketing'

MENU = {
    'label': _('Surveys'),
    'icon': 'clipboard-outline',
    'order': 62,
}

NAVIGATION = [
    {'label': _('Dashboard'), 'icon': 'speedometer-outline', 'id': 'dashboard'},
{'label': _('Surveys'), 'icon': 'clipboard-outline', 'id': 'surveys'},
{'label': _('Responses'), 'icon': 'chatbox-ellipses-outline', 'id': 'responses'},
{'label': _('Settings'), 'icon': 'settings-outline', 'id': 'settings'},
]

DEPENDENCIES = []

PERMISSIONS = [
    'surveys.view_survey',
'surveys.add_survey',
'surveys.change_survey',
'surveys.delete_survey',
'surveys.view_responses',
'surveys.manage_settings',
]
