from django.shortcuts import render
from django.views import View
import pyyoutube

from ysearch.settings import YOUTUBE_API_KEY

api = pyyoutube.Api(api_key=YOUTUBE_API_KEY)

class SuggestionView(View):

    def get(self, request, *args, **kwargs):
        search = request.GET.get("search", "")
        response = api.search_by_keywords(q=search, search_type=["video"], count=5)
        return render(request, 'suggestions.html', {'items': response.items})

class GetVideoView(View):

    def post(self, request, *args, **kwargs):
        search = request.POST.get("search")
        video = None
        if search:
            resp = api.search_by_keywords(q=search, search_type=["video"], count=1)
            video_id = resp.items[0].id.videoId
            video = api.get_video_by_id(video_id=video_id).items[0]
        return render(request, 'video_result.html', {'video': video})