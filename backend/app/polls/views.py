import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Question
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    if request.method == "GET":
        questions = Question.objects.all().values()
        return JsonResponse(
            {"code": 200, "message": "success", "data": list(questions)}
        )
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


@csrf_exempt
def create(request):
    if request.method == "POST":
        try:
            form_data = json.loads(request.body.decode("utf-8"))
            question = Question.objects.create(
                question_text=form_data["question_text"],
                pub_date=timezone.now(),
                updated_date=timezone.now(),
            )
            return JsonResponse({"code": 200, "message": "success", "data": None})
        except Exception as e:
            return JsonResponse({"code": 500, "message": str(e), "data": None})
    return JsonResponse({"code": 405, "message": "Method Not Allowed", "data": None})


@csrf_exempt
def get_poll(request):
    id = request.GET.get("id")
    if not id:
        return JsonResponse({"code": 400, "message": "missing parameter", "data": None})
    if request.method == "GET":
        try:
            question = Question.objects.filter(id=id).values()
            return JsonResponse(
                {"code": 200, "message": "success", "data": list(question)}
            )
        except Exception as e:
            return JsonResponse({"code": 500, "message": str(e), "data": None})
    return JsonResponse({"code": 405, "message": "Method Not Allowed", "data": None})


@csrf_exempt
def get_poll_list(request):
    if request.method == "GET":
        try:
            questions = Question.objects.all().values()
            return JsonResponse(
                {"code": 200, "message": "success", "data": list(questions)}
            )
        except Exception as e:
            return JsonResponse({"code": 500, "message": str(e), "data": None})
    return JsonResponse({"code": 405, "message": "Method Not Allowed", "data": None})


@csrf_exempt
def delete_poll(request):
    id = request.GET.get("id")
    if not id:
        return JsonResponse({"code": 400, "message": "missing parameter", "data": None})
    if request.method == "DELETE":
        try:
            Question.objects.filter(id=id).delete()
            return JsonResponse({"code": 200, "message": "success", "data": None})
        except Exception as e:
            return JsonResponse({"code": 500, "message": str(e), "data": None})
    return JsonResponse({"code": 405, "message": "Method Not Allowed", "data": None})


@csrf_exempt
def update_poll(request):
    form_data = json.loads(request.body.decode("utf-8"))
    if not form_data.get("id") or not form_data.get("question_text"):
        return JsonResponse({"code": 400, "message": "missing parameter", "data": None})
    if request.method == "PUT":
        try:
            Question.objects.filter(id=form_data["id"]).update(
                question_text=form_data["question_text"],
                updated_date=timezone.now(),
            )
            return JsonResponse({"code": 200, "message": "success", "data": None})
        except Exception as e:
            return JsonResponse({"code": 500, "message": str(e), "data": None})
    return JsonResponse({"code": 405, "message": "Method Not Allowed", "data": None})
