from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class CoursesView(APIView):
    """课程列表"""
    
    def get(self, request):
        """获取课程列表"""
        # 这里应该返回课程列表，暂时返回示例数据
        courses = [
            {
                "id": 1,
                "title": "Python 基础课程",
                "slug": "python-basic",
                "description": "Python 基础入门课程",
                "price": 99.00,
                "cover": "https://example.com/cover1.jpg"
            },
            {
                "id": 2,
                "title": "Django 高级课程",
                "slug": "django-advanced",
                "description": "Django 高级开发课程",
                "price": 199.00,
                "cover": "https://example.com/cover2.jpg"
            }
        ]
        return Response(courses)


class CourseDetailView(APIView):
    """课程详情"""
    
    def get(self, request, slug):
        """获取课程详情"""
        # 这里应该根据 slug 获取课程详情，暂时返回示例数据
        course = {
            "id": 1,
            "title": "Python 基础课程",
            "slug": slug,
            "description": "Python 基础入门课程",
            "price": 99.00,
            "cover": "https://example.com/cover1.jpg",
            "instructor": "张老师",
            "duration": "10 小时",
            "level": "初级"
        }
        return Response(course)


class CourseLessonsView(APIView):
    """课程章节列表"""
    
    def get(self, request, slug):
        """获取课程章节列表"""
        # 这里应该根据 slug 获取课程章节，暂时返回示例数据
        lessons = [
            {
                "id": 1,
                "title": "第一章：Python 简介",
                "duration": "45 分钟",
                "order": 1
            },
            {
                "id": 2,
                "title": "第二章：Python 基础语法",
                "duration": "60 分钟",
                "order": 2
            }
        ]
        return Response(lessons)


class CourseReviewsView(APIView):
    """课程评价"""
    permission_classes = [IsAuthenticated]
    
    def post(self, request, slug):
        """提交课程评价"""
        # 这里应该处理课程评价提交，暂时返回成功
        return Response({"message": "评价提交成功"}, status=status.HTTP_201_CREATED)
    
    def get(self, request, slug):
        """获取课程评价列表"""
        # 这里应该返回课程评价列表，暂时返回示例数据
        reviews = [
            {
                "id": 1,
                "user": "用户1",
                "rating": 5,
                "comment": "课程非常好！",
                "created_at": "2026-04-20T10:00:00Z"
            }
        ]
        return Response(reviews)