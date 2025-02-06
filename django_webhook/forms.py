from django import forms

from django_webhook.models import Webhook, WebhookTopic


class WebhookForm(forms.ModelForm):
    class Meta:
        model = Webhook
        fields = "__all__"


class WebhookTopicForm(forms.ModelForm):
    class Meta:
        model = WebhookTopic
        fields = "__all__"
