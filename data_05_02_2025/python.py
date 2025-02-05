#pip install docxtpl
from docxtpl import DocxTemplate

documento = DocxTemplate('tpl.docx')

contexto = {
    'nome': 'Pedro'
}

documento.render(contexto)
documento.save('documento.docx')