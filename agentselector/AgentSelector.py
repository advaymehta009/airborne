'''function --> input --> list of agents with their data, agent selection mode
--> returns a list of agents the issue should be presented to.  

--->given the following data for agents 
-->agent:-
    ->is_available(boolean value)
    ->available_since (the time since the agent is available)
    ->roles (a list of roles the user has, e.g. spanish speaker, sales, support etc.) 

'''
import json
from collections import deque
import datetime
import random

issue_queue = deque()
agent_list = []
assigned_list = []


def AgentSelector(agent_list, issue_queue, selection_mode):
    if selection_mode == 'all_available':
        for issue in list(issue_queue):
            for agent in range(len(agent_list)+1):
                if agents[agent_list[agent]]['agent_status'] == 1:
                    if issue_list[issue] == agents[agent_list[agent]]['role']:
                        a = issue_queue.popleft()
                        b = agent_list.pop(agent)
                        assigned_list.append((a,b))
                        break
        return assigned_list
    elif selection_mode == 'least_busy':
        lst_bsy_lst = sorted(agent_list, key=lambda x: (agents[x]['available_since'], agents[x]['agent_status']))
        for issue in list(issue_queue):
            for agent in range(len(lst_bsy_lst)+1):
                if issue_list[issue] == agents[agent_list[agent]]['role']:
                    a = issue_queue.popleft()
                    b = agent_list.pop(agent)
                    assigned_list.append((a,b))
                    break

        return assigned_list

    else:
        #random
        for _ in range(len(issue_queue)):
            a = issue_queue.popleft()
            b = random.choice(agent_list)
            agent_list.remove(b)
            assigned_list.append((a,b))

        return assigned_list
               

with open('C:\\Users\\advay\\OneDrive\\Documents\\Programs\\agentlist.json') as f:
    data = json.load(f)


agents = dict()
for agent in data['agents']:
    #print("agent_name: {}, is_available: {}, available_since: {}, role: {}".format(agent['name'], agent['is_available'], agent['available_since'], agent['role']))
    
    agent_name = agent['name']
    agents[agent_name] = {'agent_status' : agent['is_available'], 'available_since' : agent['available_since'], 'role' : agent['role'] }
    agent_list.append(agent_name)



with open('C:\\Users\\advay\\OneDrive\\Documents\\Programs\\issuequeue.json') as f1:
    iss_data = json.load(f1)

issue_list = dict()
for issue in iss_data['issues']:
    #print(f"issue_id: {issue['id']}, role: {issue['role']}")

    issue_id = issue['id']
    issue_role = issue['role']
    issue_list[issue_id] = issue_role
    issue_queue.append(issue_id)


test = int(input("Enter 1 for view Agent List , 2 for view Issue_List, 3 for view Issue_Queue, 4 for Get Assigned_List with Isuue_id\t"))
if test == 1:   
    print("Agent_List: ",agent_list)
    print()
elif test == 2:
    print("Issue_List: ",issue_list)
    print()
else:
    print("Issue_Queue: ",issue_queue)
    print()

mode = int(input("choose a selection mode: 1 for all_available , 2 for Least busy 3 for random\t"))
if mode == 1:
    selection_mode = 'all_available'
elif mode == 2:
    selection_mode = 'least_busy'
if mode == 3:
    selection_mode = 'random'
asign = AgentSelector(agent_list, issue_queue, selection_mode)
print("Issue_id, Agent_name: \n",asign)