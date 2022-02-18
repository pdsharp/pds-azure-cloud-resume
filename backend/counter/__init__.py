import logging
import azure.functions as func


def main(
    req: func.HttpRequest,
    indoc: func.DocumentList,
    outdoc: func.Out[func.Document]
    ) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')
    try:
        newcount = indoc[0]['count'] + 2
        dbupdate = {"id": '1', "count": newcount}
    except (IndexError):
        dbupdate = {"id": '1', "count": 1}
        newcount = dbupdate["count"]
    outdoc.set(func.Document.from_dict(dbupdate))
    func.HttpResponse.mimetype = 'application/json'
    return func.HttpResponse(
        f"{newcount}",
        status_code=200,
    )
