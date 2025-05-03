import argparse
import requests as req
from termcolor import colored

def chkmodel(server, selmodel):
    modarr=[]
    response=req.get("http://" + server + "/api/tags", verify=True, timeout=600)
    fnd=0
    if response.status_code == 200:
        response_text = response.json()
        models=response_text['models']
        for model in models:
            modarr.append(model['name'])
            if model['name'] == selmodel:
                fnd=1
    if fnd==1:
        return True
    else:
        print("ERROR - " + selmodel + " is not a valid model\nThe following models can be selected " + str(modarr))
        return False
    
def getmodel(server):
    modarr=[]
    response=req.get("http://" + server + "/api/tags", verify=True, timeout=300)
    fnd=0
    if response.status_code == 200:
        response_text = response.json()
        models=response_text['models']
        for model in models:
            modarr.append(model['name'])
    loop=True
    while loop:
        cnt=0
        print("\n")
        for model in modarr:
            cnt+=1
            print(str(cnt) + ") " + model)
        resp=input("Which of the above models do you wish to interact with ? ")
        try:
            respsel = int(resp)
            if respsel>0 and respsel<=len(modarr):
                selmodel=modarr[respsel-1]
                loop=False
        except:
            loop=True
    return selmodel


def proc(message, messarray, model, name, server):
    messarray.append({
        "content": message,
        "role": "user"
    })
    payload={
        "model": model, 
        "messages": messarray,
        "stream": False

    }
    response=req.post("http://" + server + "/api/chat", json=payload, verify=True, timeout=300)
    if response.status_code == 200:
        response_text = response.json()
        print(colored("\n" + name + ": " + str(response_text['message']['content']) + "\n", "blue"))
        messarray.append({
            "role": "assistant",
            "content": response_text['message']['content']
        })
    return messarray

def imgproc(message, messarray, model, name, server):
    img=input("AI: What is the link of the image you would like to describe? ")
    message="Describe this image? "
    img_data = req.get(img).content
    with open('image.jpg', 'wb') as handler:
        handler.write(img_data)
    handler.close()
    messarray.append({
        "content": message,
        "role": "user",
        "images": ["./image.jpg"]
    })
    payload={
        "model": model, 
        "messages": messarray,
        "stream": False

    }
    response=req.post("http://" + server + "/api/chat", json=payload, verify=True, timeout=300)
    if response.status_code == 200:
        response_text = response.json()
        print(colored("\n" + name + ": " + str(response_text['message']['content']) + "\n", "blue"))
        messarray.append({
            "role": "assistant",
            "content": response_text['message']['content']
        })
    return messarray

parser=argparse.ArgumentParser(prog="appcmd.py",
                               description="Command line AI interaction",
                               epilog="-s serveraddress:port -m model -n AI name")
parser.add_argument("-s", "--server", dest="server", default="localhost:11434")
parser.add_argument("-n", "--name", dest="name", default="AI")
parser.add_argument("-m", "--model", dest="model", default="")
args = parser.parse_args()
messarray=[]
model=args.model
if args.model=="":
    model=getmodel(args.server)
    modchk=True
else:
    modchk=chkmodel(args.server, args.model)
if modchk == True:
    print(colored("\nYou are entering a new conversation with " + model + ". To exit the conversation, enter just Bye! when you are prompted\n", "yellow"))
    prompt=input("User: ")
    if prompt != "Bye!":
        if prompt == "Image!":
            messarray=imgproc(prompt, messarray, model, args.name, args.server)
        else:
            messarray=proc(prompt, messarray, model, args.name, args.server)
        while prompt != "Bye!":
            prompt=input("User: ")
            messarray=proc(prompt, messarray, model, args.name, args.server)    

