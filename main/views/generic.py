from annoying.decorators import render_to
from django.conf import settings
from django.shortcuts import get_object_or_404

from ..models import Conversation


@render_to("home.html")
def home(request):
    if not (request.get_host().startswith("spa.")
            or settings.DEBUG):
        return {"TEMPLATE": "home.html"}
    return {}


@render_to("conversation_list.html")
def conversation_list(request):
    conversations = Conversation.objects.all()
    return {"conversations": conversations}


@render_to("conversation_view.html")
def conversation_view(request, conversation_id):
    conversation = get_object_or_404(Conversation, pk=conversation_id)
    return {"conversation": conversation}
