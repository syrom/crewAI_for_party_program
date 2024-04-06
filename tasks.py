from textwrap import dedent
from crewai import Task

class PoliticalProgramTasks():
	def research_task(self, agent, participants, context):
		return Task(
			description=dedent(f"""\
				Conduct comprehensive research on each typical domain of interest in the context
                of municipal elections. Gather information on needs, known problems and recent developments 
                in the respective domains.
				Participants: {participants}
				Political Program Context: {context}"""),
			expected_output=dedent("""\
				A detailed report summarizing key findings about each domain, 
				highlighting information that could be relevant for the election program."""),
			async_execution=True,
			agent=agent
		)

	def priority_analysis_task(self, agent, participants, context):
		return Task(
			description=dedent(f"""\
				Analyze the current trends, challenges, and opportunities
				of European urban politics for large cities. Consider recent
				developments and expert opinions to provide a priortiy list covering 
				all domains of urban politics that dominate the public discussion in Europe.
				Participants: {participants}
				Political Program Context: {context}"""),
			expected_output=dedent("""\
				A list of 8 domains of urban politics that rank high
				in public discussion."""),
			async_execution=True,
			agent=agent
		)

	def political_strategy_task(self, agent, context, objective):
		return Task(
			description=dedent(f"""\
				Formulate concrete political demands for the domains identified through the priortiy analysis.
                The demands must aligning with the liberal views of participants.
				Political Program Context: {context}
				Political Program Objective: {objective}"""),
			expected_output=dedent("""\
				Provide a list of concrete political demands for each domain to draft a comprehensive 
                municipal election program that reflects the liberal views of Paricipants."""),
			agent=agent
		)

	def draft_task(self, agent, context, objective):
		return Task(
			description=dedent(f"""\
				Fuse the policitcal demands per domain to create a comprehensive municipal election program.
				Ensure the municipal election program is easy to digest and the tone of voice resonates well with liberally minded citizens.
				Political Program Context: {context}
				Political Program Objective: {objective}"""),
			expected_output=dedent("""\
				A liberal municipal election program that is structured with one sections for each identified municipal policy domain,
				listing the political demands associated with the respective domain."""),
			agent=agent
		)
