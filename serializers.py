from rest_framework import serializers

from.models import *

class RegisterSerializer(serializers.ModelSerializer):
    
    # Img = serializers.ImageField(
    #     max_length=None, use_url=True,
    # )
    class Meta:
        model = Register
        fields=('id','Name','Mobile','Email','District','Pincode','State','Gender','Image')