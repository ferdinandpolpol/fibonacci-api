from rest_framework import views

from .tasks import create_fibonacci


class FibonacciApiView(views.ApiView):

    def post(self, request, *args, **kwargs):
        n = request.data["n"]

        try:
            instance = FibonacciHistory.objects.get(index=n)
            serializer = FiboniacciSerializer(instance=instance)

            return Response(
                {
                    "status": "success",
                    "nth": serializer.data.fibonacci_number
                }, 
                status=HTTP_200_OK
            )
        except FibonacciHistory.DoesNotExist:
            create_fibonacci.delay(n)

            return Response("")
