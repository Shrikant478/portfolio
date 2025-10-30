from django.shortcuts import render

def home(request):
    """Main portfolio page view"""
    context = {
        'name': 'K Shrikant',
        'designation': 'Python Developer',
        'projects': [
            {
                'name': 'E-Commerce Platform',
                'description': 'Built a full-stack e-commerce application using Django, PostgreSQL, and REST APIs with payment gateway integration.'
            },
            {
                'name': 'Task Management System',
                'description': 'Developed a collaborative task management tool with real-time updates using Django Channels and WebSockets.'
            },
            {
                'name': 'Data Analysis Dashboard',
                'description': 'Created an interactive dashboard for data visualization using Django, Pandas, and Chart.js for business analytics.'
            },
            {
                'name': 'Blog Platform',
                'description': 'Designed and implemented a modern blogging platform with user authentication, comments, and rich text editor support.'
            }
        ]
    }
    return render(request, 'docs/index.html', context)
