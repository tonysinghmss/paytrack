from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
#One-to-Many
#
#Many-to-Many
# User and Team through Member
        
class User(models.Model):    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                                 message="Phone number must be entered in the format: '+9999999999'. Up to 15 digits allowed.")
    member_phone = models.CharField(validators=[phone_regex],blank=True,max_length=15)
    member_name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.member_name + ' having phone number ending with '+ self.member_phone[-4:]
    
class Team(models.Model):
    team_name = models.CharField(max_length=50)
    team_members = models.ManyToManyField(User, through='TeamMember')
    
    def __unicode__(self):
        return self.team_name

class MemberManager(models.Manager):
    use_for_related_fields = True
    
    def add_member(self, user, team):
        team.team_members.add(user)
    
    def remove_member(self, user, team):
        team.team_members.remove(user)
    
    def transfer_member(self, user,team):
        prv_teams = user.team_set.all()
        for prv_team in prv_teams:
            self.remove_member(user, prv_team)
        self.add_member(user, team)


class TeamMember(models.Model):
    team = models.ForeignKey(Team)
    user = models.ForeignKey(User)
    objects = MemberManager()
    
    
    
   
