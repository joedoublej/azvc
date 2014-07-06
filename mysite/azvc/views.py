from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from azvc.models import Author, Post

class HomeView(TemplateView):
	template_name = 'main.html'

	def get_context_data(self, **kwargs):
		return {
			'authors': Author.objects.order_by('name'),
			'posts': Posts.objects.order_by('created'),
		}


main = HomeView.as_view()
