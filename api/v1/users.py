from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from studyproject.models import User
from ..serializers import UserSerializer


class UserMeView(APIView):
    """获取/更新当前用户信息"""
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        """获取当前用户信息"""
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request):
        """更新当前用户信息"""
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    """修改密码"""
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        
        if not old_password or not new_password:
            return Response(
                {"error": "缺少密码参数"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not user.check_password(old_password):
            return Response(
                {"error": "原密码错误"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        user.set_password(new_password)
        user.save()
        
        return Response({"message": "密码修改成功"})