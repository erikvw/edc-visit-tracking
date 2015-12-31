from django.db import models
from django.utils import timezone

from edc_base.model.validators import datetime_not_before_study_start, datetime_not_future

from .crf_model_manager import CrfModelManager
from django.core.urlresolvers import reverse


class CrfModelMixin(models.Model):

    visit_model = None

    visit_model_attr = None

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future, ],
        default=timezone.now,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

    objects = CrfModelManager()

    def get_subject_identifier(self):
        return self.get_visit().appointment.registered_subject.subject_identifier

    def get_report_datetime(self):
        return self.report_datetime

    def get_visit(self):
        return getattr(self, self.visit_model_attr)

    def dashboard(self):
        url = reverse(
            'subject_dashboard_url',
            kwargs={'dashboard_type': self.get_visit().appointment.registered_subject.subject_type.lower(),
                    'dashboard_model': 'appointment',
                    'dashboard_id': self.get_visit().appointment.pk,
                    'show': 'appointments'})
        return """<a href="{url}" />dashboard</a>""".format(url=url)
    dashboard.allow_tags = True

    class Meta:
        abstract = True
