from rest_framework import views, permissions, status
from rest_framework.response import Response


from .tasks import create_fibonacci
from .models import FibonacciHistory


class FibonacciApiView(views.APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        n = request.data["n"]

        try:
            instance = FibonacciHistory.objects.get(index=n)
            # serializer = FiboniacciSerializer(instance=instance)

            return Response(
                {
                    "status": "success",
                    "nth": instance.fibonacci_number
                }, 
                status=status.HTTP_200_OK
            )
        except FibonacciHistory.DoesNotExist:
            create_fibonacci.delay(n)

        return Response({"status": "pending"}, status=status.HTTP_200_OK)
