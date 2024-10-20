from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/ifelse/")
async def ifelse(
    a: int = Query(..., description="Nilai pertama"), 
    b: int = Query(..., description="Nilai kedua"), 
    opt: str = Query("*", description="Operasi aritmatika")
):
    if opt == "+":
        result = a + b
    elif opt == "-":
        result = a - b
    elif opt == "*":
        result = a * b
    elif opt == "/":
        if b != 0:
            result = a / b
        else:
            return {"code": 400, "mess": "Error: Division by zero"}
    else:
        return {"code": 400, "mess": "Error: Invalid operation"}
    
    return {
        "code": 200,
        "mess": "succ",
        "data": {
            "a": a,
            "b": b,
            "opt": opt,
            "result": result
        }
    }

@app.get("/switch_case/")
async def switch_case(
    a: int = Query(..., description="Nilai pertama"), 
    b: int = Query(..., description="Nilai kedua"), 
    opt: str = Query("*", description="Operasi aritmatika")
):
    switcher = {
        "+": a + b,
        "-": a - b,
        "*": a * b,
        "/": a / b if b != 0 else "Error: Division by zero"
    }
    result = switcher.get(opt, "Error: Invalid operation")
    
    if result == "Error: Division by zero":
        return {"code": 400, "mess": "Error: Division by zero"}
    elif result == "Error: Invalid operation":
        return {"code": 400, "mess": "Error: Invalid operation"}
    
    return {
        "code": 200,
        "mess": "succ",
        "data": {
            "a": a,
            "b": b,
            "opt": opt,
            "result": result
        }
    }

@app.get("/ternary/")
async def ternary_operation(
    a: int = Query(..., description="Nilai pertama"), 
    b: int = Query(..., description="Nilai kedua"), 
    opt: str = Query("*", description="Operasi aritmatika")
):
    result = (a + b) if opt == "+" else (a - b) if opt == "-" else (a * b) if opt == "*" else (a / b) if opt == "/" and b != 0 else "Error: Division by zero" if opt == "/" else "Error: Invalid operation"
    
    if result == "Error: Division by zero":
        return {"code": 400, "mess": "Error: Division by zero"}
    elif result == "Error: Invalid operation":
        return {"code": 400, "mess": "Error: Invalid operation"}
    
    return {
        "code": 200,
        "mess": "succ",
        "data": {
            "a": a,
            "b": b,
            "opt": opt,
            "result": result
        }
    }