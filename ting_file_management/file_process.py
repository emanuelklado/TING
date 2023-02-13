from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer

def process(path_file, instance):
    if len(instance) > 0:
        for i in range(len(instance)):
            if instance.search(i)["nome_do_arquivo"] == path_file:
                return

    file_result = txt_importer(path_file)

    file_formated = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_result),
        "linhas_do_arquivo": file_result,
    }

    print(file_formated)
    instance.enqueue(file_formated)

def remove(instance):
    if len(instance) < 1:
        print("Não há elementos")
    else:
        file = instance.dequeue()["nome_do_arquivo"]
        print(f"Arquivo {file} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
