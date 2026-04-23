class Proceso:
    def __init__(self, pid, vruntime):
        self.pid = pid
        self.vruntime = vruntime
    def __repr__(self):
        return f"(PID={self.pid}, vruntime={self.vruntime})"