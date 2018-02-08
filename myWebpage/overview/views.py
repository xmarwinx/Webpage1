from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json


#def overview(request):
    #return HttpResponse("overview")
  #  context = {'a': 'b'}

 #   return render(request, 'overview/index.html', context)

#test

def overview(request):
    #latest_question_list = ["a", "b", "c", "d"]
    #return HttpResponse(latest_question_list)

    #file2 = open("/home/marwin/Desktop/test3.json", "r")

    #return HttpResponse("hallo")

    with open("/home/marwin/Desktop/test3.json") as json_data:
        d = json.load(json_data)
        aString = ""
        #print(d)

        #print(d[1]["adress"])

        for i, x in enumerate(d, start=1):
            aString = (aString +
                      "<h2>Entry %s:</h2>" % i +
                      "<b>Title: </b>" + x["title"] + "</p></p>" +
                      "<b>Adress: </b>" + x["adress"] + "</p></p>" +
                      "<b>Date: </b>" + x["date"] + "</p></p>" +
                      "<b>Description: </b>" + x["description"] + "</p></p>" +
                      "<b>ImageURL: </b>" + x["image"] +  "</p></p>" +
                      "<b>ImageLinkTest: </b>" + '<a href="%s">This is the Link</a>' % x["image"]
                       )


        return HttpResponse(aString)


def detail(request):
    return HttpResponse("detail View")
