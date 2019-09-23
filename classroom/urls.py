from django.urls import include, path

from .views import classroom, students, teachers, board, upload

urlpatterns = [
    path('', classroom.home, name='home'),
    path(r'home/',board.home, name='discussion'),
    path(r'boards/', board.board_topics, name='board_topics'),
    path(r'boards/new/', board.new_topic, name='new_topic'),
    path(r'homequiz/', classroom.homequiz, name='homequiz'),
    
    path(r'^$',upload.home,name='upload'),
    path(r'^uploads/simple/$', upload.simple_upload, name='simple_upload'),
    path(r'^uploads/form/$', upload.model_form_upload, name='model_form_upload'),
    path('students/', include(([
        path('', students.QuizListView.as_view(), name='quiz_list'),
        path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
    ], 'classroom'), namespace='students')),

    path('teachers/', include(([
        path('', teachers.QuizListView.as_view(), name='quiz_change_list'),
        path('quiz/add/', teachers.QuizCreateView.as_view(), name='quiz_add'),
        path('quiz/<int:pk>/', teachers.QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/', teachers.QuizDeleteView.as_view(), name='quiz_delete'),
        path('quiz/<int:pk>/results/', teachers.QuizResultsView.as_view(), name='quiz_results'),
        path('quiz/<int:pk>/question/add/', teachers.question_add, name='question_add'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/', teachers.question_change, name='question_change'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', teachers.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'classroom'), namespace='teachers')),
]
