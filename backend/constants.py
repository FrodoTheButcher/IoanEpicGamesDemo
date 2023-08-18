
class ErrorMessage:
    POST_REQUEST_ERROR = {"errorMessage":"Bad credentials ,  try with different data"}
    POST_REQUEST_SERVER = {"errorMessage":"Request failed,try again later"}

    GETBYID_NOTFOUND = {"errorMessage":"Your id was not found,try again later"}
    GETBYID_SERVERERROR= {"errorMessage":"Request failed,try again later"}

    
class Data:
    def ReturnResponse(data):
        return {"data":data}