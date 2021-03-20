from fastapi import status
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError


async def sqlalchemy_error(request: Request, exc: IntegrityError):
    msg = " ".join(exc.args).strip()
    code = status.HTTP_500_INTERNAL_SERVER_ERROR

    if "UNIQUE" in msg:
        duplicated_value = msg.split(":")[-1]
        msg = "Duplicated:" + duplicated_value
        code = status.HTTP_400_BAD_REQUEST
    return JSONResponse(content={"msg": msg}, status_code=code)


exception_handler = {IntegrityError: sqlalchemy_error}
