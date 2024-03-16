"""
Module containing Django models for the resume app.

Classes:
    Contact
    Experience_pro
    Technical_skill
    Education
    Personal_skill
    Interest
    Language

"""

from django.db import models
from developer.models import Developer


class Contact(models.Model):
    """
    A class to represent a type of contact with developer.

    Attributes:
        type_of_contact (CharField): The type of contact.
        description (TextField): The contact description or link.
        developer (ForeignKey): The id of associated developer.

    Methods:
        __str__(): Returns a string representation of the contact.
    """

    type_of_contact = models.CharField(max_length=100)
    description = models.TextField()
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.developer.first_name} {self.developer.last_name}: {self.type_of_contact}')


class Experience_pro(models.Model):
    """
    A class to represent work experience of developer.

    Attributes:
        company_name (CharField): Name of company where developer works or worked.
        position (CharField): Position of the developer.
        start_year (DateField): When the developer started to work.
        end_year (DateField): When the developer ended to work. Leave blank if still working there.
        description (TextField): The work description.
        developer (ForeignKey): The id of associated developer.

    Methods:
        __str__(): Returns a string representation of the working experience.
    """

    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_year = models.DateField()
    end_year = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

    def __str__(self):
        if self.end_year:
            return (
                f'{self.developer.first_name} {self.developer.last_name}: '
                f'{self.company_name} - {self.position} ({self.start_year} - {self.end_year})'
                    )
        else:
            return (
                f'{self.developer.first_name} {self.developer.last_name}: '
                f'{self.company_name} - {self.position} ({self.start_year} - today)'
                    )


class Technical_skill(models.Model):
    """
    A class to represent a technical skill of developer.

    Attributes:
        name (CharField): Name of group of skills.
        description (TextField): The skills description.
        developer (ForeignKey): The id of associated developer.

    Methods:
        __str__(): Returns a string representation of the technical skill.
    """

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.developer.first_name} {self.developer.last_name}: {self.name}')


class Education(models.Model):
    """
    A class to represent education of developer.

    Attributes:
        university_name (CharField): Name of university where developer studied or studies.
        diploma_name (CharField): Name of diploma.
        start_year (DateField): When the developer started to study.
        end_year (DateField): When the developer ended to study. Leave blank if still studying there.
        description (TextField): The studies description.
        developer (ForeignKey): The id of associated developer.

    Methods:
        __str__(): Returns a string representation of education.
    """

    university_name = models.CharField(max_length=100)
    diploma_name = models.CharField(max_length=100)
    start_year = models.DateField()
    end_year = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

    def __str__(self):
        if self.end_year:
            return (
                f'{self.developer.first_name} {self.developer.last_name}: '
                f'{self.university_name} - {self.diploma_name} ({self.start_year} - {self.end_year})'
                    )
        else:
            return (
                f'{self.developer.first_name} {self.developer.last_name}: '
                f'{self.university_name} - {self.diploma_name} ({self.start_year} - today)'
                    )


class Personal_skill(models.Model):
    """
    A class to represent a personal skill of developer.

    Attributes:
        name (CharField): Name of skill.
        developer (ForeignKey): The id of associated developer.

    Methods:
        __str__(): Returns a string representation of personal skill.
    """

    name = models.CharField(max_length=100)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.developer.first_name} {self.developer.last_name}: {self.name}')


class Interest(models.Model):
    """
    A class to represent an interest of developer.

    Attributes:
        name (CharField): Name of interest.
        developer (ForeignKey): The id of associated developer.

    Methods:
        __str__(): Returns a string representation of interests.
    """

    name = models.CharField(max_length=100)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.developer.first_name} {self.developer.last_name}: {self.name}')


class Language(models.Model):
    """
    A class to represent an language of developer.

    Attributes:
        name (CharField): Language.
        level(CharField): Language level choices.
        developer (ForeignKey): The id of associated developer.

    Methods:
        __str__(): Returns a string representation of language.
    """

    LEVEL_CHOICES = [
        ('begginer', 'Begginer'),
        ('intermediate', 'Intermediate'),
        ('bilingual', 'Bilingual'),
    ]

    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.developer.first_name} {self.developer.last_name}: {self.name} ({self.level})')
