class UserQuerySetMixin():
    user_field = 'user'
    allow_view_staff = False

    # def get_queryset(self, *arg, **kwarg):   # ????????????????
    #     request = self.request  # ?????????????????????
    #     user = request.user
    #     qs = super().get_queryset(*arg, **kwarg)
    #     data = {self.user_field: user}
    #     if user.is_staff and self.allow_view_staff:     # ???????????
    #         return qs
    #     elif not user.is_authenticated:
    #         return qs.none()
    #     return qs.filter(**data)
