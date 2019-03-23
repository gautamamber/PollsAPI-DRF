from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Poll(models.Model):
	question = models.CharField(max_length = 100)
	created_by = models.ForeignKey(User, on_delete = models.CASCADE)
	pub_date = models.DateTimeField(auto_now = True)

	def __str__(self):
		return str(self.question)

	class Meta:
		verbose_name = "Poll"
		verbose_name_plural = "Poll"



class Choice(models.Model):
	poll = models.ForeignKey(Poll, related_name = 'choices', on_delete = models.CASCADE)
	choice_text = models.CharField(max_length = 100)

	def __str__(self):
		return str(self.choice_text)

	class Meta:
		verbose_name = "Choice"
		verbose_name_plural = "Choice"

class Vote(models.Model):
	choice = models.ForeignKey(Choice, on_delete = models.CASCADE, related_name = 'votes')
	poll = models.ForeignKey(Poll, on_delete = models.CASCADE)
	voted_by = models.ForeignKey(User , on_delete = models.CASCADE)

	class Meta:
		verbose_name = "Vote"
		verbose_name_plural = "Vote"
		unique_together = ("poll", "voted_by")

