from fastapi import FastAPI


def multiplication(firstNumber, secondNumber):
    return (firstNumber * secondNumber)


app = FastAPI()

@app.get("/")
async def pickArgs(first_number: int = 0, second_number: int = 0):
    return multiplication(first_number, second_number)
