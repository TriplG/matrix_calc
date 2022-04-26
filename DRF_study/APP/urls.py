from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='home'),
    # path('CalcNumbers/', CalcNumbers.as_view(), name='CalcNumbers'),
    path('extens_matrix/', ExtensMatrix.as_view(), name='ExtensMatrix'),
    path('reduce_matrix/', ReduceMatrix.as_view(), name='ReduceMatrix'),
    path('input_matrix/', InputMatrix.as_view(), name='InputMatrix'),
    path('transponse_matrix/', TransposeMatrix.as_view(), name='TransposeMatrix'),
    path('determinant_matrix/', DeterminantMatrix.as_view(), name='DeterminantMatrix'),
    path('InputMatrixB/', InputMatrixB.as_view(), name='InputMatrixB'),
    path('AdditionMatrix/', AdditionMatrix.as_view(), name='AdditionMatrix'),
    path('DifferenceMatrix/', DifferenceMatrix.as_view(), name='DifferenceMatrix'),
    path('MultiplicationMatrix/', MultiplicationMatrix.as_view(), name='MultiplicationMatrix'),


]
