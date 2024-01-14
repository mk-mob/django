from django.views.generic import TemplateView
class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self):
        context = super().get_context_data()
        context["username"] = "Kame"
        return context
    
    
class AboutView(TemplateView):
    template_name = "about.html"
    def get_context_data(self):
        context = super().get_context_data()
        context["num_services"] = "456789123"
        context["skills"] = [
            "Python","C++","Javascript","Rust","Go",
        ]
        return context