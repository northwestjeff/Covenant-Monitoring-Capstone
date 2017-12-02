from django.db import models
from django import forms
from django.contrib.auth.models import User
from localflavor.us.models import USStateField
from djmoney.models.fields import MoneyField
from django.utils.text import slugify
from django.db.models.signals import pre_save

payment_schedule_options = (
    ('Weekly', 'weekly'),
    ('Monthly', 'monthly'),
    ('Quarterly', 'quarterly'),
    ('Semi-annually', 'semi-annually'),
    ('Annually', 'annually')
)


class Loan(models.Model):
    loan_id = models.CharField(max_length=15, blank=True, null=True)
    organization = models.ForeignKey('Organization', related_name='loans', blank=True, null=True)
    amount = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    origination_date = models.DateField()
    maturity_date = models.DateField()
    payment_schedule = models.CharField(max_length=25, choices=payment_schedule_options)
    regular_payment_amount = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    loan_compliance = models.BooleanField(default=True)  # If all covenants are true
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)


    # portfolio = models.ForeignKey('Portfolio', related_name='loans')
    # noncomp_portfolio = models.ForeignKey('NoncompliantPortfolio', related_name='loans')

    def _get_unique_slug(self):
        passed_slug = "{} {}".format(self.loan_id, self.organization.business_name)
        slug = slugify(passed_slug)
        unique_slug = slug
        num = 1
        while Organization.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    def __str__(self):
        return self.cov_id

    def __str__(self):
        return "{}.{}.{}".format(self.loan_id, self.organization, self.amount)


indicator_options = (
    ('Total Liabilities', 'Total Liabilities'),
    ('Current Ratio', 'Current Ratio'),
)

operator_options = (
    ('Greater Than', '>'),
    ('Less Than', '<'),
    ('Equal to', '='),
    ('NOT Equal to', '≠'),
)


class Covenant(models.Model):
    cov_id = models.CharField(max_length=15)
    indicator = models.CharField(max_length=50, choices=indicator_options)
    operator_options = models.CharField(max_length=15, choices=operator_options)
    standard = models.IntegerField(default=0)
    compliance = models.BooleanField(default=True)
    date_last_compliant = models.DateField(blank=True, null=True)
    num_times_noncomp = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    loans = models.ForeignKey(Loan, related_name='covenants')
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    comparison = models.CharField(max_length=100, blank=True, null=True)


    def _get_unique_slug(self):
        slug = slugify(self.cov_id, self.indicator)
        unique_slug = slug
        num = 1
        while Organization.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    def make_slug(self):
        self.slug = slugify(self.cov_id, self.indicator)

    def __str__(self):
        return self.cov_id


class ClientUser(models.Model):
    username = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.username


class Organization(models.Model):
    business_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = USStateField(null=True, blank=True)
    zip = models.CharField(max_length=5, blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

    def _get_unique_slug(self):
        slug = slugify(self.business_name)
        unique_slug = slug
        num = 1
        while Organization.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    def __str__(self):
        return self.business_name


# class Borrower(models.Model):
#     # Need to inherit from Organization class
#     compliance = models.BooleanField(default=True)  # If all loans compliance === true


# class NoncompliantPortfolio(models.Model):
#     total_origination = models.FloatField(default=0)
#
#     def add_function(self):
#         self.total_origination = 0
#         loans = self.loans.all()
#         for i in loans:
#             self.total_origination += i.amount
#
#     def __str__(self):
#         return self.loans, self.total_origination


# class Portfolio(models.Model):
#     total_origination = models.FloatField(default=0)
#
#     def add_function(self):
#         self.total_origination = 0
#         loans = self.loans.all()
#         for i in loans:
#             self.total_origination += i.amount
#
#     def __str__(self):
#         return self.loans  # , self.total_origination

class Statement(models.Model):
    time = models.DateTimeField()
    name = models.CharField(max_length=255)
    start_period = models.DateField()
    end_period = models.DateField()
    summarize_by = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, related_name='statements', blank=True, null=True)

    def __str__(self):
        return str(self.end_period)

    class Meta:
        ordering = ['end_period']


class Data(models.Model):
    statement = models.ForeignKey("Statement", related_name="data")
    column_headers = models.CharField(max_length=100)
    value = models.CharField(max_length=25)

    def __str__(self):
        return "{}: {} - {}".format(self.column_headers, self.value, self.statement.name)


