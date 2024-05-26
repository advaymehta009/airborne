The readme file for agent selector program.



Agent Selecter selects the right agent for a particular issue.

-------------------------------------

### AGENT CREATION:

First the user will create a number of agents and will include various details like if the agent is currently available for handling any issue of not and fill the time according to it. If user is not free then you will provide the time needed by agent to be free.
Then user will assign various roles to specific agents(one or many).
-------------------------------------

### ISSUES CREATION

User will create number of issues which are prioritized by their creation(i.e first created will have the highest priority).
Issues will also have roles which are needed to be completed.
Then the user will input agent selection mode:
1: All avilable: In this mode the issue is presented to all agents so they pick the issue if they want.
2:Least busy :In this mode  the issue is presented to the agent that has been available for the longest.
3:Random mode:In random mode we randomly pick an agent.
User will will also enter the time needed to complete this particular issue(say x) so that when the agent is assigned with the issue, its availability will be "False" and will again be "True" after x amount of time.

-------------------------------------

### AGENT SELECTOR

After getting all the issues and agents it is time to assign each issue to agents.
Issue that is created first will be checked first.
Issue will be compared with all the agents on the basis of their roles(i.e roles present in issue must also be present in agents) and their availability(i.e True or False).
If there are more than 1 agents that satisfy the the issue,agents will be selected by agent selection mode as discussed above.
In all available user can choose between the agents that meet up the criteria of the issue.
In other modes the program will choose the agent itself.

After selecting the particular agent its availability will turn to "False".
All the other agents having "True" availability will increament their "availability time" by 1.
All the other agents having "False" availability will decreament their "issue resolving time" by 1.

In the program the Time is increamented or decreamented on the basis of Iteration(looping) of the agents.
After one iteration the time will increase/decrease by 1.

-------------------------------------
