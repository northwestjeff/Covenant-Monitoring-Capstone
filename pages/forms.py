from django.forms import ModelForm

from pages.models import Loan, Covenant

class NewLoanForm(ModelForm):
    class Meta:
        model = Loan
        fields = [
            "loan_id",
            "organization",
            "amount",
            "origination_date",
            "maturity_date",
            "payment_schedule",
            "regular_payment_amount"
        ]

class NewCovenantForm(ModelForm):
    class Meta:
        model = Covenant
        fields = [
            "cov_id",
            "indicator",
            "operator_options",
            "standard",
            "compliance",
            "loans"
        ]