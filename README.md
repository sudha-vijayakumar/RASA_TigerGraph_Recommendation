# Movie recommendations using RASA + TigerGraph

Conversational recommendation systems (CRS) using knowledge graphs is a hot topic as they intend to return the best real-time recommendations to users through a multi-turn interactive conversation. CRS allows users to provide their feedback during the conversation, unlike the traditional recommendation systems. CRS can combine the knowledge of the predefined user profile with the current user requirements to output custom yet most relevant recommendations or suggestions. This work will implement a chatbot using the open-source chatbot development framework - RASA and the most powerful, super-fast and leading cloud graph database - TigerGraph. 

**NOTE:**:
This help page will not go into the depth of RASA, TigerGraph functionalities. This help page will touchbase and demo how TigerGraph can be integrated with RASA.

## Technological Stack

Here is the high-level outline of the technological stack used in this demo project,
<p align="center">
<img src="https://github.com/sudha-vijayakumar/RASA_TigerGraph/blob/master/TechnicalStack.jpg" width="400" height="700">
</p>


## Putting things to work

### Step-1: **(RASA)** Implement language models, user intents and backend actions 

**Beginner tutorial:** This is a very good spot to learn about setting up a basic chatbot using RASA and understands the core framework constructs.
- https://rasa.com/docs/rasa/playground/

#### Install RASA

Open a new terminal and setup RASA using the below commands:

- $ python3 -m virtualenv -p python3 .
- $ source bin/activate
- $ pip install rasa

#### Create new RASA project
- $ rasa init

After the execution of the above command, a new RASA 'Movie_Chatbot' project will be created in the current directory as shown below,
Fig 1

Below is a kick-off conversation with the newly created chatbot,
Fig 2 

Ya, that's quiet simple to create a chatbot now with RASA!

#### Define intents, stories, action triggers
Now, navigate to the project folder Movie_Chatbot/data and modify the default nlu.yml and rules.yml files by adding intents, rules for our movie recommendation business usecase as show below,

Fig 3,4

Install the TigerGraph python library using pip with the below command,
- pip install pyTigerGraph

#### Define action endpoints
Now, navigate to the project folder Movie_Chatbot/actions and modify the actions.py file to include TigerGraph connection parameters and action definitions with the respective movie recommendation CSQL query as show below,

Fig 5,6


Here, 'RecommendMovies' is the name of the CSQL query in the tgcloud database which will discuss in detail in the next section.

With this step, we are done with the installation and configuration of RASA chatbot.

### Step-2: **(TigerGraph)** Setup TigerGraph database and querying APIs

**Beginner tutorial:** This is a very good spot to learn about setting up tigergraph database on the cloud and implement CSQL queries,
- https://www.tigergraph.com/blog/taking-your-first-steps-in-learning-tigergraph-cloud/

- Go to, http;//tgcloud.io/ and create a new account.
- Activate the account.
- Go to, "My Solutions" and click "Create Solution"
- Select the starter kit as shown below then click Next twice.
- Provide a solution name, password tags, and subdomain as needed and then click Next.
- Enter Submit and close your eyes for the magic!

And Yes!, the TigerGraph Movie recommendation Graph database is created. Hold on, there are few more things to do!

- Go to, GraphStudio and 'Load Data' by selecting the *.csv files and hitting on the 'play' button shown below. 
- Once the data is loaded, data statistics should display a green 'FINISHED' message as show below.
  Fig
  
- Go to, 'Write Queries' and implement the CSQL queries here as shown below, 
  Fig
- Save the CSQL query and publish it using the 'up arrow' button.

- Lets, test the query by running with a sample input as shown below,
  Fig
  
All Set! The TigerGraph Database is up and running. Are we done? Almost! There is one more thing to do!

- Let's set up the secret key access to the cloud TigerGraph API as it is very crucial to ensure a secure way of providing access to the data. 
- Go to, Admin Dashboard->Users->Management and define a secret key as shown below,
- 
- **NOTE:** Please remember to copy the key to be used in the RASA connection configuration (Movie_ChatBot/actions/actions.py)


### Step-3: **(Web UI)** Setting up a web ui for the RASA chatbot

- In this work, we are using a open-source javascript based chatbot UI to interact with the RASA solution we implemented in Step-1.
- The RASA server endpoint is configured in the Chatbot-Widget/static/Chat.js as shown below,
  Fig

Alright, we are one-step close to see the working of the TigerGraph and RASA integration.

### Step-4: **(RASA+TigerGraph)** Start RASA and run Actions

Run the below commands in separate terminals,

Terminal-1:
- $ rasa train
- $ rasa run -m models --enable-api --cors "*" --debug

Terminal-2:
- $ rasa run actions

### Step-5: **(ChatBot UI)** Open Chatbot User interface

Hit open Chatbot-Widget/index.html to start interacting with the TigerBot movie recommendation engine!

Yes, we are DONEEE! 

Below video will highlight the runtime of this setup and some sample real-time conversations using the power of RASA + TigerGraph,
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)


Hope, this source is informative and helpful.

