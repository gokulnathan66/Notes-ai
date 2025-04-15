from langchain.agents import create_sql_agent
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///mydb.sqlite")
llm = OpenAI(temperature=0)
agent_executor = create_sql_agent(llm=llm, db=db)

response = agent_executor.run("What was the total sales last quarter?")
print(response)
