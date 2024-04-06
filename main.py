import os
from contextlib2 import redirect_stdout
from crewai import Crew
from tasks import PoliticalProgramTasks
from agents import PoliticalProgramAgents

# Set up the environment for AI model interaction
os.environ["OPENAI_API_KEY"] = "null"
os.environ["OPENAI_API_BASE"]='http://localhost:11434/v1'
os.environ["OPENAI_MODEL_NAME"]="mixtral"

#####################################################################
# Establish a liberal election program for a municipal election
#####################################################################

tasks = PoliticalProgramTasks()
agents = PoliticalProgramAgents()

print("## Welcome to the the Municipal Election Program AI Crew")
print('-------------------------------')

participants = "free market liberals ; socially oriented liberal"
context="A municipal election will take place in a modern, globally connected major German city. "\
          "A liberal party must draft an election program for this election."\
		  "Participants are the party's two main factions. Both participants want to see their core values represented "\
		  "in the final election program."          
objective = "Establish an election program for a municipal election, formulating political demands based on liberal values.  " \
			"The political demands must be structured by domains. "\
			"The domains coverd in the result should include relevant aspects of municipal politics resulting. "\
            "The following domains MUST be included in the result: "\
            "- traffic and transportation "\
            "- housing "\
            "- schooling "\
            "- security "\
            "- culture "\
            "- sustainability  "\
            "- quality of life "\
            "- administrative efficiency."

# Create Agents
researcher_agent = agents.research_agent()
priority_analyst_agent = agents.priority_analysis_agent()
political_strategy_agent = agents.political_strategy_agent()
draft_agent = agents.draft_agent()

# Create Tasks
research = tasks.research_task(researcher_agent, participants, context)
priority_analysis = tasks.priority_analysis_task(priority_analyst_agent, participants, context)
political_strategy = tasks.political_strategy_task(political_strategy_agent, context, objective)
draft = tasks.draft_task(draft_agent, context, objective)

political_strategy.context = [research, priority_analysis]
draft.context = [research, priority_analysis, political_strategy]

# Create Crew responsible for Copy
crew = Crew(
	agents=[
		researcher_agent,
		priority_analyst_agent,
		political_strategy_agent,
		draft_agent
	],
	tasks=[
		research,
		priority_analysis,
		political_strategy,
		draft
	],
    verbose=True
)

# Open the file "process_and_outcome.txt" in write mode ('w')
with open("_process_and_result.txt", "w") as file:
    # Redirect stdout to the file
    with redirect_stdout(file):
        crew.kickoff()
print("FINISHED")

# ALTERNATIVE: OUTPUT IN TERMINAL
#program = crew.kickoff()
# Print results
#print("\n\n################################################")
#print("## Here is the result")
#print("################################################\n")
#print(program)
