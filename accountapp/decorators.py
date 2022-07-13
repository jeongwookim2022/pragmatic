from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])

        # url에서 현재의 pk에 해당하는 object(현재 user)와
        # 요청을 보낸 user와 동일한지 확인.
        if not user == request.user:
            return HttpResponseForbidden()

        return func(request, *args, **kwargs)

    return decorated