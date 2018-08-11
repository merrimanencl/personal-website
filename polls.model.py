from django.db import models

# Create your models here.
#Strength is for the strength of the drug (i.e. 50mcg)
class Strength(models.Model):
    strength = models.CharField(max_length=20, default=None)
    def __str__(self):
        return self.strength

#Drug_Format is for the format that the drug is available in (i.e. tablet)
class Drug_Format(models.Model):
    drug_format = models.CharField(max_length=20, default=None)
    def __str__(self):
        return self.drug_format

#Drug_length is for the amount of time the drug is prescribed (i.e. 30 days)
class Drug_Length (models.Model):
    drug_length = models.CharField(max_length=20, default=None)

    def __str__(self):
        return self.drug_length

#Dose is for the number of times the drug should be taken (i.e. once a day, twice a day)
class Dose (models.Model):
	dose = models.CharField(max_length=140, default=None)
	#dose_strength = models.ManyToManyField(Strength, through='Drug', through_fields=('dose', 'strength'),)
	#dose_drug_format = models.ManyToManyField (Drug_Format, through= 'Drug', through_fields=('dose', 'drug_format'),)
	#dose_drug_length = models.ManyToManyField (Drug_Length, through='Drug', through_fields=('dose', 'drug_length'),)

#Flagging a syntax error
    def __str__(self):
        return self.dose

#Drug is for the name of the drug iteself, which can come in many strengths, formats, length of prescription and doses
class Drug (models.Model):
	name = models.CharField(max_length=50, default=None)
	dose = models.ForeignKey(Dose, on_delete=models.CASCADE)
	strength = models.ForeignKey(Strength, on_delete=models.CASCADE)
	drug_format = models.ForeignKey(Drug_Format, on_delete=models.CASCADE)
	drug_length = models.ForeignKey(Drug_Length, on_delete=models.CASCADE)

def __str__(self):
        return self.name




