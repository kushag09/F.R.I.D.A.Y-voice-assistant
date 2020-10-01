Dim message, sapi
message=("Hello. I am Friday. Your new personal assistant. Please say my name to activate me.")
Set sapi=CreateObject("sapi.spvoice")
Set sapi.Voice = sapi.GetVoices.Item(1)
sapi.Rate = 0
sapi.volume = 100
sapi.Speak message