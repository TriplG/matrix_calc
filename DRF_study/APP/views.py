from django.shortcuts import render, redirect
import numpy as np
from django.http import QueryDict

from django.views.generic import ListView, DetailView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *

result = None
N = 2
M = 2
transponse_matrix = None
det_matrix = None
show_matrix = None
matrix_b_n, matrix_b_m = N, M
matrix_text = ''

def index(request):
    global result, N, M, transponse_matrix, det_matrix, show_matrix
    global matrix_b_n, matrix_b_m, matrix_text
    context = {
        'N': range(N),
        'M': range(M),
        'nxB': range(matrix_b_n),
        'mxB': range(matrix_b_m),
        'title': 'Калькулятор матриц'
    }
    if matrix_text is not None:
        context['matrix'] = show_matrix
        context['matrix_text'] = matrix_text

    if transponse_matrix is not None:
        context['matrix'] = transponse_matrix
        context['matrix_text'] = 'Транспонированная матрица:'

    if det_matrix is not None:
        context['result'] = round(det_matrix, 1)
        context['result_text'] = 'Определитель равен:'


    return render(request, 'APP/index.html', context=context)


class ExtensMatrix(ListView):
    def get(self, request):
        global N, M
        N = N + 1
        M += 1

        print(request.POST)

        return redirect('/')


class ReduceMatrix(ListView):
    def get(self, request):
        global N, M
        N -= 1
        M -= 1

        return redirect('/')


class InputMatrix(ListView):
    def post(self, request):
        global N, M
        N = int(request.POST['lineSize'])
        M = int(request.POST['columnSize'])

        return redirect('/')


class InputMatrixB(ListView):
    def post(self, request):
        global matrix_b_n, matrix_b_m
        matrix_b_n = int(request.POST['lineSizeB'])
        matrix_b_m = int(request.POST['columnSizeB'])
        print(request.POST)
        return redirect('/')


class TransposeMatrix(ListView):
    def post(self, request):
        global N, M, transponse_matrix, det_matrix, show_matrix, matrix_text
        det_matrix = None
        show_matrix = None
        matrix_text = None
        matrix_post = [int(i) for i in request.POST.getlist('1')]
        matr_result = []
        a = iter(matrix_post)
        for i in range(N):
            arr = []
            for j in range(M):
                arr.append(next(a))
            matr_result.append(arr)
        transponse_matrix = np.array(matr_result)
        transponse_matrix = transponse_matrix.transpose()

        return redirect('/')


class DeterminantMatrix(ListView):
    def post(self, request):
        global N, M, det_matrix, transponse_matrix, show_matrix, matrix_text
        transponse_matrix = None
        show_matrix = None
        matrix_text = None
        if N != M:
            det_matrix = 'Введите квадратную матрицу'
            return redirect('/')
        matrix_post = [int(i) for i in request.POST.getlist('1')]
        matr_result = []
        a = iter(matrix_post)
        for i in range(N):
            arr = []
            for j in range(M):
                arr.append(next(a))
            matr_result.append(arr)
        det_matrix = np.array(matr_result)
        det_matrix = np.linalg.det(det_matrix)
        print(det_matrix)
        return redirect('/')


class AdditionMatrix(ListView):
    def post(self, request):
        global N, M, matrix_b_n, matrix_b_m, matrix_text
        global transponse_matrix, det_matrix, show_matrix
        det_matrix = None
        transponse_matrix = None

        if N == matrix_b_n and M == matrix_b_m:
            matrix_postA = [int(i) for i in request.POST.getlist('1')]
            matrix_postB = [int(i) for i in request.POST.getlist('2')]
            matr_resultA = []
            matr_resultB = []
            a = iter(matrix_postA)
            b = iter(matrix_postB)
            for i in range(N):
                arrA = []
                arrB = []
                for j in range(M):
                    arrA.append(next(a))
                    arrB.append(next(b))
                matr_resultA.append(arrA)
                matr_resultB.append(arrB)

            matr_resultA = np.array(matr_resultA)
            matr_resultB = np.array(matr_resultB)

            show_matrix = matr_resultB + matr_resultA
            print(show_matrix)
            matrix_text = 'Результат сложения матриц'
        else:
            show_matrix = None
            matrix_text = 'Введите матрицы одинакового размера'

        return redirect('/')


class DifferenceMatrix(ListView):
    def post(self, request):
        global N, M, matrix_b_n, matrix_b_m, matrix_text
        global transponse_matrix, det_matrix, show_matrix
        det_matrix = None
        transponse_matrix = None
        if N == matrix_b_n and M == matrix_b_m:
            matrix_postA = [int(i) for i in request.POST.getlist('1')]
            matrix_postB = [int(i) for i in request.POST.getlist('2')]
            matr_resultA = []
            matr_resultB = []
            a = iter(matrix_postA)
            b = iter(matrix_postB)
            for i in range(N):
                arrA = []
                arrB = []
                for j in range(M):
                    arrA.append(next(a))
                    arrB.append(next(b))
                matr_resultA.append(arrA)
                matr_resultB.append(arrB)

            matr_resultA = np.array(matr_resultA)
            matr_resultB = np.array(matr_resultB)

            show_matrix = matr_resultA - matr_resultB
            print(show_matrix)
            matrix_text = 'Результат разности матриц'
        else:
            show_matrix = None
            matrix_text = 'Введите матрицы одинакового размера'

        return redirect('/')


class MultiplicationMatrix(ListView):
    def post(self, request):
        global N, M, matrix_b_n, matrix_b_m, matrix_text
        global transponse_matrix, det_matrix, show_matrix
        det_matrix = None
        transponse_matrix = None
        if N == matrix_b_m:
            matrix_postA = [int(i) for i in request.POST.getlist('1')]
            matrix_postB = [int(i) for i in request.POST.getlist('2')]
            matr_resultA = []
            matr_resultB = []
            a = iter(matrix_postA)
            b = iter(matrix_postB)
            for i in range(N):
                arrA = []
                arrB = []
                for j in range(M):
                    arrA.append(next(a))
                    arrB.append(next(b))
                matr_resultA.append(arrA)
                matr_resultB.append(arrB)
            show_matrix = np.dot(matr_resultA, matr_resultB)
            print(show_matrix)
            matrix_text = 'Результат умножения матриц'
        else:
            show_matrix = None
            matrix_text = 'Количество строк А должно совпадать с количество столбцов В'

        return redirect('/')

# class CalcNumbers(ListView):
#     def post(self, request):
#         global result
#         # result = None
#         if request.POST['Var1'] == '+':
#             result = int(request.POST.get('var1')) + int(request.POST.get('var2'))
#         elif request.POST['Var1'] == '-':
#             result = int(request.POST.get('var1')) - int(request.POST.get('var2'))
#         elif request.POST['Var1'] == '*':
#             result = int(request.POST.get('var1')) * int(request.POST.get('var2'))
#         elif request.POST['Var1'] == '/':
#             result = int(request.POST.get('var1')) / int(request.POST.get('var2'))
#         else:
#             result = 'Выберите действие'
#
#         return redirect('/')









