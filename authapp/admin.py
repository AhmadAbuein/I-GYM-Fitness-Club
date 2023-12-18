from django.contrib import admin
from .models import Contact,Enrollment,MembershipPlan,Trainer,Gallery,Attendance,GymLocation, GymInstructor

# Register your models here.

admin.site.register(Contact)
admin.site.register(Enrollment)
admin.site.register(MembershipPlan)
admin.site.register(Trainer)
admin.site.register(Gallery)
admin.site.register(Attendance)
admin.site.register(GymLocation)
admin.site.register(GymInstructor)