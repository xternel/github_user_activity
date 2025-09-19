import requests
import json

# Next: Code errrors - how to implement

# Next: take github username as an argunent
try:
    github_user = input("Please, enter your GitHub username: ")


    # Next: fetch the user's recent activity using the GitHub API
    url= "https://api.github.com/users/" + github_user + "/events"
    user_data = requests.get(url)
    user_data = user_data.text

    # Next: move into json file, prettify it with indent=4
    with open("user_data.json", mode="w", encoding="utf-8") as write_file:
        write_data = json.loads(user_data)
        json.dump(write_data, write_file, indent=4)


        

    # Next: display the fetched activity in the terminal.

    with open("user_data.json", mode="r", encoding="utf-8") as read_file:
        if(read_file.read(2) == '[]'):
            print("User's activity is hidden")
        else:

            read_data = json.load(read_file)
            n = 0
            push_event = 0
            create_event = 0
            fork_event = 0

            for i in read_data:
                type_data = read_data[n]["type"]
                repo_data = read_data[n]["repo"]["name"]
        
                if (type_data == "PushEvent"):
                    commit_data = read_data[n]["payload"]["commits"]
                    commit_number = 0
                    for commits in commit_data:
                        commit_number = commit_number + 1 
                        if (commit_number == 1):
                            print("Pushed " + str(commit_number) + " commit to " + repo_data)
                        if (commit_number > 1):
                            print("Pushed " + str(commit_number) + " commits to " + repo_data)

                elif (type_data == "CreateEvent"):
                    print("Created " + repo_data + " repo")
                

                elif (type_data == "ForkEvent"):
                    print("Forked " + repo_data + " repo")

                elif(type_data == "IssuesEvent"):
                    print("Opened " + type_data + "issue in " + repo_data + " repo")
            
            
                n = n + 1


except: 
    print("Error 404: not found")








