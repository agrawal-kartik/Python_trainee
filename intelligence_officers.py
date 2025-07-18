import random

first_names = ["James", "Sarah", "Michael", "Laura", "David", "Emma", "John", "Emily", "Robert", "Olivia"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
designations = ["Field Agent", "Analyst", "Tech Operative", "Intel Officer", "Surveillance Expert", "Cybersecurity Lead"]
indian_cities = [
    "Delhi", "Mumbai", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Ahmedabad",
    "Pune", "Jaipur", "Lucknow", "Bhopal", "Patna", "Chandigarh", "Indore", "Nagpur",
    "Kanpur", "Surat", "Ranchi", "Guwahati", "Thiruvananthapuram"
]

rows = []
for _ in range(100):
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    salary = random.randint(60000, 150000)
    designation = random.choice(designations)
    hometown = random.choice(indian_cities)
    row = f"<tr><td>{name}</td><td>{salary}</td><td>{designation}</td><td>{hometown}</td></tr>"
    rows.append(row)

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Intelligence Officers</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        th, td {{
            border: 1px solid #666;
            padding: 8px 12px;
            text-align: left;
        }}
        th {{
            background-color: #003366;
            color: white;
        }}
        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
        caption {{
            font-size: 24px;
            margin-bottom: 10px;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <table>
        <caption>Intelligence Officers</caption>
        <thead>
            <tr>
                <th>Name</th>
                <th>Salary ($)</th>
                <th>Designation</th>
                <th>Hometown</th>
            </tr>
        </thead>
        <tbody>
            {''.join(rows)}
        </tbody>
    </table>
</body>
</html>
"""

# Save to a file
with open("intelligence_officers_india.html", "w") as file:
    file.write(html_content)
