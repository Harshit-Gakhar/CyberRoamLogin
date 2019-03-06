import requests     #To send form submission requests
f=open("data.txt", "r")     #open contents of file named 'data.txt' in the same folder
yee=str(f.read())           #get the text of file
arr=yee.split("\n")     #Split by new line, and store in an array
for i in arr:       
        un, pas=i.split()       #to get username and password
        data = {                #the request data to send
            'username': un,
            'password': pas,
            'mode': '191'
        }           
        url = "http://172.16.0.30:8090/httpclient.html"         #The login URL
        response = requests.post(url, data=data)        #To post the data
        if("You have successfully logged in"  in response.text):    #check if successful
            print("logged in with", un)
            break       #break out once logged in