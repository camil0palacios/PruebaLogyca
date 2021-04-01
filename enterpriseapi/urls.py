from django.urls import path
from .views import AllEnterprise, EnterpriseByNit, EnterpriseById, EnterpriseView, AllCodeById, CodeView

urlpatterns = [
    # enpoint para obtener todos las empresas
    path('AllEnterprise/', AllEnterprise.as_view()), 
    # enpoint para obtener la empresa con un nit especifico y los codigos asociados
    path('EnterpriseByNit/<int:nit>/', EnterpriseByNit.as_view()),
    # endpoint para obtener una empresa a partir de un id de un codigo
    path('EnterpriseById/<int:id>/', EnterpriseById.as_view()),
    # endpoint para hacer get, post y patch sobre las empresas
    path('Enterprise/', EnterpriseView.as_view()),
    path('Enterprise/<int:id>/', EnterpriseView.as_view()),
    # endpoint para obtener todas los codigos a partir de un Id de una empresa
    path('AllCodesById/<int:id>/', AllCodeById.as_view()),
    # endpoint para hacer get, post y patch sobre los codigos
    path('Code/', CodeView.as_view()),
    path('Code/<int:id>/', CodeView.as_view())
]