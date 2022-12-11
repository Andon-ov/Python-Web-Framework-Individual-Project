from django.http import Http404


class OwnerRequiredMixin:
    def get(self, request, *args, **kwargs):
        result = super().get(request, *args, **kwargs)
        if request.user.id != kwargs.get('pk'):
            raise Http404
        return result

    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)
        if request.user.id != kwargs.get('pk'):
            raise Http404
        return result


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())
