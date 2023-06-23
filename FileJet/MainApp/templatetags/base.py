from django import template
from ProfileApp.models import Profile
from FileApp.models import Message, Chat

register = template.Library()


@register.simple_tag
def give_user(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)
        return profile
    
@register.simple_tag
def give_chats(request):
    if request.user.is_authenticated:
        chats = Chat.objects.filter(send_user = request.user)
        # context["chats"] = chats
        chat_and_last_message_list = []
        for chat in chats:
            chat_and_last_message = []
            try:
                last_message = Message.objects.filter(chat = chat).order_by('pk').latest('pk')
            except Message.DoesNotExist:
                last_message = ''
            profile_image = Profile.objects.get(user = chat.send_user)
            chat_and_last_message.append(profile_image)
            chat_and_last_message.append(last_message)
            chat_and_last_message.append(chat)
            chat_and_last_message_list.append(chat_and_last_message)
            
        return chat_and_last_message_list