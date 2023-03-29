from rest_framework.views import APIView
from rest_framework.response import Response


class LogoutView(APIView):
    def get(self, request):
        token = request.COOKIES.get('Bte8wiZdhuuwmItf0lioiEfe9oPh9ArBi_lHlUZQI50')
        if not token:
            return Response({
                'message': 'You are not logged in.'
            })        
            
        response = Response({
            'message': 'Logout successful'
        })
        response.set_cookie(
            key='Bte8wiZdhuuwmItf0lioiEfe9oPh9ArBi_lHlUZQI50',
            value='',
            max_age=1,
            httponly=True,
            # samesite='None',
            # secure=True
        )
        
        return response
