from django.shortcuts import render
from core.forms import LoginForm
import json
from .models import TicketSystem
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

def home(request):
    response = requests.get('http://api.ipstack.com/45.250.227.46?access_key=13eb3f02919ed947333aa67e56e72174&output=json')
    geodata = response.json()
    json_pretty = json.dumps(geodata, indent=2)
    context = {
        "json_pretty": json_pretty,
    }
    return render(request, 'core/home.html', context)

def login(request):
    Ticket = "not submitted"

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            Ticket = MyLoginForm.cleaned_data['ClientTicketID']
            Summary = MyLoginForm.cleaned_data['Summary']
            Description = MyLoginForm.cleaned_data['Description']
    else:
        MyLoginForm = LoginForm()

    return render(request, 'core/loggedin.html', {"ClientTicketID": Ticket, "Summary": Summary, "Description": Description})


def submit_req(request):
    with open('rfc.txt') as json_file:
        data = json.load(json_file)

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            data["ns0:Process"]["ns2:Ticket"]["ClientTicketID"] = MyLoginForm.cleaned_data['ClientTicketID']
            data["ns0:Process"]["ns2:Ticket"]["Summary"] = MyLoginForm.cleaned_data['Summary']
            data["ns0:Process"]["ns2:Ticket"]["Description"] = MyLoginForm.cleaned_data['Description']
    else:
        MyLoginForm = LoginForm()

    json_pretty = json.dumps(data)
    context = {
        "json_pretty": json_pretty,
    }
    return render(request, 'core/hello.html', context)
    #response = requests.post('https://a-esb.kpn.org/IG_V3_Rest/ITIL.svc/Change',auth=('ESB-AUTOMIC-ARA-ACC', XXXXXXXXXXXX'), headers=headers, data=data)
    #print(response)
    #print(response.json())

@csrf_exempt
def tech_resp(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        #print(json_data["header:Header"]["MessageType"])
        #print(json_data["process:Process"]["ticket:Ticket"]["@xmlns:ticket"])

        ticket_attrs = {
            "ClientTicketID": json_data["process:Process"]["ticket:Ticket"]["ClientTicketID"],
            "xmlns_process": json_data["process:Process"]["@xmlns:process"],
            "xmlns_header": json_data["header:Header"]["@xmlns:header"],
            "xmlns_ticket": json_data["process:Process"]["ticket:Ticket"]["@xmlns:ticket"],
            "PartnerTicketID": json_data["process:Process"]["ticket:Ticket"]["PartnerTicketID"],
            "Source": json_data["header:Header"]["Source"],
            "Destination": json_data["header:Header"]["Destination"],
            "Version": json_data["header:Header"]["Version"],
            "MessageDate": json_data["header:Header"]["MessageDate"],
            "MessageID": json_data["header:Header"]["MessageID"],
            "ProcessType": json_data["header:Header"]["ProcessType"],
            "ActionType": json_data["header:Header"]["ActionType"],
            "MessageType": json_data["header:Header"]["MessageType"],
            "IsTask": json_data["header:Header"]["IsTask"],
            "Status": json_data["header:Header"]["Status"],
            "StatusText": json_data["header:Header"]["StatusText"],
        }
        result = TicketSystem.objects.create(**ticket_attrs)

        return JsonResponse({'Message': 'Technical Response Inserted in Database!'})

    return JsonResponse({"message": "Something Wrong with Request!"})

@csrf_exempt
def business_resp(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        validate_ticket = json_data["process:Process"]["ticket:Ticket"]["ClientTicketID"]
        print(validate_ticket)
        is_valid = TicketSystem.objects.get(ClientTicketID=validate_ticket)
        print(is_valid)
        if is_valid:
            ticket_attrs = {
                "xmlns_process": json_data["process:Process"]["@xmlns:process"],
                "xmlns_header": json_data["header:Header"]["@xmlns:header"],
                "xmlns_ticket": json_data["process:Process"]["ticket:Ticket"]["@xmlns:ticket"],
                "PartnerTicketID": json_data["process:Process"]["ticket:Ticket"]["PartnerTicketID"],
                "Source": json_data["header:Header"]["Status"],
                "Destination": json_data["header:Header"]["Destination"],
                "Version": json_data["header:Header"]["Version"],
                "MessageDate": json_data["header:Header"]["MessageDate"],
                "MessageID": json_data["header:Header"]["MessageID"],
                "ProcessType": json_data["header:Header"]["ProcessType"],
                "ActionType": json_data["header:Header"]["ActionType"],
                "MessageType": json_data["header:Header"]["MessageType"],
                "IsTask": json_data["header:Header"]["IsTask"],
                "Status": json_data["header:Header"]["Status"],
                "StatusText": json_data["header:Header"]["StatusText"],
            }
            TicketSystem.objects.filter(ClientTicketID=validate_ticket).update(**ticket_attrs)
            return JsonResponse({'Message': 'Business Response Updated in Database!'})
        return JsonResponse({'Message': 'Business Response has invalid ClientTicketID !'})
    return JsonResponse({"message": "Something Wrong with Request!"})


@csrf_exempt
def comment_resp(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        validate_ticket = json_data["process:Process"]["ticket:Ticket"]["ClientTicketID"]
        print(validate_ticket)
        is_valid = TicketSystem.objects.get(ClientTicketID=validate_ticket)
        print(is_valid)
        if is_valid:
            ticket_attrs = {
                "xmlns_process": json_data["process:Process"]["@xmlns:process"],
                "xmlns_header": json_data["header:Header"]["@xmlns:header"],
                "xmlns_ticket": json_data["process:Process"]["ticket:Ticket"]["@xmlns:ticket"],
                "PartnerTicketID": json_data["process:Process"]["ticket:Ticket"]["PartnerTicketID"],
                "Source": json_data["header:Header"]["Status"],
                "Destination": json_data["header:Header"]["Destination"],
                "Version": json_data["header:Header"]["Version"],
                "MessageDate": json_data["header:Header"]["MessageDate"],
                "MessageID": json_data["header:Header"]["MessageID"],
                "ProcessType": json_data["header:Header"]["ProcessType"],
                "ActionType": json_data["header:Header"]["ActionType"],
                "MessageType": json_data["header:Header"]["MessageType"],
                "IsTask": json_data["header:Header"]["IsTask"],
                "Status": json_data["header:Header"]["Status"],
                "StatusText": json_data["header:Header"]["StatusText"],
                "Comment": json_data["process:Process"]["ticket:Ticket"]["Comment"],
            }
            TicketSystem.objects.filter(ClientTicketID=validate_ticket).update(**ticket_attrs)
            return JsonResponse({'Message': 'Comment Response Updated in Database!'})
        return JsonResponse({'Message': 'Comment Response has invalid ClientTicketID !'})
    return JsonResponse({"message": "Something Wrong with Request!"})
