from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    registers = []
    reg_list = []
    file_add = False

    for index in range(len(instance)):
        file = instance.search(index)
        lines = file["linhas_do_arquivo"]

        for j in range(len(lines)):
            if word.lower() in lines[j].lower():
                reg_list.append({"linha": j + 1})
                file_add = True

        if file_add:
            registers.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": reg_list
            })

    return registers


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
