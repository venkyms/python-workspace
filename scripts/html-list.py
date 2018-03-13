def html_list(data_list):
    """
    Generate html document list from input string list
    :param data_list: string which needs to be converted as html list
    :return: html document string
    """

    html_doc = ['<ul>']
    for data in data_list:
        html_doc.append('<li>' + data + '</li>')

    html_doc.append('</ul>')

    return "\n".join(html_doc)


print(html_list(['first string', 'second string']))
