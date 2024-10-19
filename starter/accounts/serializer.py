from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    #snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())
    
    class Meta:
        model = Account
        fields = '__all__'
        # lookup_field = 'username'
