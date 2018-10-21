import json
import apps.hello.models

helloModel = apps.hello.models

import apps.services.httpError

httpError = apps.services.httpError

###
# hello controllers
###
def hello(request):
    result = helloModel.hello()
    if (result["code"] == 200):
        return json.dumps(result["result"])
    else:
        return httpError.errorHTTP(result["code"], result["result"])