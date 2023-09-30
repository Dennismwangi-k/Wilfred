from rest_framework import serializers
from .models import User, WasteCollector, WasteRecycler

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = "__all__"

class WasteCollectorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    def validate(self, attrs):
        password = attrs['password']
        confirm_password = attrs['confirm_password']
        if password == confirm_password:
            return attrs
        else:
            raise serializers.ValidationError(detail="Passwords do not match")
    
    class Meta:
        model = WasteCollector
        fields = ['id','username', 'first_name', 'last_name', 'email', 'phonenumber', 'location', 'password', 'confirm_password']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        user = User.objects.create(is_wastecollector=True, email=validated_data['email'], username=validated_data['username'], password=password)
        wastecollector = WasteCollector.objects.create(user=user, **validated_data)
        return wastecollector

class WasteRecyclerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    def validate(self, attrs):
        password = attrs['password']
        confirm_password = attrs['confirm_password']
        if password == confirm_password:
            return attrs
        else:
            raise serializers.ValidationError(detail="Passwords do not match")
    
    class Meta:
        model = WasteRecycler
        fields = ['id','username', 'first_name', 'last_name', 'email', 'phonenumber', 'password', 'confirm_password']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        user = User.objects.create(is_wasterecycler=True, email=validated_data['email'], username=validated_data['username'], password=password)
        wasterecycler = WasteRecycler.objects.create(user=user, **validated_data)
        return wasterecycler
