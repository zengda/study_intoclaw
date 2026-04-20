from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class OrdersView(APIView):
    """订单管理"""
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        """创建订单"""
        # 这里应该处理订单创建，暂时返回成功
        return Response({"order_no": "ORD20260420001", "message": "订单创建成功"}, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        """获取订单列表"""
        # 这里应该返回订单列表，暂时返回示例数据
        orders = [
            {
                "order_no": "ORD20260420001",
                "amount": 99.00,
                "status": "待支付",
                "created_at": "2026-04-20T10:00:00Z"
            },
            {
                "order_no": "ORD20260419001",
                "amount": 199.00,
                "status": "已支付",
                "created_at": "2026-04-19T15:00:00Z"
            }
        ]
        return Response(orders)


class OrderDetailView(APIView):
    """订单详情"""
    permission_classes = [IsAuthenticated]
    
    def get(self, request, order_no):
        """获取订单详情"""
        # 这里应该根据 order_no 获取订单详情，暂时返回示例数据
        order = {
            "order_no": order_no,
            "amount": 99.00,
            "status": "待支付",
            "created_at": "2026-04-20T10:00:00Z",
            "items": [
                {
                    "course_id": 1,
                    "title": "Python 基础课程",
                    "price": 99.00
                }
            ]
        }
        return Response(order)


class OrderCancelView(APIView):
    """取消订单"""
    permission_classes = [IsAuthenticated]
    
    def post(self, request, order_no):
        """取消订单"""
        # 这里应该处理订单取消，暂时返回成功
        return Response({"message": "订单取消成功"})