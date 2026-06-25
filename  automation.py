import re

text = """
Nimmi mail ids:
nirmala@gmail.com
student123@yahoo.com
contact us at support@codealpha.tech
"""

emails = re.findall(r'\S+@\S+', text)

print("Extracted Emails:")
for email in emails:
    print(email)