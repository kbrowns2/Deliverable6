
class SubscriberForm:
    class Meta:
        model = subscriberForm
        fields = ["SubscriberID", "ServiceCode", "SubscriptionRequest", "SubscriptionStart, "SubscriptionEnd", "MotifOfCancellation", "SubscriptionType", "UserName",
                  "BeneficiaryID", "SpecialNtoes",]

        labels = {
            "SubscriberID": 'Subscriber ID',
            "ServiceCode": 'Service Code',
            "SubscriptionRequest": 'Subscription Request',
            "SubscriptionStart": 'Subscription Start',
            "SubscriptionEnd": 'Subscription End',
            "MotifOfCancellation": 'Motif Of Cancellation',
            "SubscriptionType": 'Subscription Type',
            "BeneficiaryID": 'Beneficiary ID',
            "SpecialNotes": 'Zip Code'

        }
        widgets = {
            'SubscriberID': forms.TextInput(attrs={'placeholder': 'Subscriber ID - Required'}),
            'ServiceCode': forms.TextInput(attrs={'placeholder': 'Service Code - Required'}),
            'SubscriptionRequest': forms.TextInput(attrs={'placeholder': 'Subscription Request'}),
            'SubscriptionStart': forms.TextInput(attrs={'placeholder': 'Subscription Start - Required'}),
            'SubscriptionEnd': forms.TextInput(attrs={'placeholder': 'Subscription Start - Required'}),
            'MotifOfCancellation': forms.TextInput(attrs={'placeholder': 'Subscription End - Required'}),
            'SubscriptionType': forms.TextInput(attrs={'placeholder': 'Motif Of Cancellation - Required'}),
            'BeneficiaryID': forms.TextInput(attrs={'placeholder': 'Beneficiary ID - Required'}),
            'SpecialNotes': forms.TextInput(attrs={'placeholder': 'Speical Notes'}),