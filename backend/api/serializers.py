from rest_framework import serializers
import api.models as models


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        lookup_field = 'uuid'
        fields = [
            'uuid',
            'organization',
            'created_by',
            'first_name',
            'last_name',
            'primary_contact_method',
            'rank'
        ]


class ContactRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactRank
        lookup_field = 'uuid'
        fields = [
            'uuid',
            'organization',
            'name',
            'description'
        ]


class ContactNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactNote
        lookup_field = 'uuid'
        fields = [
            'uuid',
            'contact',
            'created_by',
            'created',
            'body',
            'tags'
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        lookup_field = 'uuid'
        fields = [
            'uuid',
            'name'
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        lookup_field = 'uuid'
        fields = [
            'uuid',
            'first_name', 
            'last_name', 
            'email',
            'is_admin',
            'is_staff',
            'created',
            'updated',
        ]


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        lookup_field = 'uuid'
        fields = [
            'uuid',
            'user',
            'created',
            'body'
        ]


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        lookup_field = 'uuid'
        fields = [
            'uuid',
            'institution',
            'organization_name',
            'chapter_name',
            'users',
            'admin_users'
        ]


class MembershipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MembershipRequest
        lookup_field = 'uuid'
        fields = [
            'uuid',
            'organization',
            'user'
        ]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        lookup_field = 'uuid'
        fields = [
            'uuid',
            'organization',
            'assigner',
            'assignees',
            'title',
            'body',
            'due_date'
        ]


class OrganizationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrganizationImage
        lookup_field = 'uuid'
        fields = [
            'uuid',
            'organization',
            'created',
            'created_by',
            'image'
        ]
