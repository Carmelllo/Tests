import os
import glob
import re
from datetime import datetime

def get_projects():
    """Find all numbered project folders (1-candidatura, 2-rtb, etc.)"""
    return sorted(
        [f for f in os.listdir('Tests.github.io') 
         if re.match(r'^\d+-', f) and os.path.isdir(os.path.join('Tests.github.io', f))],
        key=lambda x: int(x.split('-')[0])
    )

def generate_project_section(project_folder):
    project_path = f"Tests.github.io/{project_folder}"
    project_name = re.sub(r'^\d+-', '', project_folder).replace("-", " ").title()
    
    html = f"""
    <section id="{project_folder}">
        <h1>{project_name}</h1>
    """
    
    # Non-verbali documents (include root-level PDFs)a
    non_verbali = []
    for doc in glob.glob(f"{project_path}/**/*.pdf", recursive=True):
        # Check if "verbali" is in the relative path from the project folder
        if "verbali" not in os.path.relpath(doc, project_path):
            rel_path = os.path.relpath(doc, project_path)
            doc_name = os.path.basename(doc).replace(".pdf", "").replace("-", " ").title()
            non_verbali.append(f'<li><a href="{project_folder}/{rel_path}">{doc_name}</a></li>')
    
    if non_verbali:
        print("AaaAaaaaaaaaaaaaa")
        html += '<ul class="document-list">\n' + '\n'.join(non_verbali) + '</ul>'
    
    # Verbali subsections
    html += '<div class="verbali-container">'
    for tipo in ["interni", "esterni"]:
        verbali = sorted(glob.glob(f"{project_path}/verbali/{tipo}/*.pdf"), 
                       key=lambda x: os.path.basename(x), reverse=True)
        if verbali:
            html += f"""
            <div>
                <h2>Verbali {tipo.title()}</h2>
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
    
    # Generate aside links with acronym handling
    projects = get_projects()
    aside_links = []
    for p in projects:
        name_part = p.split("-", 1)[1] if "-" in p else p
        if name_part.islower() and 3 <= len(name_part) <= 5:
            display_name = name_part.upper()
        else:
            display_name = name_part.replace("-", " ").title()
        aside_links.append(f'<li><a href="#{p}">{display_name}</a></li>')
    
    aside_start = "<!-- AUTO-GENERATED ASIDE START -->"
    aside_end = "<!-- AUTO-GENERATED ASIDE END -->"
    aside_pattern = re.compile(f"{re.escape(aside_start)}.*?{re.escape(aside_end)}", re.DOTALL)
    new_aside_content = f"{aside_start}\n{''.join(aside_links)}\n{aside_end}"
    content = aside_pattern.sub(new_aside_content, content)
    
    # Generate main contenta
    projects_html = "\n".join([generate_project_section(p) for p in projects])
    start_marker = "<!-- AUTO-GENERATED CONTENT START -->"
    end_marker = "<!-- AUTO-GENERATED CONTENT END -->"
    pattern = re.compile(f"{re.escape(start_marker)}.*?{re.escape(end_marker)}", re.DOTALL)
    content = re.sub(pattern, f"{start_marker}\n{projects_html}\n{end_marker}", content)
    
    # Save changes
    with open("Tests.github.io/index.html", "w") as f:
        f.write(content)

if __name__ == "__main__":
    update_index()
