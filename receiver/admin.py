from django.contrib import admin

from models import Member, Team, TeamMember

class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    extra = 1
    
class MemberAdmin(admin.ModelAdmin):
    inlines = (TeamMemberInline,)

class TeamAdmin(admin.ModelAdmin):
    inlines = (TeamMemberInline,)    

admin.site.register(Team, TeamAdmin)
admin.site.register(Member, MemberAdmin)
