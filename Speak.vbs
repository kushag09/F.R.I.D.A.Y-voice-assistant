Dim message, sapi
message=("Please wait while I install my dependency modules. This may take a while depending on the speed of your connection")
Set sapi=CreateObject("sapi.spvoice")
Set sapi.Voice = sapi.GetVoices.Item(1)
sapi.Rate = 0
sapi.volume = 100
sapi.Speak message