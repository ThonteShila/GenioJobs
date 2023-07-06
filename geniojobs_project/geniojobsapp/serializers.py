from rest_framework import serializers
from geniojobsapp.models import Job_Listing
#create ser
class Job_ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Job_Listing
        fields="__all__"
