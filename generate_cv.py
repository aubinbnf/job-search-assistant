import json
from jinja2 import Template
from src.models.profile import UserProfile
import subprocess
import os

def generate_cv():
    with open('data/user_profile.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    profile = UserProfile(**data)
    print("✅ Données validées avec Pydantic")

    with open('src/templates/cv_template.tex', 'r', encoding='utf-8') as f:
        template_content = f.read()

    template = Template(template_content)
    latex_filled = template.render(**profile.model_dump())
    print("✅ Template rempli avec Jinja2")

    os.makedirs('generated_cvs', exist_ok=True)
    with open('generated_cvs/cv.tex', 'w', encoding='utf-8') as f:
        f.write(latex_filled)
    print("✅ Fichier LaTeX généré : generated_cvs/cv.tex")

    result = subprocess.run(
        ['pdflatex', '-output-directory=generated_cvs', '-interaction=nonstopmode', 'generated_cvs/cv.tex'],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print("✅ CV généré avec succès : generated_cvs/cv.pdf")
    else:
        print("❌ Erreur lors de la compilation LaTeX")
        print(result.stdout)
        print(result.stderr)

if __name__ == "__main__":
    generate_cv()
