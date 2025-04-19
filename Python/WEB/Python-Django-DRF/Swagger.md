. Installation

* `pip install drf-spectacular`

2. Setting.py
    * `INSTALL_APPS=[... , 'drf-spectacular' ,...]` # Swagget
    * `REST_FRAMEWORK = {... , 'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema' , ...}`
    * Add this line
     ```python
   SPECTACULAR_SETTINGS = {
      'TITLE': 'Your Project API',
      'DESCRIPTION': 'Your project description',
      'VERSION': '1.0.0',
      'SERVE_INCLUDE_SCHEMA': False,
      # OTHER SETTINGS
   }

   ```
3. `urls.py` #global urls.py
   ```python
   from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
   
   urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('home.urls')),
        path('todos/', include('todo.urls')),
        ...
        # YOUR PATTERNS
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        # Optional UI:
        path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
      ]
   ```

4. اگر بخواهیم مواردی که در صفحه سوئگر هست را تغییر بدهید به روش زیر امکان پذیر خواهد بود


* File: `/todo/views.py`
   ```python
   from drf_spectacular.utils import extend_schema
  
    class TodosListApiView(APIView):
        @extend_schema(# ✅️
             request=TodoSerializer,# ✅️
             responses={201: TodoSerializer},# ✅️
             description='this api is used for get all todos list',# ✅️
        )# ✅️
    def get(self, request: Request):
        todos = Todo.objects.order_by('priority').all()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(None, status.HTTP_400_BAD_REQUEST)


   class TodosDetailApiView(APIView):
        def get_object(self, todo_id: int):
            try:
                todo = Todo.objects.get(pk=todo_id)
                return todo
        except Todo.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)

       def get(self, request: Request, todo_id:int):
            todo = self.get_object(todo_id)
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status.HTTP_200_OK)

       def put(self, request: Request, todo_id:int):
            todo = self.get_object(todo_id)
            serializer = TodoSerializer(todo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_202_ACCEPTED)
            return Response(None, status.HTTP_400_BAD_REQUEST)

       def delete(self, request: Request, todo_id:int):
            todo = self.get_object(todo_id)
            todo.delete()
            return Response(None, status.HTTP_204_NO_CONTENT)

   ```