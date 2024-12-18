from django.views.generic import TemplateView

class CommandView(TemplateView):
    template_name = 'live_refund_monitor/command.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 假设你通过 URL 参数传递一个参数，例如 'my_param'
        my_param = self.request.GET.get('run_param', 'echo please input run_param')  # 获取 GET 参数
        context['run_param'] = my_param  # 将参数添加到上下文
        return context
