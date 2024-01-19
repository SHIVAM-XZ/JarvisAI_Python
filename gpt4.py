import g4f

def Gpt(message):
    try:
        response = g4f.ChatCompletion.create(
            model= "gpt-4-32k-0613",
            provider= g4f.Provider.GPTalk,  # Provider is a module
            messages=[{"role":"user", "content":message}],# content is set by provided message
            stream=True # for smooth transition
        )
        mg=""
        for i in response:
            mg+=i
            print(i,end="",flush=True)
        return mg

    except:
        print("some error occured")
