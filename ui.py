@app.get('/')
def home(): 
    global outputString
    txtBox = fhtml.Input(id="userText", placeholder="E.g.: The woman painted the bald man's back blue")
    submit = fhtml.Button("Submit",id="submit", action="/", method="POST")
    responseLabel = fhtml.Label(outputString, id="response")
    return(fhtml.H1("Enter text!"), fhtml.H3(fhtml.Group(txtBox, submit), responseLabel))
@app.post("/")
def getResponse(usrInput):
    global outputString
    outputString = hello_func(usrInput)
    return home()

fhtml.serve()