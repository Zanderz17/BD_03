from flask import Blueprint, current_app, jsonify
main = Blueprint('search_python_blueprint', __name__)


@main.route('/<query>/<topk>')
def SearchPython(query, topk):
    instance = current_app.config['PrincipalClass']

    result_list, execution_time = instance.search(query, topk)

    docs_list = []
    for result in result_list:
        temp_doc = {}
        temp_doc["id"] = result['id'];
        temp_doc["score"] = result['score']
        temp_doc["title"] = result['title']
        docs_list.append(temp_doc)    

    result = {'docs_list': docs_list, 'execution_time':execution_time}
    return jsonify(result)
