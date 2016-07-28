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
    member_phone = models.CharField(validators=[phone_regex],blank=True)
    member_name = models.CharField(max_length=50)
    
class Team(models.Model):
    team_name = models.CharField(max_length=50)
    members = models.ManyToManyField(User, through='Member')
    
    def __unicode__(self):
        return self.team_name

class MemberManager(models.Manager):
    use_for_related_fields = True
    
    def add_member(self, user, team):
        pass
    
    def remove_member(self, user, team):
        pass
    
    def transfer_member(self, user, team):
        pass


class Member(models.Model):
    team = models.ForeignKey(Team)
    user = models.ForeignKey(User)
    objects = MemberManager()
    
    
    
   