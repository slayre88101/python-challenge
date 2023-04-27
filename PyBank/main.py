#Python Project PyPoll
  import pandas as pd
  from pathlib import Path
  import csv
#Load in file
#Store filepath in a variable
  election_data = Path("/kaggle/input/python-project-3/Starter_Code/PyPoll/Resources/election_data.csv")
 #Read and display the CSV with Pandas
  pypoll_df=pd.read_csv(election_data)
  pypoll_df.head()
  #count the total number of votes
votes_df = pypoll_df["Ballot ID"].count()
votes_df
#count the total list of candidates that received votes
candidates_df = pypoll_df["Candidate"].value_counts()
candidates_df
#count the total percentage of votes received
candidates = pypoll_df["Candidate"].value_counts()
candidates_divided = candidates/votes_df
percentage_of_votes_df = candidates_divided
pd.options.display.float_format = '{:,.2%}'.format
percentage_of_votes_df
#Name the Winner
winner = pypoll_df["Candidate"].mode()
winner
#Summary

summary_df= {
"Total number of votes": [votes_df],
"Per candidate": [candidates],
"Percentage per candidate": [percentage_of_votes_df],
"Winner":[winner]
}
info_df = pd.DataFrame(summary_df, columns=["Total number of votes", "Per candidate", "Percentage per candidate","Winner"])
info_df
#Save to CSV
info_df.to_csv('PyPoll.csv',index=False)
