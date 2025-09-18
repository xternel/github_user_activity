import requests
import json

# Next: Code errrors - how to implement

# Next: take github username as an argunent
github_user = input("Please, enter your GitHub username: ")



# Next: fetch the user's recent activity using the GitHub API
url= "https://api.github.com/users/" + github_user + "/events"
user_data = requests.get(url)
print(user_data)
user_data = user_data.text

# Next: move into json file, prettify it with indent=4
with open("user_data.json", mode="w", encoding="utf-8") as write_file:
    write_data = json.loads(user_data)
    json.dump(write_data, write_file, indent=4)




    

# Next: display the fetched activity in the terminal.
with open("user_data.json", mode="r", encoding="utf-8") as read_file:
    read_data = json.load(read_file)
    print(read_data)

    for i in user_data:
        type_data = user_data[i]["Type"] 
        print(type_data)


        # if (i["Type"] == "Create"):
        #         print(i)
# Next: how to change that in array i will modify strings, not string indices






