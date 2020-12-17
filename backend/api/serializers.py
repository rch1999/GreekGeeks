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


class ContactMethodAdditionSerializer(serializers.Serializer):
    contact_uuid = serializers.UUIDField(required=False)
    medium = serializers.CharField()
    value = serializers.CharField()


class ContactAdditionSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    primary_contact_method = ContactMethodAdditionSerializer(required=False)
    rank_uuid = serializers.UUIDField(required=False)
    organization_uuid = serializers.UUIDField()


class ContactUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    primary_contact_method_uuid = serializers.UUIDField(required=False)
    rank_uuid = serializers.UUIDField(required=False)


class ContactNoteAdditionSerializer(serializers.Serializer):
    body = serializers.CharField()
    tags = serializers.ListSerializer(child=serializers.CharField())


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


class EmailVerificationSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()


class UserAdditionSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()


class UserUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    password = serializers.CharField(required=False)


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        lookup_field = 'uuid'
        fields = [
            'uuid',
            'first_name',
            'last_name',
            'email'
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


class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactRank
        lookup_field = 'uuid'
        fields = [
            'uuid',
            'organization',
            'name',
            'description'
        ]


class RankUpdateSerializer(serializers.Serializer):
    description = serializers.CharField()


class RankAdditionSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()


class MembershipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MembershipRequest
        lookup_field = 'uuid'
        fields = [
            'uuid',
            'organization',
            'user'
        ]


class MembershipRequestAdditionSerializer(serializers.Serializer):
    user_uuid = serializers.UUIDField()


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
