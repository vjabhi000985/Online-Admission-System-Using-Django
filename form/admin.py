from django.contrib import admin
from . models import appform

class appformAdmin(admin.ModelAdmin):
    fields = ('mark1','mark2','first_name','last_name','email','date_of_birth','aadhar_number','picture','courses','phone_no','father_name','mother_name','sign')
    list_display = [
        'picture',
        'first_name',
        'last_name',
        'date_of_birth',
        'aadhar_number',
        'father_name',
        'mother_name',
        'email',
        'courses',
        'yours_choice',
        'sign',
        'mark1',
        'mark2'
    ]

    readonly_fields = ['picture','sign']

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="100" />'.format(
            url = obj.picture.url,
            width=obj.picture.width,
            height=obj.picture.height,
            )
    )
    def sign_image(self, obj):
        return mark_safe('<img src="{url}" width="100" />'.format(
            url = obj.sign.url,
            width=obj.sign.width,
            height=obj.sign.height,
            )
    )
    def mark1_image(self, obj):
        return mark_safe('<img src="{url}" width="100" />'.format(
            url = obj.mark1.url,
            width=obj.mark1.width,
            height=obj.mark1.height,
            )
    )
    def mark2_image(self, obj):
        return mark_safe('<img src="{url}" width="100" />'.format(
            url = obj.mark2.url,
            width=obj.mark2.width,
            height=obj.mark2.height,
            )
    )

class payAdmin(admin.ModelAdmin):
    fields = ('name','card_no','expiry_month','expiry_year','cvv')
    list_display = [
        'name',
        'card_no',
        'expiry_month',
        'expiry_year',
        'cvv'
   ]

# Register your models here.
admin.site.register(appform,appformAdmin)
#admin.site.register(pay,payAdmin)
#admin.site.unregister(pay)