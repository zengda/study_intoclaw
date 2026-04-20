from django.urls import path
from .auth import RegisterView, LoginView, RefreshTokenView, LogoutView
from .users import UserMeView, ChangePasswordView
from .courses import CoursesView, CourseDetailView, CourseLessonsView, CourseReviewsView
from .learning import MyCoursesView, CourseProgressView, LessonProgressView
from .orders import OrdersView, OrderDetailView, OrderCancelView
from .payments import PaymentsView, PaymentDetailView, WechatCallbackView, AlipayCallbackView, RefundsView

urlpatterns = [
    # 认证相关
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/refresh/", RefreshTokenView.as_view(), name="refresh"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    
    # 用户相关
    path("users/me/", UserMeView.as_view(), name="user-me"),
    path("users/change-password/", ChangePasswordView.as_view(), name="change-password"),
    
    # 课程相关
    path("courses/", CoursesView.as_view(), name="courses"),
    path("courses/<slug:slug>/", CourseDetailView.as_view(), name="course-detail"),
    path("courses/<slug:slug>/lessons/", CourseLessonsView.as_view(), name="course-lessons"),
    path("courses/<slug:slug>/reviews/", CourseReviewsView.as_view(), name="course-reviews"),
    
    # 学习相关
    path("learning/my-courses/", MyCoursesView.as_view(), name="my-courses"),
    path("learning/courses/<int:course_id>/progress/", CourseProgressView.as_view(), name="course-progress"),
    path("learning/lessons/<int:lesson_id>/progress/", LessonProgressView.as_view(), name="lesson-progress"),
    
    # 订单相关
    path("orders/", OrdersView.as_view(), name="orders"),
    path("orders/<str:order_no>/", OrderDetailView.as_view(), name="order-detail"),
    path("orders/<str:order_no>/cancel/", OrderCancelView.as_view(), name="order-cancel"),
    
    # 支付相关
    path("payments/", PaymentsView.as_view(), name="payments"),
    path("payments/<str:payment_no>/", PaymentDetailView.as_view(), name="payment-detail"),
    path("payments/callback/wechat/", WechatCallbackView.as_view(), name="wechat-callback"),
    path("payments/callback/alipay/", AlipayCallbackView.as_view(), name="alipay-callback"),
    path("refunds/", RefundsView.as_view(), name="refunds"),
]