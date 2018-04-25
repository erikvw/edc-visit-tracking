from dateutil.relativedelta import relativedelta
from edc_visit_schedule import VisitSchedule, Schedule, Visit, Panel
from edc_visit_schedule import FormsCollection, Crf, Requisition


crfs = FormsCollection(
    Crf(show_order=1, model='edc_metadata.crfone', required=True),
    Crf(show_order=2, model='edc_metadata.crftwo', required=True),
    Crf(show_order=3, model='edc_metadata.crfthree', required=True),
    Crf(show_order=4, model='edc_metadata.crffour', required=True),
    Crf(show_order=5, model='edc_metadata.crffive', required=True),
)

requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=Panel('one', requisition_model='edc_metadata.subjectrequisition'),
        required=True, additional=False),
    Requisition(
        show_order=20,
        panel=Panel('two', requisition_model='edc_metadata.subjectrequisition'),
        required=True, additional=False),
    Requisition(
        show_order=30,
        panel=Panel(
            'three', requisition_model='edc_metadata.subjectrequisition'),
        required=True, additional=False),
    Requisition(
        show_order=40,
        panel=Panel(
            'four', requisition_model='edc_metadata.subjectrequisition'),
        required=True, additional=False),
    Requisition(
        show_order=50,
        panel=Panel(
            'five', requisition_model='edc_metadata.subjectrequisition'),
        required=True, additional=False),
    Requisition(
        show_order=60,
        panel=Panel('six', requisition_model='edc_metadata.subjectrequisition'),
        required=True, additional=False),
)

visit_schedule1 = VisitSchedule(
    name='visit_schedule1',
    offstudy_model='edc_visit_tracking.subjectoffstudy',
    death_report_model='edc_visit_tracking.deathreport')

visit_schedule2 = VisitSchedule(
    name='visit_schedule2',
    offstudy_model='edc_visit_tracking.subjectoffstudy',
    death_report_model='edc_visit_tracking.deathreport')

schedule1 = Schedule(
    name='schedule1',
    onschedule_model='edc_visit_tracking.onscheduleone',
    offschedule_model='edc_visit_tracking.offscheduleone',
    consent_model='edc_visit_tracking.subjectconsent',
    appointment_model='edc_appointment.appointment')

schedule2 = Schedule(
    name='schedule2',
    onschedule_model='edc_visit_tracking.onscheduletwo',
    offschedule_model='edc_visit_tracking.offscheduletwo',
    consent_model='edc_visit_tracking.subjectconsent',
    appointment_model='edc_appointment.appointment')


visits = []
for index in range(0, 4):
    visits.append(
        Visit(
            code=f'{index + 1}000',
            title=f'Day {index + 1}',
            timepoint=index,
            rbase=relativedelta(days=index),
            rlower=relativedelta(days=0),
            rupper=relativedelta(days=6),
            requisitions=requisitions,
            crfs=crfs,
            facility_name='default'))
for visit in visits:
    schedule1.add_visit(visit)

visits = []
for index in range(4, 8):
    visits.append(
        Visit(
            code=f'{index + 1}000',
            title=f'Day {index + 1}',
            timepoint=index,
            rbase=relativedelta(days=index),
            rlower=relativedelta(days=0),
            rupper=relativedelta(days=6),
            requisitions=requisitions,
            crfs=crfs,
            facility_name='default'))
for visit in visits:
    schedule2.add_visit(visit)

visit_schedule1.add_schedule(schedule1)
visit_schedule2.add_schedule(schedule2)
