from .models import Candidate
from rest_framework import serializers

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        return Candidate.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        return value

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Age must be at least 18.")
        return value

    def validate_gender(self, value):
        if value not in ['M', 'F']:
            raise serializers.ValidationError("Gender must be 'M' or 'F'.")
        return value

    def validate_email(self, value):
        if '@' not in value:
            raise serializers.ValidationError("Email must be valid.")
        return value

    def validate_phone_number(self, value):
        if len(value) != 10:
            raise serializers.ValidationError("Phone number must be 10 digits.")
        return value

    def validate(self, data):
        if 'name' not in data:
            raise serializers.ValidationError("Name is required.")
        if 'age' not in data:
            raise serializers.ValidationError("Age is required.")
        if 'gender' not in data:
            raise serializers.ValidationError("Gender is required.")
        if 'email' not in data:
            raise serializers.ValidationError("Email is required.")
        if 'phone_number' not in data:
            raise serializers.ValidationError("Phone number is required.")
        return data

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'age': instance.age,
            'gender': instance.gender,
            'email': instance.email,
            'phone_number': instance.phone_number,
            'created_at': instance.created_at,
            'updated_at': instance.updated_at,
        }

    def to_internal_value(self, data):
        return {
            'name': data.get('name'),
            'age': data.get('age'),
            'gender': data.get('gender'),
            'email': data.get('email'),
            'phone_number': data.get('phone_number'),
        }

    def to_internal_value(self, data):
        return {
            'name': data.get('name'),
            'age': data.get('age'),
            'gender': data.get('gender'),
            'email': data.get('email'),
            'phone_number': data.get('phone_number'),
        }
