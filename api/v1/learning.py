from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class MyCoursesView(APIView):
    """我的课程列表"""
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        """获取我的课程列表"""
        # 这里应该返回当前用户的课程列表，暂时返回示例数据
        courses = [
            {
                "id": 1,
                "title": "Python 基础课程",
                "progress": 30,
                "last_learned": "2026-04-20T10:00:00Z"
            },
            {
                "id": 2,
                "title": "Django 高级课程",
                "progress": 10,
                "last_learned": "2026-04-19T15:00:00Z"
            }
        ]
        return Response(courses)


class CourseProgressView(APIView):
    """课程学习进度"""
    permission_classes = [IsAuthenticated]
    
    def get(self, request, course_id):
        """获取课程学习进度"""
        # 这里应该根据 course_id 获取学习进度，暂时返回示例数据
        progress = {
            "course_id": course_id,
            "total_lessons": 10,
            "completed_lessons": 3,
            "progress_percentage": 30,
            "last_lesson": "第三章：Python 函数"
        }
        return Response(progress)


class LessonProgressView(APIView):
    """章节学习进度"""
    permission_classes = [IsAuthenticated]
    
    def post(self, request, lesson_id):
        """提交章节学习进度"""
        # 这里应该处理章节学习进度提交，暂时返回成功
        return Response({"message": "进度提交成功"})