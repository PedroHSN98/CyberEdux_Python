from docxtpl import DocxTemplate

nome_aluno = input("Digite o nome do aluno: ")
nome_curso = input("Digite o nome do curso: ")
carga_horaria = input("Digite a carga horária do curso: ")

documento = DocxTemplate('tpl.docx')

contexto = {
    'nome_aluno': nome_aluno,
    'nome_curso': nome_curso,
    'carga_horaria': carga_horaria
}

documento.render(contexto)

# Salvar o documento preenchido
documento.save('certificado.docx')

print("Certificado gerado com sucesso!")