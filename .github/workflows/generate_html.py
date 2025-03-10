import os
import glob
import re
from datetime import datetime

def get_projects():
    return sorted([f for f in os.listdir('Tests.github.io') 
                  if re.match(r'^\d+-', f)])

def generate_project_section(project_folder):
    project_path = f"Tests.github.io/{project_folder}"
    project_name = re.sub(r'^\d+-', '', project_folder).replace("-", " ").title()
    
    html = f"""
    <section id="{project_folder}">
        <h1>{project_name}</h1>
    """
    
    # Non-verbali documents
    non_verbali = []
    for doc in glob.glob(f"{project_path}/*.pdf"):
        if "verbali" not in doc:
            doc_name = os.path.basename(doc).replace(".pdf", "").replace("-", " ").title()
            non_verbali.append(f'<li><a href="{project_folder}/{os.path.basename(doc)}">{doc_name}</a></li>')
    
    if non_verbali:
        html += '<ul class="document-list">\n' + '\n'.join(non_verbali) + '</ul>'
    
    # Verbali subsections
    html += '<div class="verbali-container">'
    for tipo in ["interni", "esterni"]:
        verbali = sorted(glob.glob(f"{project_path}/verbali/{tipo}/*.pdf"), 
                       key=lambda x: os.path.basename(x), reverse=True)
        if verbali:
            html += f"""
            <div>
                <h2>Verbale {tipo[:-1].title()}</h2>
                <ul>
            """
            for pdf in verbali:
                date_str = os.path.basename(pdf).split('_')[1][:8]
                date = datetime.strptime(date_str, "%Y%m%d").strftime("%d/%m/%Y")
                html += f'<li><a href="{project_folder}/verbali/{tipo}/{os.path.basename(pdf)}">{date}</a></li>'
            html += '</ul></div>'
    html += '</div></section>'
    
    return html

def update_index():
    with open("Tests.github.io/index.html", "r") as f:
        content = f.read()
    
    projects = get_projects()
    projects_html = "\n".join([generate_project_section(p) for p in projects])
    
    # Define placeholders
    start_marker = "<!-- AUTO-GENERATED CONTENT START -->"
    end_marker = "<!-- AUTO-GENERATED CONTENT END -->"
    
    # Replace content between markers
    pattern = re.compile(f"{re.escape(start_marker)}.*?{re.escape(end_marker)}", re.DOTALL)
    new_content = re.sub(
        pattern,
        f"{start_marker}\n{projects_html}\n{end_marker}",
        content
    )
    
    with open("Tests.github.io/index.html", "w") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_index()
