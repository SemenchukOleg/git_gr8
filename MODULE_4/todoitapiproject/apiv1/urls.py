from django.urls import path
from tasks import views as tasks_views

urlpatterns = [
    #tasks data
    path('tasks/', tasks_views.get_task_list),
    path('tasks/task/<int:id>', tasks_views.get_or_update_task_by_id),
    path('tasks/priorities', tasks_views.get_task_priorities_list),
    path('tasks/complete-all/', tasks_views.complete_all_tasks),
    path('tasks/uncomplete-all/', tasks_views.uncomplete_all_tasks),
    path('tasks/delete-all/', tasks_views.delete_all_tasks)
]