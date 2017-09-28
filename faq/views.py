# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from faq.models import Topic, Question


def _fragmentify(model, slug, url=None):
    get_object_or_404(model.objects.published().filter(slug=slug))
    url = url or reverse('faq-topic-list')
    fragment = '#%s' % slug

    return redirect(url + fragment, permanent=True)


class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context['topic'] = Topic.objects.published().get(
            slug=context['question'].topic.slug
        )
        return context

    def get_template_names(self):
        return ['faq/question_detail.html']


class TopicDetailView(DetailView):
    model = Topic

    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context['question_list'] = Question.objects.published().filter(
            topic__slug=context['topic'].slug
        )
        return context

    def get_template_names(self):
        return ['faq/topic_detail.html']


class TopicListView(ListView):
    model = Topic

    def get_template_names(self):
        return ['faq/topic_list.html']


def question_detail(request, topic_slug, slug):
    """
    A detail view of a Question.

    Simply redirects to a detail page for the related :model:`faq.Topic`
    (:view:`faq.views.topic_detail`) with the addition of a fragment
    identifier that links to the given :model:`faq.Question`.
    E.g. ``/faq/topic-slug/#question-slug``.

    """
    url = reverse('faq-topic-detail', kwargs={'slug': topic_slug})
    return _fragmentify(Question, slug, url)


def topic_detail(request, slug):
    """
    A detail view of a Topic

    Simply redirects to :view:`faq.views.topic_list` with the addition of
    a fragment identifier that links to the given :model:`faq.Topic`.
    E.g., ``/faq/#topic-slug``.

    """
    return _fragmentify(Topic, slug)
