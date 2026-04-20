from rest_framework import serializers
from studyproject.models import User


class UserSerializer(serializers.ModelSerializer):
    """用户序列化器"""
    class Meta:
        model = User
        fields = [
            "id", "phone", "nickName", "trueName", "email", "gender",
            "avatarUrl", "birthday", "is_h5", "is_app", "is_pc",
            "regtime", "last_time", "state", "is_distributor",
            "uniacid", "unionid", "is_user", "lid"
        ]
        read_only_fields = ["id", "regtime", "last_time"]


class UserRegisterSerializer(serializers.ModelSerializer):
    """用户注册序列化器"""
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ["phone", "password", "nickName", "email"]
        required_fields = ["phone", "password", "nickName"]
    
    def create(self, validated_data):
        user = User.objects.create_user(
            phone=validated_data["phone"],
            password=validated_data["password"],
            nickName=validated_data.get("nickName", ""),
            email=validated_data.get("email", "")
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    """用户登录序列化器"""
    phone = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)