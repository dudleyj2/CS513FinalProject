import markdown

with open('final_project.md', 'r') as f:
    text = f.read()
    html = markdown.markdown(text)

with open('final_project.html', 'w') as f:
    f.write(html)