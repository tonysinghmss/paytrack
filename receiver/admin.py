from django.contrib import admin

from models import Member, Team, TeamMember, MemberPaymentDetails

class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    extra = 1
    
class MemberPaymentInline(admin.TabularInline):
    model = MemberPaymentDetails
    extra = 0    
    
class MemberAdmin(admin.ModelAdmin):
    inlines = (TeamMemberInline, MemberPaymentInline,)

class TeamAdmin(admin.ModelAdmin):
    inlines = (TeamMemberInline,)

admin.site.register(Team, TeamAdmin)
admin.site.register(Member, MemberAdmin)

