from passlib.context import CryptContext


pwd_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hashed_password(password):
    return pwd_context.hash(password)


def verify_password(
    password,
    hashed_passsword
):
    return pwd_context.verify(
        password,
        hashed_passsword
    )
              