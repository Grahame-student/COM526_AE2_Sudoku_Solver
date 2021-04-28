from datetime import datetime

class saveToFile:

    start_time = datetime.now()
    
    def save(solution, iteration):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        solveTime = saveToFile.calculateTimeToSolve(now)
        with open("./solutions.txt", "a") as file:
            file.write(f"Date time of solution: {dt_string}\niterations: {iteration}\nSolution:\n{solution}\nTime to solve:\n {solveTime}\n\n\n")

    def calculateTimeToSolve(timeOfSolution):
        delta = timeOfSolution - saveToFile.start_time
        saveToFile.start_time = timeOfSolution
        return delta
