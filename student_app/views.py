from django.shortcuts import render

def student_form(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('student_name', '').strip()
        student_id = request.POST.get('student_id', '').strip()
        major = request.POST.get('major', '')
        class_standing = request.POST.get('class_standing', '')
        languages = request.POST.getlist('languages')
        grad_year = request.POST.get('grad_year', '')
        comments = request.POST.get('comments', '')

        # Validation: Check if Name or ID are blank
        if not name or not student_id:
            return render(request, 'student_app/student_form.html', {
                'error': 'Student Name and Student ID are required fields.',
                'student_name': name,
                'student_id': student_id,
                'major': major,
                'class_standing': class_standing,
                'languages': languages,
                'grad_year': grad_year,
                'comments': comments,
            })

        # Pass data to results page if valid
        context = {
            'student_name': name,
            'student_id': student_id,
            'major': major,
            'class_standing': class_standing,
            'languages': ", ".join(languages) if languages else "None",
            'grad_year': grad_year,
            'comments': comments,
        }
        return render(request, 'student_app/student_results.html', context)

    return render(request, 'student_app/student_form.html')