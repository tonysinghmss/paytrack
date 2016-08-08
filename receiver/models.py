from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
#One-to-Many
#
#Many-to-Many
# Member and Team through TeamMember
        
class Member(models.Model):    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                                 message="Phone number must be entered in the format: '+9999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex],blank=True,max_length=15)
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name + ' having phone number ending with '+ self.phone[-4:]
    
class Team(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    members = models.ManyToManyField(Member, through='TeamMember')
    
    def __unicode__(self):
        return self.name

class MemberManager(models.Manager):
    #Custom manager for TeamMember model
    use_for_related_fields = True
    
    def add_member(self, member, team):                
        self.create(member=member, team=team)
    
    def remove_member(self, member, team):
        tu_entry = self.get(member=member, team=team)
        tu_entry.delete()
    
    def transfer_member(self, member, team):
        prv_teams = member.team_set.all()
        for prv_team in prv_teams:
            self.remove_member(member, prv_team)
        self.add_member(member, team)


class TeamMember(models.Model):
    # Model for mapping Member and Team models
    team = models.ForeignKey(Team)
    member = models.ForeignKey(Member)
    objects = MemberManager()
    
    def __unicode__(self):
        return 'Team: '+self.team.name +' User: '+self.member.name
    
class MemberPaymentDetails(models.Model):
    # Model to store payment details of Member
    has_payed = models.BooleanField()
    pay_dt = models.DateTimeField('payment date')
    member = models.ForeignKey(Member)
    
    def __unicode__(self):
        return 'Member Name: '+self.member.name + ' Payment status: '+str(self.has_payed)

