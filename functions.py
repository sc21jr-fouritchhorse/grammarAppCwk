import functions_framework as googlefunc

@googlefunc.http
def hello_func(request: fhtml.Request) -> fhtml.Response:
    if request.form.get("submit"):
        return fhtml.Response(f"I got the text \"{request.form['userText']}\"!")
    else:
        return fhtml.Response("I have the request, but I didn't get anything!")
