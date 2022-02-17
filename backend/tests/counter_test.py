import azure.functions as func
from counter import main
 

def test_counter():
        request = func.HttpRequest(
            method='GET',
            url='/api/counter',
            body=None
        )
        outdoc = func.Document.from_dict({"id": 1, "count": 1})
        indoc = func.DocumentList([outdoc])
        outdoc.__setattr__('set', set)
        response = main(request, indoc, outdoc)
        assert response.status_code == 200
        assert int(response.get_body()) == 2
