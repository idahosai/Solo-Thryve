from django.db import models

# Create your models here.

class CareerCounselorForm(models.Model):
    q1c_sso = models.BooleanField(default=False)
    q1c_friend = models.BooleanField(default=False)
    q1c_faculty = models.BooleanField(default=False)
    q1c_visit = models.BooleanField(default=False)
    q1c_orient = models.BooleanField(default=False)
    q1c_event = models.BooleanField(default=False)
    q1c_kpi = models.BooleanField(default=False)
    q1c_outreach = models.BooleanField(default=False)
    q1c_posters = models.BooleanField(default=False)
    q1c_stv = models.BooleanField(default=False)
    q1c_social = models.BooleanField(default=False)
    q1c_media = models.BooleanField(default=False)
    q1c_walkby = models.BooleanField(default=False)
    q1c_website = models.BooleanField(default=False)
    ccs_exploration = models.BooleanField(default=False)
    ccs_eplanning = models.BooleanField(default=False)
    ccs_cplanning = models.BooleanField(default=False)
    ccs_labourmarket = models.BooleanField(default=False)
    ccs_other = models.BooleanField(default=False)

    def __str__(self):
        return self.title