from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class PaymentsView(APIView):
    """支付管理"""
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        """创建支付"""
        # 这里应该处理支付创建，暂时返回成功
        return Response({"payment_no": "PAY20260420001", "message": "支付创建成功"}, status=status.HTTP_201_CREATED)


class PaymentDetailView(APIView):
    """支付详情"""
    permission_classes = [IsAuthenticated]
    
    def get(self, request, payment_no):
        """获取支付详情"""
        # 这里应该根据 payment_no 获取支付详情，暂时返回示例数据
        payment = {
            "payment_no": payment_no,
            "amount": 99.00,
            "status": "待支付",
            "created_at": "2026-04-20T10:00:00Z",
            "order_no": "ORD20260420001"
        }
        return Response(payment)


class WechatCallbackView(APIView):
    """微信支付回调"""
    
    def post(self, request):
        """处理微信支付回调"""
        # 这里应该处理微信支付回调，暂时返回成功
        return Response({"code": "SUCCESS", "message": "回调处理成功"})


class AlipayCallbackView(APIView):
    """支付宝支付回调"""
    
    def post(self, request):
        """处理支付宝支付回调"""
        # 这里应该处理支付宝支付回调，暂时返回成功
        return Response({"code": "SUCCESS", "message": "回调处理成功"})


class RefundsView(APIView):
    """退款管理"""
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        """创建退款"""
        # 这里应该处理退款创建，暂时返回成功
        return Response({"refund_no": "REF20260420001", "message": "退款申请成功"}, status=status.HTTP_201_CREATED)