from django.http import HttpResponse
from django.template import loader
# 处理 404
from django.http import Http404
# 快捷渲染函数 render, 此时就不需要 HttpResponse 和 loader 了
# 快捷处理 404, 此时就不需要 Http404 了
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice


# Create your views here.
# tip 感觉视图更多像是 controller

# class IndexView(generic.ListView):
#     def get_queryset(self):
#         return Question.objects.order_by('-pub_date')[:5]

def index(request):
    # 切片不会影响原列表
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    # tip string.join(iterable)
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # 渲染模板
    # return HttpResponse(template.render(context, request))
    # 使用一种更简单快捷的方式渲染模板
    return render(request, 'polls/index.html', context)


# class DetailView(generic.DetailView):
#
#     def get_detail(self, question_id):
#         return Question.objects.get(pk=question_id)
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    # 简化版
    question = get_object_or_404(Question, pk=question_id)
    print('=====>', question, question.question_text, question.pub_date)
    # return HttpResponse(question.pub_date)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # tip request.POST 是一个类字典对象，让你可以通过关键字的名字获取提交的数据。
        #  这个例子中， request.POST['choice'] 以字符串形式返回选择的 Choice 的 ID。
        #  request.POST 的值永远是字符串。
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "error!!!You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # tip 重定向到结果界面
        #   args 是一个 tuple
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # return HttpResponse("You're voting on question %s." % question_id)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


'''以下代码是使用通用视图更改后的代码'''


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    # tip 对于 ListView， 自动生成的 context 变量是 question_list。
    #  为了覆盖这个行为，我们提供 context_object_name 属性，表示我们想使用 latest_question_list。
    context_object_name = 'latest_question_list'

    # ques 这难道是一个覆盖函数吗
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    # tip 每个通用视图需要知道它将作用于哪个模型，这就由 model 属性提供
    model = Question
    # tip 使用 template_name 来告诉通用视图使用什么模板
    # 对于 DetailView ， question 变量会自动提供—— 因为我们使用 Django 的模型（Question）
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
