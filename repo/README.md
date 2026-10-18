# IT Service Desk Ticket Analysis — SLA & Incident Trends

Analysis of IT helpdesk ticket data to measure **SLA breach rates** by priority,
category and time of day, and to find peak hours and recurring incident types.

> **Data note:** this repo uses a **synthetic sample dataset** (`data/sample_tickets.csv`).
> No real company or client data is included.

## Tech stack
Python, Pandas, MySQL, Seaborn

## What the project does
- Cleans the raw ticket data (types, missing values, duplicates)
- Uses SQL (joins, window functions) to calculate SLA breach rates
- Breaks breaches down by priority, category and hour of day
- Visualizes peak hours and recurring incident types
- Summarizes staffing and root-cause recommendations

## Project structure
```
data/sample_tickets.csv      # synthetic sample data
generate_sample_data.py      # creates the sample data
<your notebook / script>     # <-- add your file name(s) here
requirements.txt
README.md
```

## How to run
```bash
git clone https://github.com/NikitaSinghCSE/<repo-name>.git
cd <repo-name>
pip install -r requirements.txt
python generate_sample_data.py      # optional: regenerate sample data
jupyter notebook                    # open the analysis notebook
```

## Key findings
<!-- Fill in with YOUR results from the sample data, e.g.:
- Overall SLA breach rate: __%
- Highest breach rate: __ priority / __ category
- Peak ticket hours: __ -->

## Author
Nikita Singh  [LinkedIn](https://linkedin.com/in/nikita-singh-cse)
