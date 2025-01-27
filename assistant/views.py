from django.shortcuts import render
from .forms import BlogForm
from django.http import HttpResponse
from ollama import chat

def assistant(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        result = ""

        if form.is_valid():
            topic = form.cleaned_data.get('topic')
            text = form.cleaned_data.get('text')
            tone = form.cleaned_data.get('tone')

            if topic:
                prompt = f"Generate 2 blog ideas for the topic `{topic}`"
            elif text and tone:
                prompt = f"Rewrite the following text in a {tone} tone: `{text}`"
            else:
                return HttpResponse("Please provide either a topic or text with a selected tone.")
            
            try:
                response = chat(model='llama3.2', messages=[
                    {
                        "role": 'user',
                        'content': prompt,
                    },
                ])
                result = response.message.content
            except Exception as e:
                result = f"Error connecting to Ollama {str(e)}"
        return HttpResponse(result)
    else:
        form = BlogForm()
    return render(request, "assistant/index.html", {"form": form})