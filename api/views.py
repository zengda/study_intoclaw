from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from studyproject.models import User
from .serializers import UserSerializer, UserRegisterSerializer, UserLoginSerializer


class RegisterView(APIView):
    """用户注册视图"""
    
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": "注册成功", "user": UserSerializer(user).data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """用户登录视图"""
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data["phone"]
            password = serializer.validated_data["password"]
            
            try:
                user = User.objects.get(phone=phone)
            except User.DoesNotExist:
                return Response(
                    {"error": "手机号或密码错误"},
                    status=status.HTTP_401_UNAUTHORIZED
                )
            
            if not user.check_password(password):
                return Response(
                    {"error": "手机号或密码错误"},
                    status=status.HTTP_401_UNAUTHORIZED
                )
            
            # 生成JWT令牌
            refresh = RefreshToken.for_user(user)
            
            # 设置Refresh Token到HttpOnly Cookie
            response = Response({
                "access": str(refresh.access_token),
                "user": UserSerializer(user).data
            })
            
            # 设置HttpOnly Cookie
            response.set_cookie(
                "refresh_token",
                str(refresh),
                max_age=7 * 24 * 60 * 60,  # 7天
                httponly=True,
                samesite="Lax",
                secure=False,  # 开发环境为False，生产环境为True
                path="/"
            )
            
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserInfoView(APIView):
    """获取用户信息视图"""
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class RefreshTokenView(APIView):
    """刷新Token视图"""
    
    def post(self, request):
        # 从Cookie中获取refresh token
        refresh_token = request.COOKIES.get("refresh_token")
        if not refresh_token:
            return Response(
                {"error": "缺少refresh token"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            refresh = RefreshToken(refresh_token)
            access_token = refresh.access_token
            return Response({
                "access": str(access_token)
            })
        except Exception as e:
            return Response(
                {"error": "无效的refresh token"},
                status=status.HTTP_401_UNAUTHORIZED
            )


class LogoutView(APIView):
    """用户登出视图"""
    
    def post(self, request):
        # 清除refresh token cookie
        response = Response({"message": "登出成功"})
        response.delete_cookie("refresh_token", path="/")
        return response