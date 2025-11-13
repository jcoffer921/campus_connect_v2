# network/views.py
from django.shortcuts import render
from django.templatetags.static import static
from .models import Student, Connection

def network_view(request):
    students = Student.objects.all().order_by('id')
    connections = Connection.objects.all()

    default_avatar = static("images/default.png")

    nodes = []
    for s in students:
        img_url = s.image.url if getattr(s, "image", None) and s.image else default_avatar
        nodes.append({
            "id": s.id,
            "label": s.name,
            "title": f"Major: {s.major or 'N/A'}<br>Year: {s.year or 'N/A'}",
            "image": img_url,                 # PNG for node
            "size": 34,                       # base size; we’ll scale on hover
        })

    edges = [{"from": c.student1_id, "to": c.student2_id} for c in connections]

    return render(request, "network/network.html", {"nodes": nodes, "edges": edges})
