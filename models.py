from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.base import HubBaseModel

class Survey(HubBaseModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))
    start_date = models.DateField(null=True, blank=True, verbose_name=_('Start Date'))
    end_date = models.DateField(null=True, blank=True, verbose_name=_('End Date'))
    response_count = models.PositiveIntegerField(default=0, verbose_name=_('Response Count'))

    class Meta(HubBaseModel.Meta):
        db_table = 'surveys_survey'

    def __str__(self):
        return self.title


class SurveyQuestion(HubBaseModel):
    survey = models.ForeignKey('Survey', on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500, verbose_name=_('Text'))
    question_type = models.CharField(max_length=20, default='text', verbose_name=_('Question Type'))
    is_required = models.BooleanField(default=True, verbose_name=_('Is Required'))
    order = models.PositiveIntegerField(default=0, verbose_name=_('Order'))

    class Meta(HubBaseModel.Meta):
        db_table = 'surveys_surveyquestion'

    def __str__(self):
        return str(self.id)

